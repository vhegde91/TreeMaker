import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/3E32FF92-A3EF-EA11-8B54-0001010008A3.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/46C45BDF-A6EF-EA11-8281-00010100092C.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/B43E8B1D-0AF0-EA11-AB4C-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/B6D0B813-BCEF-EA11-8B0E-000101000936.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/BE187029-08F0-EA11-BD01-000101000977.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/DEC612C0-05F0-EA11-B331-E0071B7A7650.root',
] )
