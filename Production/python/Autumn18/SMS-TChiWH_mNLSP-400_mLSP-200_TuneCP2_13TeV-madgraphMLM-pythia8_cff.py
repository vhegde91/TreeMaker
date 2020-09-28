import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/05A95395-3401-2840-95E1-B50C49195680.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/1E3D9401-EDDA-D549-9D16-9F25936D40E6.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/266480F3-144B-154E-83D2-5748E6F424D1.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/2B949A3E-EE6B-354F-9B62-43E7205F46F4.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/59B57DA2-4E86-0540-95BA-694E6C573768.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/66A3DBB7-7A01-674D-B8C7-CD49A46E7EF6.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/88BE9B3F-024C-414E-BBC7-45CBB907E269.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/98AAD468-6BD7-7F40-A54B-3AE74441DE26.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/B23A42E3-EC12-D740-AC12-FB8940F1E8AA.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/E3AA2540-3B9B-224F-B8AB-B6CBDCCA181E.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/E6F36AF1-5907-0C40-B9FF-CDDA62A78360.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/F7ABD170-4172-9948-8AA8-D0554B24AD9D.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/FD3CA828-0C84-D647-A552-DED590D81706.root',
] )
