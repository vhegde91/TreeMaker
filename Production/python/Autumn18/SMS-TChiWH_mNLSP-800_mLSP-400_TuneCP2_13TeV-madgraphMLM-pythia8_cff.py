import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/1B809181-8738-0742-86CE-F313665608DA.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/204F1D16-587F-1E4F-9CC5-6674893EA0AF.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/20F1581A-4661-DC44-9FB8-88688C5E6C5E.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/21C69965-D956-9A41-B056-5E5152E5AF81.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/BE7EF788-59CB-D940-AA4A-BBEA3C26D37B.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/D4051EF2-848C-3E46-96BF-4F78841995A5.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/E0C21E8A-D5B4-A644-A60C-B8DF624B9AC2.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/E7D25443-5C70-804A-81A8-4067B391F20E.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/FF4E9A1C-8FD7-1849-ACE7-4A63E929AC9F.root',
] )
