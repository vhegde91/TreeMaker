import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/43E35442-F7D8-3A43-A259-B2D6572E2902.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/4776B409-0CDB-F64F-9F50-269DC1AFD4B7.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/483F4127-B99B-804E-BCE4-5BF696A6ED98.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/512A3E88-81EC-EE4B-92A6-331415DD84EC.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/551BD879-8D34-7746-BBC1-7507F5D0D8B0.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/56EBD822-2B3E-FE44-AE02-8BD57CE7DA78.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/8DEB4315-A850-F54B-BF09-8BFE8EE8B44D.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/992754B3-065F-7641-9348-2F1F1172557E.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/9B1C9666-AB93-6247-8D2E-051061043879.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/B7AD8207-85E2-D64A-BF4E-C8A11B14A78C.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/C6FA6E65-4541-D34B-95BE-9251695281B8.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/D9DD3179-9D04-744A-B035-65882D3D1BD3.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/DA671AE3-2ED2-DD4F-A5CC-61695F95A5E8.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/DCFC6CD0-189E-B740-A044-528F61DE5E07.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/E99E76D5-EF43-3C4B-A887-145183E7077C.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/EB0F7006-33A1-DE48-8003-433E596ACFAD.root',
] )
