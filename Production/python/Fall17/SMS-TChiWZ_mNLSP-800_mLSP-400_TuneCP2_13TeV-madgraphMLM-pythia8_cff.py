import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/260000/209BBD8C-82EF-EA11-A27B-000101000936.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/260000/24E68BAE-7FEF-EA11-AF9B-0001010008A1.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/260000/800D24A5-8BEF-EA11-B1E4-0001010008FB.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/260000/96B5F202-A6EF-EA11-83D5-A0369F3102B6.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/260000/F26D9480-A4EF-EA11-84FF-0CC47AA989BA.root',
] )
