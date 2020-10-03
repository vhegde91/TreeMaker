import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/047A0F54-5920-E911-99FE-AC1F6B0DE49C.root',
       '/store/mc/RunIISummer16MiniAODv3/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/26B577CB-F91F-E911-A7F6-A0369FD0B1B0.root',
       '/store/mc/RunIISummer16MiniAODv3/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/44320241-9A20-E911-AA4E-48FD8EE739BB.root',
       '/store/mc/RunIISummer16MiniAODv3/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/60C228BC-4C20-E911-9ED2-0090FAA59864.root',
       '/store/mc/RunIISummer16MiniAODv3/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/6A5921A6-4120-E911-AF2B-A0369FE2C084.root',
       '/store/mc/RunIISummer16MiniAODv3/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/6AECC91E-4220-E911-A635-0090FAA58D34.root',
       '/store/mc/RunIISummer16MiniAODv3/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/84FA1247-4420-E911-8C84-AC1F6B0F6758.root',
       '/store/mc/RunIISummer16MiniAODv3/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/E636C87C-3320-E911-AFCA-90B11CBCFF4E.root',
       '/store/mc/RunIISummer16MiniAODv3/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/EE10CBBF-4C20-E911-BB24-A0369FE2C1FC.root',
       '/store/mc/RunIISummer16MiniAODv3/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/F0596208-4520-E911-9DB2-AC1F6B0F6FCE.root',
] )
