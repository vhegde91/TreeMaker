import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    '/store/user/hatake/SUSYEWK/TChiWZ/TChiWZ_800_100/SUS-RunIIAutumn18MiniAOD-99999-800_100.root',
] )

