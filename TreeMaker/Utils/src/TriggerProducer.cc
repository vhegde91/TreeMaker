// -*- C++ -*-
//
// Package:    TriggerProducer
// Class:      TriggerProducer
// 
/**\class TriggerProducer TriggerProducer.cc RA2Classic/TriggerProducer/src/TriggerProducer.cc
 */
//
// Original Author:  Sam Bein,
//         Created:  Wednesday June 24 2015
// system include files
#include <memory>
#include <algorithm>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include <DataFormats/Math/interface/deltaR.h>
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"

#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "TLorentzVector.h"
//
// class declaration
//

class TriggerProducer : public edm::EDProducer {
public:
  explicit TriggerProducer(const edm::ParameterSet&);
  ~TriggerProducer();
	
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
	
  virtual void beginRun(edm::Run&, edm::EventSetup const&);
  virtual void endRun(edm::Run&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  
  void GetInputTag(edm::InputTag& tag, std::string arg1, std::string arg2, std::string arg3, std::string arg1_default);
  edm::InputTag trigResultsTag_, trigPrescalesTag_;
  edm::EDGetTokenT<edm::TriggerResults> trigResultsTok_;
  edm::EDGetTokenT<pat::PackedTriggerPrescales> trigPrescalesTok_;
  std::vector<std::string> parsedTrigNamesVec;

  edm::EDGetTokenT<edm::TriggerResults> trigResultsToken;
  edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> trigObjCollToken;

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
TriggerProducer::TriggerProducer(const edm::ParameterSet& iConfig)
{
  parsedTrigNamesVec = iConfig.getParameter <std::vector<std::string> > ("triggerNameList");
  //sort the trigger names
  std::sort(parsedTrigNamesVec.begin(), parsedTrigNamesVec.end());
  //print triggers
  std::cout << "List of stored triggers:" << std::endl;
  for(unsigned t = 0; t < parsedTrigNamesVec.size(); ++t){
    std::cout << t << ": " << parsedTrigNamesVec[t] << std::endl;
  }
  
  GetInputTag(trigResultsTag_,
              iConfig.getParameter <std::string> ("trigTagArg1"),
              iConfig.getParameter <std::string> ("trigTagArg2"),
              iConfig.getParameter <std::string> ("trigTagArg3"),
              "TriggerResults");

  GetInputTag(trigPrescalesTag_,
              iConfig.getParameter <std::string> ("prescaleTagArg1"),
              iConfig.getParameter <std::string> ("prescaleTagArg2"),
              iConfig.getParameter <std::string> ("prescaleTagArg3"),
              "patTrigger");

  trigResultsTok_ = consumes<edm::TriggerResults>(trigResultsTag_);
  trigPrescalesTok_ = consumes<pat::PackedTriggerPrescales>(trigPrescalesTag_);

  edm::InputTag theTriggerLabel("TriggerResults", "", "HLT");
  edm::InputTag theTrigObjLabel("selectedPatTrigger");
  trigResultsToken = consumes<edm::TriggerResults>(theTriggerLabel);
  trigObjCollToken = consumes<pat::TriggerObjectStandAloneCollection>(theTrigObjLabel);

  produces<std::vector<std::string> >("TriggerNames");
  produces<std::vector<int> >("TriggerPass");
  produces<std::vector<int> >("TriggerPrescales");
  produces<std::vector<TLorentzVector> >("HLTElectronObjects");
  produces<std::vector<TLorentzVector> >("L1EGObjects");
}


TriggerProducer::~TriggerProducer()
{}

//
// member functions
//

// ------------ helper function to make InputTags ------------
void
TriggerProducer::GetInputTag(edm::InputTag& tag, std::string arg1, std::string arg2, std::string arg3, std::string arg1_default=""){
  // We we make the producer a little smarter. There are four cases we look at
  // 1) arg1 and arg3 are set, if this is the case we create the label bases on all three arguments
  // 2) arg3 is not set, in this case we create the label based only on arg1
  // 3) Neither arg1 nor arg3 are set, in this case we default to searching for arg1_default
  // 4) arg1 is not set, but arg3 is set, we look for arg1_default in the process defined by arg3

  if(arg1.empty()) arg1 = arg1_default;
  
  if(arg3.empty()){
    tag = edm::InputTag(arg1);
  } else {
    tag = edm::InputTag(arg1,arg2,arg3);
  }	
}

// ------------ method called to produce the data  ------------
void
TriggerProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace std;
  auto passTrigVec = std::make_unique<std::vector<int>>(parsedTrigNamesVec.size(),-1);
  auto trigPrescaleVec = std::make_unique<std::vector<int>>(parsedTrigNamesVec.size(),1);
  auto trigNamesVec = std::make_unique<std::vector<std::string>>(parsedTrigNamesVec.size(),"");
  auto hltEleObj = std::make_unique<std::vector<TLorentzVector>>();
  auto l1EGObj = std::make_unique<std::vector<TLorentzVector>>();

  //int passesTrigger;
  edm::Handle<edm::TriggerResults> trigResults; //our trigger result object
  iEvent.getByToken(trigResultsTok_,trigResults);
  const edm::TriggerNames& trigNames = iEvent.triggerNames(*trigResults);
  edm::Handle<pat::PackedTriggerPrescales> trigPrescales;
  iEvent.getByToken(trigPrescalesTok_,trigPrescales);

  //Find the matching triggers
  std::string testTriggerName;
  for(unsigned int parsedIndex = 0; parsedIndex < parsedTrigNamesVec.size(); parsedIndex++){
    trigNamesVec->at(parsedIndex) = parsedTrigNamesVec[parsedIndex];
    for(unsigned int trigIndex = 0; trigIndex < trigNames.size(); trigIndex++){
      testTriggerName = trigNames.triggerName(trigIndex);
      if(testTriggerName.find(parsedTrigNamesVec.at(parsedIndex)) != std::string::npos){
        trigNamesVec->at(parsedIndex) = testTriggerName;
        passTrigVec->at(parsedIndex) = trigResults->accept(trigIndex);
        trigPrescaleVec->at(parsedIndex) = trigPrescales->getPrescaleForIndex(trigIndex);
        //std::cout << "Matched: " << testTriggerName << std::endl;
        break; //We only match one trigger to each trigger name fragment passed
      }
    }
  }

  edm::Handle<edm::TriggerResults> triggerBits;
  iEvent.getByToken(trigResultsToken,triggerBits);

  const edm::TriggerNames& names = iEvent.triggerNames(*triggerBits);
  //for (unsigned int i = 0, n = triggerBits->size(); i < n; ++i) {                                                                  
  //  cout << "Trigger " << names.triggerName(i) <<                                                                                  
  //              ": " << (triggerBits->accept(i) ? "PASS" : "fail (or not run)")                                                    
  //              << endl;                                                                                                           
  //  }                                                                                                                              

  edm::Handle<pat::TriggerObjectStandAloneCollection> triggerObjects;
  iEvent.getByToken(trigObjCollToken,triggerObjects);
  //save the trigger object corresponding to the trigger HLT_Ele27_WPTight_Gsf_v*. Obtained code from https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2016#Trigger
  bool saveL1Obj = false;
  // loop over selected trigger objects                                                                                              
  for (pat::TriggerObjectStandAlone obj : *triggerObjects) {
    obj.unpackPathNames(names);
    TLorentzVector objVec(obj.px(),obj.py(),obj.pz(),obj.energy());
    bool saveObj = false;
    if(obj.pt() < 10.0) continue;
    //    std::cout << "\tTrigger object:  pt " << obj.pt() << ", eta " << obj.eta() << ", phi " << obj.phi() << std::endl;
    // Print trigger object collection and type
    // std::cout << "\t   Collection: " << obj.collection() << std::endl;
    // std::cout << "\t   Type IDs:   ";
    //    for (unsigned h = 0; h < obj.filterIds().size(); ++h) std::cout << " " << obj.filterIds()[h] ;
    // Print associated trigger filters
    // std::cout << "\t   Filters:    ";
    // for (unsigned h = 0; h < obj.filterLabels().size(); ++h) std::cout << " " << obj.filterLabels()[h];
    // std::cout << std::endl;
    std::vector<std::string> pathNamesAll = obj.pathNames(false);
    std::vector<std::string> pathNamesLast = obj.pathNames(true);
    // Print all trigger paths, for each one record also if the object is associated to a 'l3' filter (always true for the
    // definition used in the PAT trigger producer) and if it's associated to the last filter of a successfull path (which
    // means that this object did cause this trigger to succeed; however, it doesn't work on some multi-object triggers)
    //    std::cout << "\t   Paths (" << pathNamesAll.size()<<"/"<<pathNamesLast.size()<<"):    ";
    for (unsigned h = 0, n = pathNamesAll.size(); h < n; ++h) {
      bool isBoth = obj.hasPathName( pathNamesAll[h], true, true );//object is associated wih l3 filter and associated to the last filter of a successfull path. this object caused the trigger to fire.
      string path_i = pathNamesAll[h];
      path_i.pop_back(); path_i.pop_back(); //remove last 2 characters from path name.
      if( isBoth && ( (path_i == "HLT_Ele27_WPTight_Gsf_v") || (path_i == "HLT_Ele27_WPTight_Gsf_") ) ){ //check if the trigger path name is "HLT_Ele27_WPTight_Gsf_vX" or "HLT_Ele27_WPTight_Gsf_vXX"
	//	cout<<" We found path "<<path_i<<". Path name in MiniAOD: "<<pathNamesAll[h]<<endl; 
	saveObj = true;	//save this trigger object
	saveL1Obj = true;//will save all L1 objects for thsis events if Ele27_WPTight has fired.
	break;
      }
      //      std::cout << "   " << pathNamesAll[h];
      //      if (isBoth) std::cout << "(L,3)";
    }
    if(saveObj){
      hltEleObj->push_back(objVec);//save the trigger object corresponding to HLT_Ele27_WPTight_Gsf_v* trigger.
    }
    //    cout<<endl;
  }
  for (pat::TriggerObjectStandAlone obj : *triggerObjects) {
    obj.unpackPathNames(names);
    TLorentzVector objVec(obj.px(),obj.py(),obj.pz(),obj.energy());
    if( saveL1Obj && (obj.hasTriggerObjectType(trigger::TriggerL1EG)) ) l1EGObj->push_back(objVec);//save L1 objects if HLT_Ele27_WPTight_Gsf trigger fired.
  }

  iEvent.put(std::move(passTrigVec),"TriggerPass");
  iEvent.put(std::move(trigPrescaleVec),"TriggerPrescales");
  iEvent.put(std::move(trigNamesVec),"TriggerNames");
  iEvent.put(std::move(hltEleObj),"HLTElectronObjects");
  iEvent.put(std::move(l1EGObj),"L1EGObjects");
}


// ------------ method called once each job just before starting event loop  ------------
void 
TriggerProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TriggerProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
TriggerProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
TriggerProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
TriggerProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
TriggerProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TriggerProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TriggerProducer);
