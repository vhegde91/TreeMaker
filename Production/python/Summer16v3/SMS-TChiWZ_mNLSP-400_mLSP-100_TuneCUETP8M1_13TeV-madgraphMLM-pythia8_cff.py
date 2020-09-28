import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/0E74EFE4-7BF0-EA11-8ED7-FA163EFC23D1.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/1E2025E9-7BF0-EA11-A20B-6C2B597D1BF0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/2EC4A2E4-7BF0-EA11-A1B6-F4E9D4A351B0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/329774E6-7BF0-EA11-8EBC-B083FED138B3.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/36D66CE7-7BF0-EA11-9C2A-A0369FC5B7E0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/3EEFA7EA-7BF0-EA11-8569-001E67DFF6E0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/507859F8-7BF0-EA11-999C-B02628DEB980.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/62C1DAFD-7BF0-EA11-9EEF-AC1F6BAC7C20.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/6AC778F7-7BF0-EA11-9614-D4AE526A1687.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/729FE1F9-7BF0-EA11-A507-A0369FE2C170.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/80360BF4-7BF0-EA11-84E7-0025905C2CA4.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/A8014AF9-7BF0-EA11-A3F2-A4BF0112BE36.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/ACC9A52F-7DF0-EA11-8893-1CB72C1B6CCA.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/BAD5E1F3-7BF0-EA11-8279-0CC47A57CB8E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/C623D8DF-7BF0-EA11-86B5-AC1F6BD59A32.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/EC2788D7-7CF0-EA11-AD44-44A842CFC97E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/F2D08AE5-7BF0-EA11-B17C-F4E9D497BBE0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/FED0BBF8-7BF0-EA11-A5E3-0242AC1C0501.root',
] )
