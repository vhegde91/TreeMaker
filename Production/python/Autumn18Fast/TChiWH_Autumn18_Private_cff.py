import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/akanugan/TChiWH/MINIAOD/SUS-RunIIAutumn18MiniAOD-99998-300_1.root',
       '/store/user/akanugan/TChiWH/MINIAOD/SUS-RunIIAutumn18MiniAOD-99998-400_1.root',
       '/store/user/akanugan/TChiWH/MINIAOD/SUS-RunIIAutumn18MiniAOD-99998-500_1.root',
       '/store/user/akanugan/TChiWH/MINIAOD/SUS-RunIIAutumn18MiniAOD-99998-500_100.root',
       '/store/user/akanugan/TChiWH/MINIAOD/SUS-RunIIAutumn18MiniAOD-99998-500_200.root',
       '/store/user/akanugan/TChiWH/MINIAOD/SUS-RunIIAutumn18MiniAOD-99998-500_300.root',
       '/store/user/akanugan/TChiWH/MINIAOD/SUS-RunIIAutumn18MiniAOD-99998-600_1.root',
       '/store/user/akanugan/TChiWH/MINIAOD/SUS-RunIIAutumn18MiniAOD-99998-600_200.root',
       '/store/user/akanugan/TChiWH/MINIAOD/SUS-RunIIAutumn18MiniAOD-99998-600_300.root',
       '/store/user/akanugan/TChiWH/MINIAOD/SUS-RunIIAutumn18MiniAOD-99998-600_400.root',
       '/store/user/akanugan/TChiWH/MINIAOD/SUS-RunIIAutumn18MiniAOD-99998-800_1.root',
       '/store/user/akanugan/TChiWH/MINIAOD/SUS-RunIIAutumn18MiniAOD-99998-800_200.root',
       '/store/user/akanugan/TChiWH/MINIAOD/SUS-RunIIAutumn18MiniAOD-99998-800_300.root',
       '/store/user/akanugan/TChiWH/MINIAOD/SUS-RunIIAutumn18MiniAOD-99998-800_400.root',
       '/store/user/akanugan/TChiWH/MINIAOD/SUS-RunIIAutumn18MiniAOD-99998-800_500.root',
       '/store/user/akanugan/TChiWH/MINIAOD/SUS-RunIIAutumn18MiniAOD-99998-800_600.root',
] )
