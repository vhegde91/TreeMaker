#include "FWCore/Framework/interface/stream/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Common/interface/PtrVector.h"

#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "CommonTools/Utils/interface/StringCutObjectSelector.h"

class BadGlobalMuonTagger : public edm::stream::EDFilter<> {
    public:
        explicit BadGlobalMuonTagger(const edm::ParameterSet & iConfig);
        virtual ~BadGlobalMuonTagger() {}

        virtual bool filter(edm::Event & iEvent, const edm::EventSetup & iSetup) override;

    private:
        edm::EDGetTokenT<edm::View<reco::Muon>> muons_;            
        edm::EDGetTokenT<std::vector<reco::Vertex>> vtx_;            
        double ptCut_;
        bool   selectClones_, taggingMode_, verbose_;

        bool outInOnly(const reco::Muon &mu) const {
            const reco::Track &tk = *mu.innerTrack();
            return tk.algoMask().count() == 1 && tk.isAlgoInMask(reco::Track::muonSeededStepOutIn);
        }
        bool preselection(const reco::Muon &mu) const { 
            return (!selectClones_ || outInOnly(mu));
        }
        bool tighterId(const reco::Muon &mu) const { 
            return muon::isMediumMuon(mu) && mu.numberOfMatchedStations() >= 2; 
        }
        bool tightGlobal(const reco::Muon &mu) const {
            return mu.isGlobalMuon() && (mu.globalTrack()->hitPattern().muonStationsWithValidHits() >= 3 && mu.globalTrack()->normalizedChi2() <= 20);
        }
        bool safeId(const reco::Muon &mu) const { 
            if (mu.muonBestTrack()->ptError() > 0.2 * mu.muonBestTrack()->pt()) { return false; }
            return mu.numberOfMatchedStations() >= 1 || tightGlobal(mu);
        }
        bool partnerId(const reco::Muon &mu) const {
            return mu.pt() >= 10 && mu.numberOfMatchedStations() >= 1;
        }
        bool badTrk(const reco::Muon &mu) const {
            bool isBadTrkMuLoose = false;
            bool goodQualityTrack = true;
            if (!(mu.isPFMuon() && mu.isTrackerMuon() && mu.numberOfMatchedStations()>0)) isBadTrkMuLoose = true;
            if (mu.innerTrack().isNonnull()) {
                goodQualityTrack = (mu.innerTrack()->numberOfValidHits()>=10||(mu.innerTrack()->numberOfValidHits()>=7 && mu.innerTrack()->numberOfLostHits()==0));
            }
            return (isBadTrkMuLoose || !goodQualityTrack);
        }
};

BadGlobalMuonTagger::BadGlobalMuonTagger(const edm::ParameterSet & iConfig) :
    muons_(consumes<edm::View<reco::Muon>>(iConfig.getParameter<edm::InputTag>("muons"))),
    vtx_(consumes<std::vector<reco::Vertex>>(iConfig.getParameter<edm::InputTag>("vtx"))),
    ptCut_(iConfig.getParameter<double>("muonPtCut")),
    selectClones_(iConfig.getParameter<bool>("selectClones")),
    taggingMode_(iConfig.getParameter<bool> ("taggingMode")),
    verbose_(iConfig.getUntrackedParameter<bool> ("verbose",true))
{
    if (selectClones_) {
        produces<bool>("dup");
        produces<double>("dupLeadPt");
    }
    else {
        produces<bool>("bad");
        produces<double>("badLeadPt");
        produces<bool>("badTrk");
        produces<double>("badTrkLeadPt");
    }
}


bool 
BadGlobalMuonTagger::filter(edm::Event & iEvent, const edm::EventSetup & iSetup) {
    using namespace edm;

    // read input
    Handle<edm::View<reco::Muon>> hmuons;
    Handle<std::vector<reco::Vertex>> vtx;
    std::vector<int> goodMuon;

    iEvent.getByToken(vtx_,  vtx);
    assert(vtx->size() >= 1);
    const auto &PV = vtx->front().position();

    iEvent.getByToken(muons_,  hmuons);
    const edm::View<reco::Muon> & muons = *hmuons;
    bool foundBadTrk = false;
    double foundBadTrkPt = 0.0;
    for (const reco::Muon & mu : muons) {
        if(!selectClones_ and badTrk(mu)){
            foundBadTrk = true;
            if(mu.pt() > foundBadTrkPt) foundBadTrkPt = mu.pt();
        }
        if (!mu.isPFMuon() || mu.innerTrack().isNull()) {
            goodMuon.push_back(-1); // bad but we don't care
            continue;
        } 
        if (preselection(mu)) {
            float dxypv = std::abs(mu.innerTrack()->dxy(PV));
            float dzpv  = std::abs(mu.innerTrack()->dz(PV));
            if (tighterId(mu)) {
                bool ipLoose = ((dxypv < 0.5 && dzpv < 2.0) || mu.innerTrack()->hitPattern().pixelLayersWithMeasurement() >= 2);
                goodMuon.push_back(ipLoose || (!selectClones_ && tightGlobal(mu)));
            } else if (safeId(mu)) {
                bool ipTight = (dxypv < 0.2 && dzpv < 0.5);
                goodMuon.push_back(ipTight);
           } else {
                goodMuon.push_back(0);
            }
        } else {
            goodMuon.push_back(3); // maybe good, maybe bad, but we don't care
        }
    }

    bool foundBad = false;
    double foundBadPt = 0.0;
    bool foundDup = false;
    double foundDupPt = 0.0;
    for (unsigned int i = 0, n = muons.size(); i < n; ++i) {
        if(!verbose_ and (selectClones_ ? foundDup : foundBad)) break; //end loop if we know the event is bad
        if (muons[i].pt() < ptCut_ || goodMuon[i] != 0) continue;
        if (verbose_) printf("potentially bad muon %d of pt %.1f eta %+.3f phi %+.3f\n", int(i+1), muons[i].pt(), muons[i].eta(), muons[i].phi());
        foundBad = true;
        if(muons[i].pt() > foundBadPt) foundBadPt = muons[i].pt();
        if (selectClones_) {
            unsigned int n1 = muons[i].numberOfMatches(reco::Muon::SegmentArbitration);
            for (unsigned int j = 0; j < n; ++j) {
                if (j == i || goodMuon[j] <= 0 || !partnerId(muons[j])) continue;
                unsigned int n2 = muons[j].numberOfMatches(reco::Muon::SegmentArbitration);
                if (deltaR2(muons[i],muons[j]) < 0.16 || (n1 > 0 && n2 > 0 && muon::sharedSegments(muons[i],muons[j]) >= 0.5*std::min(n1,n2))) {
                    if (verbose_) printf("     tagged as clone of muon %d of pt %.1f eta %+.3f phi %+.3f\n", int(j+1), muons[j].pt(), muons[j].eta(), muons[j].phi());
                    foundDup = true;
                    if(muons[i].pt() > foundDupPt) foundDupPt = muons[i].pt();
                    break;
                } 
            }
        }
    }

    if (selectClones_) {
        auto outDup = std::make_unique<bool>(foundDup);
        auto outDupPt = std::make_unique<double>(foundDupPt);
        iEvent.put(std::move(outDup), "dup");
        iEvent.put(std::move(outDupPt), "dupLeadPt");
        return taggingMode_ || foundDup;
    }
    else {
        auto outBad = std::make_unique<bool>(foundBad);
        auto outBadPt = std::make_unique<double>(foundBadPt);
        auto outBadTrk = std::make_unique<bool>(foundBadTrk);
        auto outBadTrkPt = std::make_unique<double>(foundBadTrkPt);
        iEvent.put(std::move(outBad), "bad");
        iEvent.put(std::move(outBadPt), "badLeadPt");
        iEvent.put(std::move(outBadTrk), "badTrk");
        iEvent.put(std::move(outBadTrkPt), "badTrkLeadPt");
        return taggingMode_ || foundBad;
    }
}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(BadGlobalMuonTagger);
