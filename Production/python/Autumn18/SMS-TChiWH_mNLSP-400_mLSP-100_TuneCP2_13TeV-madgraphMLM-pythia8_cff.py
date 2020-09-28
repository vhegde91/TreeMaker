import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/1520A4C9-41A4-B044-84BE-C46811119F55.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/2C88030C-D5A8-0B4D-A2BC-75D7664F4137.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/37C6B4F2-C827-0541-85EA-FEE25CB18F92.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/489F9DA1-FDED-0041-A7CF-BD354F99704B.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/531CCF1F-1BDC-EF46-AEFA-A7D4D5D706C7.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/54CC6D09-9397-2446-8131-6C677C15C55F.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/5A422C35-4214-8745-AEC6-DEE0D4C2CE50.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/8E449A9C-E2C6-844A-9491-6FEB69C40B3D.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/96C16DC7-5435-3847-9CFA-5A5287AA2877.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/CE191456-A10F-BA47-96B2-628E8CA93128.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/D2E7676E-0941-994A-B247-818A27BD1199.root',
] )
