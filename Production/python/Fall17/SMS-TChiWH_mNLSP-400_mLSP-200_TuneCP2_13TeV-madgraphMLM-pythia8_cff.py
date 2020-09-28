import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/3A9CFAC6-F4EF-EA11-81F5-0CC47AD98BEE.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/764848B4-F4EF-EA11-9965-20040FE8ECAC.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/9E84B2DB-CCEF-EA11-8603-000101000896.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/B00EE0B2-F4EF-EA11-8C01-FA163ED7ECAE.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/B43289CD-F4EF-EA11-83F2-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/B48955CB-64F0-EA11-AA27-001E67DFFF5F.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/F458346E-F2EF-EA11-A138-000101000954.root',
] )
