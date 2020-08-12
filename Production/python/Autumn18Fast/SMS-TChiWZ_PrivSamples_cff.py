import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-300_1.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-400_1.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-500_1.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-600_1.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-600_100.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-600_200.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-600_300.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-600_400.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-600_500.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-700_1.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-700_100.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-800_1.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-800_100_v2.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-800_200.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-800_300.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-800_400.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-800_500.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-800_600.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-800_700.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-900_1.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-900_100.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-1000_1.root',
       '/store/user/akanugan/TChiWZ/MINIAOD/SUS-RunIIAutumn18MiniAOD-99999-1000_100_v2.root',
] )
