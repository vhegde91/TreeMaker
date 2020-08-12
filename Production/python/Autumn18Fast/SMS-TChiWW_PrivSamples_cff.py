import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/akanugan/TChipmWW/MINIAOD/SUS-RunIIAutumn18MiniAOD-99997-600_100.root',
       '/store/user/akanugan/TChipmWW/MINIAOD/SUS-RunIIAutumn18MiniAOD-99997-800_100.root',
       '/store/user/akanugan/TChipmWW/MINIAOD/SUS-RunIIAutumn18MiniAOD-99997-1000_100.root',
] )
