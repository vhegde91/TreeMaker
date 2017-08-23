import FWCore.ParameterSet.Config as cms

TreeMaker = cms.EDProducer(
'TreeMaker',
# Name of the output tree
TreeName          = cms.string('RA2Tree'),
## might help if something isn't working, will produce couts
debug = cms.bool(False),
#default: output RecoCands as vector<TLorentzVector>
#switches to vector<double> pt, eta, phi, energy if false
doLorentz = cms.bool(True),
#branches are sorted alphabetically by default
sortBranches = cms.bool(True),
# list of reco candidate objects: for each reco cand collection, the TLorentzVector will be stored in a vector.
VarsBool = cms.vstring(),
VarsInt = cms.vstring(),
VarsFloat = cms.vstring(),
VarsString = cms.vstring(),
VarsTLorentzVector = cms.vstring(),
VectorBool = cms.vstring(),
VectorInt = cms.vstring(),
VectorFloat = cms.vstring(),
VectorString = cms.vstring(),
VectorTLorentzVector = cms.vstring(),
VectorRecoCand = cms.vstring(),
)
