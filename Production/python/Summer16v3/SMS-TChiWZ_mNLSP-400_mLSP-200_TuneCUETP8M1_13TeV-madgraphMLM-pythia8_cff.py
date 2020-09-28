import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/067112E0-03F1-EA11-8999-A0369FD0B286.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/08A4374A-03F1-EA11-ACB8-F0D4E2E523AC.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/0C35E124-03F1-EA11-B655-A4BF01125558.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/0E0F9F12-03F1-EA11-8FF0-484D7E8DF051.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/4CDF38CE-03F1-EA11-9961-A0369FF883FA.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/4CF8B4E3-03F1-EA11-821A-001E67E5EDBB.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/50FF7191-15F1-EA11-9018-FA163EA528C2.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/545FB5D8-03F1-EA11-BB16-20000109FE80.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/589603B8-04F1-EA11-BCB4-509A4C83EF3E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/6E4A5D68-03F1-EA11-958E-0425C5DE7BF0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/8658C552-03F1-EA11-81D7-0CC47A0AD6FE.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/9EA4ECDF-03F1-EA11-BF9E-008CFAC93EB0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/A66A2A6B-03F1-EA11-B766-0026B9278644.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/AADE315A-03F1-EA11-A56B-001E67A3EC00.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/B2331718-03F1-EA11-9329-6C2B59900458.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/BAA5F720-04F1-EA11-B992-2047478D3CC8.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/D0F32166-03F1-EA11-875A-047D7B10618E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/D8C4D722-03F1-EA11-9C56-0CC47AFF0300.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/EE92E8D3-02F1-EA11-8747-0CC47A7EEE32.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/F2AC60E2-03F1-EA11-9ECE-0242AC1C0539.root',
] )
