// -*- C++ -*-
//
// Package:    LeptonProducer
// Class:      LeptonProducer
//
/**\class LeptonProducer LeptonProducer.cc RA2Classic/LeptonProducer/src/LeptonProducer.cc
 * 
 * Description: [one line class summary]
 *
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger,68/111,4719,
//         Created:  Fri Apr 11 16:35:33 CEST 2014
// $Id$
//
//


// system include files

#include <cmath>
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

#include "TVector2.h"

#include "TreeMaker/Utils/interface/get_isolation_activity.h"
//
// class declaration
//



class LeptonProducer : public edm::EDProducer {
  enum elecIDLevel {VETO, LOOSE, MEDIUM, TIGHT};
public:
  explicit LeptonProducer(const edm::ParameterSet&);
  ~LeptonProducer();
        
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  float MTWCalculator(double metPt,double  metPhi,double  lepPt,double  lepPhi);
  bool MuonID(const pat::Muon & muon, const reco::Vertex& vtx);
  bool MuonIDtight(const pat::Muon & muon, const reco::Vertex& vtx);
  bool ElectronID(const pat::Electron & electron, const reco::Vertex & vtx, const elecIDLevel level);
        
private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
        
  virtual void beginRun(edm::Run&, edm::EventSetup const&);
  virtual void endRun(edm::Run&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  edm::InputTag MuonTag_, ElecTag_, PrimVtxTag_, metTag_, PFCandTag_, RhoTag_;
  edm::EDGetTokenT<edm::View<pat::Muon>> MuonTok_;
  edm::EDGetTokenT<edm::View<pat::Electron>> ElecTok_;
  edm::EDGetTokenT<reco::VertexCollection> PrimVtxTok_;
  edm::EDGetTokenT<edm::View<pat::MET>> metTok_;
  edm::EDGetTokenT<pat::PackedCandidateCollection> PFCandTok_;
  edm::EDGetTokenT<double> RhoTok_;
  double minElecPt_, maxElecEta_, minMuPt_, maxMuEta_;
  bool useMiniIsolation_;
  double muIsoValue_, elecIsoValue_;
  SUSYIsolation SUSYIsolationHelper;
        
        
  // ----------member data ---------------------------


};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
LeptonProducer::LeptonProducer(const edm::ParameterSet& iConfig)
{
  //register your product
  MuonTag_                                 =         iConfig.getParameter<edm::InputTag >("MuonTag");
  ElecTag_                                 =         iConfig.getParameter<edm::InputTag >("ElectronTag");
  PrimVtxTag_=iConfig.getParameter<edm::InputTag>("PrimaryVertex");
  minElecPt_=iConfig.getParameter<double>          ("minElecPt");
  maxElecEta_=iConfig.getParameter<double>          ("maxElecEta");
  minMuPt_=iConfig.getParameter<double>          ("minMuPt");
  maxMuEta_=iConfig.getParameter<double>          ("maxMuEta");
  useMiniIsolation_ = iConfig.getParameter<bool>("UseMiniIsolation");
  muIsoValue_=iConfig.getParameter<double>          ("muIsoValue");
  elecIsoValue_=iConfig.getParameter<double>          ("elecIsoValue");
  metTag_   = iConfig.getParameter<edm::InputTag> ("METTag");
  RhoTag_ = edm::InputTag("fixedGridRhoFastjetCentralNeutral");
  PFCandTag_ = edm::InputTag("packedPFCandidates");
  
  MuonTok_ = consumes<edm::View<pat::Muon>>(MuonTag_);
  ElecTok_ = consumes<edm::View<pat::Electron>>(ElecTag_);
  PrimVtxTok_ = consumes<reco::VertexCollection>(PrimVtxTag_);
  metTok_ = consumes<edm::View<pat::MET>>(metTag_);
  PFCandTok_ = consumes<pat::PackedCandidateCollection>(PFCandTag_);
  RhoTok_ = consumes<double>(RhoTag_);
        
  produces<std::vector<pat::Muon> > ("IdMuon");
  produces<std::vector<bool> > ("IdMuonTightID");
  produces<std::vector<pat::Muon> > ("IdIsoMuon");
  produces<std::vector<bool> > ("IdIsoMuonTightID");
  produces<std::vector<int> >("MuonCharge");
  produces<std::vector<pat::Electron> > ("IdElectron");
  produces<std::vector<bool> > ("IdElectronMediumID");
  produces<std::vector<bool> > ("IdElectronTightID");
  produces<std::vector<pat::Electron> > ("IdIsoElectron");
  produces<std::vector<bool> > ("IdIsoElectronMediumID");
  produces<std::vector<bool> > ("IdIsoElectronTightID");
  produces<std::vector<int> >("ElectronCharge");
  produces<std::vector<double> >("MuIDMTW");
  produces<std::vector<double> >("MuIDIsoMTW");
  produces<std::vector<double> >("ElecIDMTW");
  produces<std::vector<double> >("ElecIDIsoMTW");
  
  produces<int>("");        
}


LeptonProducer::~LeptonProducer()
{
        
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
        
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void LeptonProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  //  std::cout<<"Running LeptonProducer"<<std::endl;
 
  using namespace edm;

  auto isoElectrons = std::make_unique<std::vector<pat::Electron>>();
  auto idElectrons = std::make_unique<std::vector<pat::Electron>>();
  auto isoMuons = std::make_unique<std::vector<pat::Muon>>();
  auto idMuons = std::make_unique<std::vector<pat::Muon>>();
  
  auto MuonCharge = std::make_unique<std::vector<int>>();
  auto ElectronCharge = std::make_unique<std::vector<int>>();

  auto muIDMTW = std::make_unique<std::vector<double>>();
  auto muIDIsoMTW = std::make_unique<std::vector<double>>();
  auto muIDTight = std::make_unique<std::vector<bool>>();
  auto muIDIsoTight = std::make_unique<std::vector<bool>>();
  auto elecIDMTW = std::make_unique<std::vector<double>>();
  auto elecIDIsoMTW = std::make_unique<std::vector<double>>();
  auto elecIDMedium = std::make_unique<std::vector<bool>>();
  auto elecIDIsoMedium = std::make_unique<std::vector<bool>>();
  auto elecIDTight = std::make_unique<std::vector<bool>>();
  auto elecIDIsoTight = std::make_unique<std::vector<bool>>();

  edm::Handle< edm::View<pat::MET> > MET;
  iEvent.getByToken(metTok_,MET); 
  reco::MET::LorentzVector metLorentz(0,0,0,0);
  if(MET.isValid() )
    {
      metLorentz=MET->at(0).p4();
    } else std::cout<<"LeptonProducer::MetTag Invalid Tag: "<<metTag_.label()<<std::endl;

  int Leptons=0;
  edm::Handle<pat::PackedCandidateCollection> pfcands;
  iEvent.getByToken(PFCandTok_, pfcands);

  edm::Handle< double > rho_;
  iEvent.getByToken(RhoTok_, rho_); // Central rho recommended for SUSY
  double rho = *rho_;

  edm::Handle<reco::VertexCollection> vtx_h;
  iEvent.getByToken(PrimVtxTok_, vtx_h);
  edm::Handle<edm::View<pat::Muon> > muonHandle;
  iEvent.getByToken(MuonTok_, muonHandle);
  if(muonHandle.isValid())
    {
      for(unsigned int m=0; m<muonHandle->size(); ++m)
        {
          if(muonHandle->at(m).pt()<minMuPt_ || fabs(muonHandle->at(m).eta())>maxMuEta_) continue;
                        
          if(MuonID(muonHandle->at(m),vtx_h->at(0)))
            {
              idMuons->push_back(muonHandle->at(m));
              muIDTight->push_back(MuonIDtight(muonHandle->at(m),vtx_h->at(0)));
              muIDMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),muonHandle->at(m).pt(),muonHandle->at(m).phi()));
              float ChgIso=muonHandle->at(m).pfIsolationR04().sumChargedHadronPt;
              float ChgPU=muonHandle->at(m).pfIsolationR04().sumPUPt;
              float NeuIso=muonHandle->at(m).pfIsolationR04().sumNeutralHadronEt+muonHandle->at(m).pfIsolationR04().sumPhotonEt;
              double dBIsoMu= (ChgIso+std::max(0., NeuIso-0.5*ChgPU))/muonHandle->at(m).pt();
              if(useMiniIsolation_) {
                double mt2_act = 0.0;
                SUSYIsolationHelper.GetMiniIsolation(pfcands, &muonHandle->at(m), SUSYIsolation::muon, rho, dBIsoMu, mt2_act);
              }
              if(dBIsoMu<muIsoValue_)
                {
                  Leptons++;
                  isoMuons->push_back(muonHandle->at(m));
                  muIDIsoTight->push_back(MuonIDtight(muonHandle->at(m),vtx_h->at(0)));
                  muIDIsoMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),muonHandle->at(m).pt(),muonHandle->at(m).phi()));
                  //        std::cout<<"muIDIsoMTW: "<<MTWCalculator(metLorentz.pt(),metLorentz.phi(),muonHandle->at(m).pt(),muonHandle->at(m).phi())<<"\n";
                  MuonCharge->push_back(muonHandle->at(m).charge());
                }
            }
        }
    }


  edm::Handle<edm::View<pat::Electron> > eleHandle;
  iEvent.getByToken(ElecTok_, eleHandle);
  if(eleHandle.isValid())
    {
      for(unsigned int e=0; e<eleHandle->size(); ++e)
        {
          if(fabs(eleHandle->at(e).superCluster()->eta())>maxElecEta_ ||eleHandle->at(e).pt()<minElecPt_)continue;
          const pat::Electron aEle = eleHandle->at(e);
          const reco::Vertex vtx = vtx_h->at(0);

          double miniIso = 0.0;
          double mt2_act = 0.0;
          SUSYIsolationHelper.GetMiniIsolation(pfcands, &aEle, SUSYIsolation::electron, rho, miniIso, mt2_act);

          if(ElectronID(aEle, vtx, VETO)) // check VETO id
            {
              // id passed
              idElectrons->push_back(eleHandle->at(e));
              elecIDMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),eleHandle->at(e).pt(),eleHandle->at(e).phi()));
              elecIDMedium->push_back(ElectronID(aEle, vtx, MEDIUM));
              elecIDTight->push_back(ElectronID(aEle, vtx, TIGHT));
              if(miniIso<elecIsoValue_)
                {
                  // iso passed
                  isoElectrons->push_back(eleHandle->at(e));
                  elecIDIsoMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),eleHandle->at(e).pt(),eleHandle->at(e).phi()));
                  elecIDIsoMedium->push_back(ElectronID(aEle, vtx, MEDIUM));
                  elecIDIsoTight->push_back(ElectronID(aEle, vtx, TIGHT));
                  Leptons++;
                  ElectronCharge->push_back(eleHandle->at(e).charge());
                }
            }
        }
    }

  auto htp = std::make_unique<int>(Leptons);
  iEvent.put(std::move(htp));
  iEvent.put(std::move(idMuons),"IdMuon");
  iEvent.put(std::move(isoMuons),"IdIsoMuon");

  iEvent.put(std::move(idElectrons),"IdElectron");
  iEvent.put(std::move(isoElectrons),"IdIsoElectron");

  iEvent.put(std::move(ElectronCharge),"ElectronCharge");
  iEvent.put(std::move(MuonCharge),"MuonCharge");

  iEvent.put(std::move(muIDMTW),"MuIDMTW");
  iEvent.put(std::move(muIDIsoMTW),"MuIDIsoMTW");
  iEvent.put(std::move(muIDTight),"IdMuonTightID");
  iEvent.put(std::move(muIDIsoTight),"IdIsoMuonTightID");
  iEvent.put(std::move(elecIDMTW),"ElecIDMTW");
  iEvent.put(std::move(elecIDIsoMTW),"ElecIDIsoMTW");
  iEvent.put(std::move(elecIDMedium),"IdElectronMediumID");
  iEvent.put(std::move(elecIDTight),"IdElectronTightID");
  iEvent.put(std::move(elecIDIsoMedium),"IdIsoElectronMediumID");
  iEvent.put(std::move(elecIDIsoTight),"IdIsoElectronTightID");

}

// ------------ method called once each job just before starting event loop  ------------
void
LeptonProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
LeptonProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
LeptonProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
LeptonProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
LeptonProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
LeptonProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
LeptonProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

float LeptonProducer::MTWCalculator(double metPt,double  metPhi,double  lepPt,double  lepPhi)
{
  if(std::isnan(lepPhi) || std::isnan(metPhi)) return 0.;
  float deltaPhi =TVector2::Phi_mpi_pi(lepPhi-metPhi);
  return sqrt(2*lepPt*metPt*(1-cos(deltaPhi)) );
}

bool LeptonProducer::MuonID(const pat::Muon & muon, const reco::Vertex& vtx){
  //medium WP + dz/dxy cuts
  bool goodGlob = muon.isGlobalMuon() && 
                  muon.globalTrack()->normalizedChi2() < 3 && 
                  muon.combinedQuality().chi2LocalPosition < 12 && 
                  muon.combinedQuality().trkKink < 20; 
  bool isMedium = muon.isLooseMuon() && 
                  muon.innerTrack()->validFraction() > 0.8 && 
                  muon.segmentCompatibility() > (goodGlob ? 0.303 : 0.451);
  bool isMediumPlus = isMedium && muon.dB() < 0.2 && fabs(muon.muonBestTrack()->dz(vtx.position())) < 0.5;
  return isMediumPlus; 
}

bool LeptonProducer::MuonIDtight(const pat::Muon & muon, const reco::Vertex& vtx){
  //tight WP
  bool isTight = muon.isGlobalMuon() &&
                 muon.isPFMuon() &&
                 muon.globalTrack()->normalizedChi2() < 10. &&
                 muon.globalTrack()->hitPattern().numberOfValidMuonHits() > 0 &&
                 muon.numberOfMatchedStations() > 1 &&
                 muon.dB() < 0.2 &&
                 fabs(muon.muonBestTrack()->dz(vtx.position())) < 0.5 &&
                 muon.innerTrack()->hitPattern().numberOfValidPixelHits() > 0 &&
                 muon.innerTrack()->hitPattern().trackerLayersWithMeasurement() > 5;

  return isTight;
}

bool LeptonProducer::ElectronID(const pat::Electron & electron, const reco::Vertex & vtx, const elecIDLevel level) {
  // electron ID cuts, updated for Spring15 25ns MC and Run2015C-D data 
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2

  // barrel electrons
  double eb_ieta_cut[4] = {0.0115, 0.011, 0.00998, 0.00998};
  double eb_deta_cut[4] = {0.00749, 0.00477, 0.00311, 0.00308};
  double eb_dphi_cut[4] = {0.228, 0.222, 0.103, 0.0816};
  double eb_hovere_cut[4] = {0.356, 0.298, 0.253, 0.0414};
  double eb_ooeminusoop_cut[4] = {0.299, 0.241, 0.134, 0.0129};
  double eb_d0_cut[4] = {0.05, 0.05, 0.05, 0.05};
  double eb_dz_cut[4] = {0.10, 0.10, 0.10, 0.10};
  int eb_misshits_cut[4] = {2, 1, 1, 1};

  // endcap electrons
  double ee_ieta_cut[4] = {0.037, 0.0314, 0.0298, 0.0292};
  double ee_deta_cut[4] = {0.00895, 0.00868, 0.00609, 0.00605};
  double ee_dphi_cut[4] = {0.213, 0.213, 0.045, 0.0394};
  double ee_hovere_cut[4] = {0.211, 0.101, 0.0878, 0.0641};
  double ee_ooeminusoop_cut[4] = {0.15, 0.14, 0.13, 0.0129};
  double ee_d0_cut[4] = {0.10, 0.10, 0.10, 0.10};
  double ee_dz_cut[4] = {0.20, 0.20, 0.20, 0.20};
  int ee_misshits_cut[4] = {3, 1, 1, 1};

  // common
  bool reqConvVeto[4] = {true, true, true, true};

  double sieie = electron.full5x5_sigmaIetaIeta();
  bool convVeto = electron.passConversionVeto();
  int mhits = electron.gsfTrack()->hitPattern().numberOfLostHits(reco::HitPattern::MISSING_INNER_HITS);;
  double dEtaIn  = electron.deltaEtaSuperClusterTrackAtVtx();
  double dPhiIn  = electron.deltaPhiSuperClusterTrackAtVtx();
  double hoe   = electron.hadronicOverEm();
  double ooemoop = fabs(1.0/electron.ecalEnergy() - electron.eSuperClusterOverP()/electron.ecalEnergy());
  double d0vtx = electron.gsfTrack()->dxy(vtx.position());
  double dzvtx = electron.gsfTrack()->dz(vtx.position());

  if (electron.isEB()) {
    return eb_deta_cut[level] > fabs(dEtaIn)
      && eb_dphi_cut[level] > fabs(dPhiIn)
      && eb_ieta_cut[level] > sieie
      && eb_hovere_cut[level] > hoe
      && eb_d0_cut[level] > fabs(d0vtx)
      && eb_dz_cut[level] > fabs(dzvtx)
      && eb_ooeminusoop_cut[level] > fabs(ooemoop)
      && (!reqConvVeto[level] || convVeto)
      && (eb_misshits_cut[level] >= mhits);
  } else if (electron.isEE()) {
    return ee_deta_cut[level] > fabs(dEtaIn)
      && ee_dphi_cut[level] > fabs(dPhiIn)
      && ee_ieta_cut[level] > sieie
      && ee_hovere_cut[level] > hoe
      && ee_d0_cut[level] > fabs(d0vtx)
      && ee_dz_cut[level] > fabs(dzvtx)
      && ee_ooeminusoop_cut[level] > fabs(ooemoop)
      && (!reqConvVeto[level] || convVeto)
      && (ee_misshits_cut[level] >= mhits);
  } else return false;

}

//define this as a plug-in
DEFINE_FWK_MODULE(LeptonProducer);
