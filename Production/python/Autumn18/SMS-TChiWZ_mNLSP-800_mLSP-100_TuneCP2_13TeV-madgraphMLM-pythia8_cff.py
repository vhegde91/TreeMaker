import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/2DFE4CC5-C4A5-9343-911B-3C54E242DB76.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/44C63C58-FD68-1041-A943-2AE9D2ED1341.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/45C5A3B9-1804-3649-9A69-5D6AAB2D297C.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/C4D70AF7-6FA3-3846-8A28-F4E1BA9C516B.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/C516314F-4309-DB43-9CE2-AE3E5D664627.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/F1855D38-3F60-4242-AAC9-8D837292F5C3.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/F45AE0A4-A924-6E43-9CFF-69EFECF3F9BA.root',
] )
