import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/06315BD8-B2F0-EA11-927E-FA163E66615C.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/248C2F6C-9AF0-EA11-81F2-0CC47AFCC69E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/52DABEAC-99F0-EA11-BEE5-E0071B88B988.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/62FD64D4-98F0-EA11-915D-008CFAF5592A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/64E4C7CE-98F0-EA11-8203-1866DAEA6CC4.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/68CFF5CA-98F0-EA11-BA61-A4BF01125AB8.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/6C829DCB-98F0-EA11-92B3-A0369FE2C14A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/6CA6B8B3-99F0-EA11-861E-002590791D60.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/7E2CF6CF-98F0-EA11-B447-0242AC1C0515.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/7ED84CE5-99F0-EA11-AAD1-B02628DEB7E0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/927CA3DC-98F0-EA11-A1A8-0CC47A7EEE80.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/A4484EC2-98F0-EA11-9A70-008CFAC93BE0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/A6BA2D79-D9F0-EA11-9728-9CDC715F8720.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/B401D704-9BF0-EA11-9846-0025905A6070.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/C07333D2-98F0-EA11-89F1-0CC47AFC3C64.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/C21D45D8-98F0-EA11-9E87-B02628E2A770.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/CE2D0B0D-E6F0-EA11-9D50-C4346BC84780.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/D066013F-9CF0-EA11-BBA2-001E67DDBEDA.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/FC36D6D0-98F0-EA11-B836-B496910A8648.root',
] )
