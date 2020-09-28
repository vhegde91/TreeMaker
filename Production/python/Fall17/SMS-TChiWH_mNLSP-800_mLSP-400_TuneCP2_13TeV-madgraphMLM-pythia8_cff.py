import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/120385A5-1AF0-EA11-94CD-A0369FD0B1C2.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/1283C4FD-2AF0-EA11-A347-008CFA152144.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/2E889666-29F0-EA11-87B6-000101000918.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/363949F4-2AF0-EA11-8A16-CCC5E5F02BEE.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/8A29EDED-2AF0-EA11-A7AC-20040FE9BCD4.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/D27790F0-2AF0-EA11-BA3A-AC1F6BABF8E3.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/D89CFEFC-2AF0-EA11-A5F1-0CC47AFCC4BE.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/DE7E9E01-2BF0-EA11-BF86-A0369FD0B192.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/E6CBD2FF-2AF0-EA11-B1C1-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/EEF998EF-2AF0-EA11-AA46-0CC47AD98F70.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/F4E110EF-01F0-EA11-BF17-E0071B7A36C0.root',
] )
