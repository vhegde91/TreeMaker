import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/12F4144A-FDFB-EA11-B206-AC1F6BD5A08A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/52E3530E-FDFB-EA11-837D-0001010008A0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/6A7DA3D6-25FA-EA11-96B7-F4E9D4AEC940.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/6E5F03C5-5DFC-EA11-8302-3417EBE465FE.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/726CB7E4-25FA-EA11-9306-B4969121E614.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/88AB26DF-25FA-EA11-8E5F-BC305B390AB4.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/90BD7626-29FA-EA11-9165-008CFA1C645C.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/BEB848E9-83FA-EA11-B6C2-0CC47A5FBE25.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/C05A1E1C-23FA-EA11-9186-A0369FE2C16A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/D486F695-27FA-EA11-9DFF-141877640173.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/E28AEEE2-25FA-EA11-9F9D-B499BAAC0A22.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/E422CBD7-46FA-EA11-A2B0-FA163EC44481.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/E86D2DA8-24FA-EA11-ABA1-B02628344400.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/F8A02967-26FA-EA11-A98B-001E6739665D.root',
] )
