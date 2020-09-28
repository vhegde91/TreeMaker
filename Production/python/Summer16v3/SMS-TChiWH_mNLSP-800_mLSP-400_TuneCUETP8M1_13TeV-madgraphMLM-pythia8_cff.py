import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/041E2C6A-10FA-EA11-807A-20CF305B066A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/0C1FF32F-41FC-EA11-B322-002590FD583A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/1E8481CA-07FA-EA11-9D4F-506B4BF38130.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/24572482-06FA-EA11-A817-1866DAED28E4.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/305D86B2-07FA-EA11-9FA5-246E96D14BC8.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/30E768BB-0AFA-EA11-9AE7-FA163E385F2D.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/34E8EA19-16FA-EA11-9309-B026283419E0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/3AAEB8D5-1FFA-EA11-A01B-B496910A9A2C.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/40651E30-39FA-EA11-91DB-B02628DEC1B0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/524676D5-07FA-EA11-8C7D-BC305B390A73.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/5C1F94F4-0AFA-EA11-BFDE-44A842CFC97E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/740EBF53-06FA-EA11-B2F6-0CC47AFF2C3A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/76732C11-0BFA-EA11-BE51-00266CFFC0C0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/7E5039DC-07FA-EA11-9F5E-AC1F6BB1783A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/A07EC529-06FA-EA11-8473-E0071B7A16F0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/A6845D62-10FA-EA11-A374-0CC47A5FC491.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/AE99CA60-4BFA-EA11-B29D-A4BADB1E72AE.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/BE2ABE14-2BFA-EA11-8700-0025905B8572.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/CC36AD03-0BFA-EA11-A73D-0CC47A7DFF5A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/D02495D9-5DFC-EA11-B49C-000E1E875C10.root',
] )
