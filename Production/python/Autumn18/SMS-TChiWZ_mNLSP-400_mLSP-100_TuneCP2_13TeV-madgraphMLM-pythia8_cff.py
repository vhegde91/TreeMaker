import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/1BD701F2-D621-DB4A-8E06-8AFB94881E84.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/602FB9AB-925C-E64F-98DC-C74E860523A9.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/82255DFF-6A68-3E4D-BFA2-0B55D2D5F615.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/DBC724BD-903B-E744-80E0-0999481B5DAE.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/E9114093-AF37-604D-8CB3-AFCB835D1732.root',
] )
