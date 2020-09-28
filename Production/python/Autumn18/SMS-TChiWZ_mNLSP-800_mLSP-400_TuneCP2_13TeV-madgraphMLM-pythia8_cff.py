import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/01A38B0C-AC30-2643-8F8C-00B54800F9B3.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/74D7533C-57FD-4A4A-902F-F41549BF492B.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/A49CFB39-614C-3945-8C8A-BECFCB573BCC.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/B288E47F-BEDA-D04B-8278-422ED16271BB.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/B511CFAD-4C1C-814D-8F01-5EC348EF9459.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/E73C7AAF-768E-8D45-8EB4-6CCFE8A8F7BE.root',
] )
