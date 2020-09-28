import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/1258A4A8-B7EF-EA11-8AF3-0001010008A1.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/2E7BCC53-BEEF-EA11-BF31-5065F37D60D2.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/5A4FEF41-BCEF-EA11-8111-0001010008D1.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/640F9485-AFEF-EA11-992E-00010100093A.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/D608B684-BEEF-EA11-A7F5-FA163EB92B8A.root',
] )
