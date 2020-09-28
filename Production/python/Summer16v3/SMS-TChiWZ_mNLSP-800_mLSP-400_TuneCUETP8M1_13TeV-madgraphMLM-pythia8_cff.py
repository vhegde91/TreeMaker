import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/12AB48F9-AFF0-EA11-8255-0CC47A57CB8E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/18381A8F-B0F0-EA11-8937-B499BAAC03BA.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/2A941161-B0F0-EA11-881C-CCC5E5EF4F88.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/30C15FF4-AFF0-EA11-8ACF-3417EBE6451F.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/3635EF08-B0F0-EA11-947A-EC0D9A0B3350.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/38CA1FF1-E6F0-EA11-BC96-C4346BC84780.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/3E62AD8D-B0F0-EA11-9DFF-A0369FD0B266.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/40CE6ACB-B5F0-EA11-91C7-A4BF0112BE36.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/42D7D8B0-B1F0-EA11-A89F-BC97E128CED1.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/42F17138-B8F0-EA11-9564-28924A33AFF6.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/4625E589-B1F0-EA11-99FE-0025905A497A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/608CF35A-B0F0-EA11-918B-AC1F6B4E0178.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/6A96ACED-AFF0-EA11-A35F-6C2B598FF837.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/8A4E9CF8-AFF0-EA11-8A09-002590DE39F0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/B8A761ED-AFF0-EA11-8689-0CC47AFF0640.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/C6B760F3-AFF0-EA11-A19D-B49691456296.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/CED085EE-AFF0-EA11-9A3A-0242AC1C0509.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/E2D728F4-AFF0-EA11-BE33-509A4C748114.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/EC8ECECD-B0F0-EA11-91E4-F4E9D4AF7E20.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/F69D4043-B0F0-EA11-B4F8-C4346BC76CD8.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/FEE996A2-B0F0-EA11-8F6A-141877412793.root',
] )
