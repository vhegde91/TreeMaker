import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/260000/00DA90DD-206A-E911-BFA9-A4BF0112BD6A.root',
       '/store/mc/RunIISummer16MiniAODv3/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/260000/0A14D7B5-226A-E911-B10E-A4BF011255D0.root',
       '/store/mc/RunIISummer16MiniAODv3/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/260000/12DFDEB7-226A-E911-92BE-A4BF01158888.root',
       '/store/mc/RunIISummer16MiniAODv3/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/260000/1CE32BF5-346A-E911-A87B-A4BF0112BD2C.root',
       '/store/mc/RunIISummer16MiniAODv3/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/260000/224474B2-226A-E911-8304-A4BF0112E490.root',
       '/store/mc/RunIISummer16MiniAODv3/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/260000/32708ADD-226A-E911-92E2-A4BF0112DD7C.root',
       '/store/mc/RunIISummer16MiniAODv3/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/260000/4E67CF0E-266A-E911-AF91-001E677926B6.root',
       '/store/mc/RunIISummer16MiniAODv3/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/260000/5ACCEA41-166A-E911-BD4A-A4BF0112BD0E.root',
       '/store/mc/RunIISummer16MiniAODv3/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/260000/6CE85839-1E6A-E911-9A76-A4BF0112BDB6.root',
       '/store/mc/RunIISummer16MiniAODv3/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/260000/8474B477-216A-E911-85DD-A4BF01125BA0.root',
       '/store/mc/RunIISummer16MiniAODv3/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/260000/86AC7BFD-216A-E911-BFC2-001E677928D6.root',
       '/store/mc/RunIISummer16MiniAODv3/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/260000/9838AEBD-226A-E911-92D3-A4BF01125AB8.root',
       '/store/mc/RunIISummer16MiniAODv3/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/260000/9C83CF0F-1A6A-E911-B695-A4BF01125A48.root',
       '/store/mc/RunIISummer16MiniAODv3/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/260000/DA66317B-216A-E911-A8F0-A4BF0115A150.root',
       '/store/mc/RunIISummer16MiniAODv3/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/260000/E86B0496-2F6A-E911-8BDA-A4BF0112BDA8.root',
       '/store/mc/RunIISummer16MiniAODv3/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/260000/F68B1D55-1F6A-E911-BB19-A4BF0112BD12.root',
       '/store/mc/RunIISummer16MiniAODv3/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/260000/FA42FB70-1F6A-E911-971A-A4BF011257C0.root',
] )
