import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/046BFAE8-07FA-EA11-A83B-0025907E35AA.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/140AB600-12FA-EA11-84A3-20CF305B060E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/16371A01-0BFA-EA11-9F19-008CFA1980B8.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/1EEDCFA1-32FA-EA11-812A-B02628DEA060.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/2A48A9B6-0AFA-EA11-8E62-FA163E5C3BC5.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/40D19B0E-2BFA-EA11-BB96-AC1F6BAC7C20.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/40D38A7E-06FA-EA11-B0C7-B083FED0FFCF.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/48EAC029-06FA-EA11-903B-E0071B7A16F0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/4EF95763-BFFB-EA11-8C2B-68CC6EA5BE22.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/5AD62501-03FA-EA11-B075-0CC47AFF0188.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/68EAA0EB-02FA-EA11-AB62-B4969121E614.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/8C5EE979-48FA-EA11-98F2-44A84224BE51.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/C871A8D7-04FA-EA11-A73E-6C2B597CFA0D.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/DE3DF9A2-01FA-EA11-859E-44A842CFD5D8.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/ECA92F30-0FFA-EA11-BDD3-0CC47A5FA215.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/F667F28A-06FA-EA11-BDDB-0026B92785E9.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/F82B41CC-5DFC-EA11-90B5-A0369F6369D2.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/FC8E81F1-01FA-EA11-853B-22C6F260B0C8.root',
] )
