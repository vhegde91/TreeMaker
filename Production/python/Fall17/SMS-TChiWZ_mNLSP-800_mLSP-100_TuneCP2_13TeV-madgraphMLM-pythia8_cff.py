import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/260000/10EB4402-6EEF-EA11-B43D-00010100093A.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/260000/6449F0F5-85EF-EA11-B4FF-0001010008AE.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/260000/BC1D2683-96EF-EA11-AC26-000101000890.root',
] )
