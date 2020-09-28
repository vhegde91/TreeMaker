import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/280000/34FBDE83-91EF-EA11-A86D-A4BF01159734.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/280000/36E64D89-1BF0-EA11-9F01-6C3BE5B5A088.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/280000/3A06718B-91EF-EA11-A816-509A4C728881.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/280000/3A6B8694-90EF-EA11-926A-1C34DA7C673A.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/280000/4678B7D7-D0EF-EA11-A91D-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/280000/4CADD145-90EF-EA11-A987-0001010008CB.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/280000/70592E3E-57EF-EA11-9EDB-00010100091B.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/280000/768574A3-92EF-EA11-8913-5254007EEA90.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/280000/7AAC1EA7-91EF-EA11-8165-6CC2173C3DD0.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/280000/7C5AA643-F4EF-EA11-B0D9-0CC47AFB81B4.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/280000/A86E5279-91EF-EA11-AE97-90B11C2801E1.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/280000/AE3F7589-91EF-EA11-BCC8-AC1F6BAC7EAE.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/280000/F2BFE568-91EF-EA11-A7AA-008CFAC93E68.root',
] )
