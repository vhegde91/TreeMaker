import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/90000/04DF2F78-CE1F-E911-9B8D-B496912ED94C.root',
       '/store/mc/RunIISummer16MiniAODv3/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/90000/2E40D7DA-D41F-E911-840F-44A842B2D631.root',
       '/store/mc/RunIISummer16MiniAODv3/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/90000/345D0F72-1E20-E911-8B3E-A0369FD206F8.root',
       '/store/mc/RunIISummer16MiniAODv3/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/90000/347EF0DF-CC1F-E911-8AB9-3417EBE52468.root',
       '/store/mc/RunIISummer16MiniAODv3/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/90000/6653804B-0120-E911-890B-B496912ED94C.root',
       '/store/mc/RunIISummer16MiniAODv3/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/90000/984101C6-CC1F-E911-A140-B496912ED620.root',
       '/store/mc/RunIISummer16MiniAODv3/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/90000/CECC7DE7-CC1F-E911-AE57-A0369FD206F8.root',
       '/store/mc/RunIISummer16MiniAODv3/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/90000/DEB34EE3-CC1F-E911-B988-3417EBE52930.root',
] )
