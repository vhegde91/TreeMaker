import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/2F99B4C5-5F97-1E47-A966-9AB6BC6A5AEB.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/6DD4227C-8577-014E-98FF-85EBEEFB8096.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/6F3113E1-D7C8-834B-841B-84C41A589A9B.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/73C1721A-6EDA-EF47-939F-E8E68983B2F4.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/9111C5AB-F83E-954D-8789-D2E6211B37ED.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/978AAE92-1BA6-F943-8325-D28FE613CBEB.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/99ECA541-517A-1B43-9CF3-1DAE23EF5DB7.root',
] )
