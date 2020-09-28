import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/020B3AD0-C7F7-EA11-87D4-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/0C405B43-B8F7-EA11-B043-0CC47A00A832.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/326F15A0-BAF7-EA11-8C4D-6CC21739C400.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/3EE014CA-B9F7-EA11-9042-0CC47AF9B13A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/44AC4808-C1F7-EA11-8B0B-A0369FF882E0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/44D882B6-C5F7-EA11-BF23-FA163E312F44.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/46BCE9E0-B7F7-EA11-86B8-20040FE9AD78.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/52315F59-86FB-EA11-9AF4-0CC47A7452DA.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/744C4A4F-86FB-EA11-BF18-1CB72C1B2D84.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/762D5111-C5F7-EA11-B9E8-0026B92779F1.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/886C9E8F-BCF7-EA11-B065-1C34DA758B02.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/88FA2AD9-B7F7-EA11-AC33-5065F37D9082.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/AC5FD3FC-BCF7-EA11-9F89-008CFAE451AC.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/AEFED0F2-BEF7-EA11-91B0-AC1F6BABF8D1.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/B62B0649-B8F7-EA11-9774-E0DB55FC1055.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/C61B0513-C2F7-EA11-903F-20CF3027A62B.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/C677F12F-C1F7-EA11-B098-003048CBA4EC.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/E8793442-C0F7-EA11-B33F-549F351F915E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/F21B2CCF-BCF7-EA11-8495-B02628342C70.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/250000/F683A4E5-B7F7-EA11-86F8-001E67DFF61D.root',
] )
