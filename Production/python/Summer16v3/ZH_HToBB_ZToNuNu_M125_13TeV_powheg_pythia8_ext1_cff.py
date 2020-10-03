import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/2E264888-2F20-E911-A698-0025905C54FC.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/58B3DF7D-6320-E911-A9BE-0025905C53B0.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/7077A22E-2820-E911-A7C4-0025905C5430.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/8A765201-2820-E911-8787-0025905C3E36.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/94BF47AA-2720-E911-AA1D-0CC47AF9B2C2.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/02A7DF3B-4920-E911-ACBE-0025905D1D52.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/20AAE726-4E20-E911-8DF6-0CC47AFF01F0.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/3A4B2CBD-3020-E911-8EB3-0025905D1CB0.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/44003C58-4E20-E911-AA4F-0CC47AFCC396.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/4EAD370B-5220-E911-90CA-0025905C3DD0.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/5236A622-4E20-E911-9EF8-0CC47AFF0274.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/5E12F1AE-9820-E911-83D2-0CC47AF9B23A.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/688CAB29-4E20-E911-B84B-0CC47AFCC37A.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/6C10E2D7-5920-E911-BAF4-0CC47AFCC69E.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/7431A8B7-5820-E911-B8A7-003048947BB9.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/76CFE60B-4E20-E911-B208-0025904C669C.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/8A9F4D25-5D20-E911-BE4C-0025905C542C.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/8E4BF2F4-5120-E911-A427-0025904C678A.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/9CFFCCA6-6220-E911-B183-0025905C42A2.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/D09EC48C-4D20-E911-A894-0CC47AFCC3FE.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/D87B0499-5320-E911-8985-0CC47AFCC62A.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/DA6312C3-4F20-E911-BAC4-0CC47AFF0478.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/E0AE31E0-5320-E911-9AC2-0CC47AFF0230.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/F431ABE4-5720-E911-BB55-0CC47AFCC6EE.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/F653764F-5320-E911-B14E-0CC47AFF0208.root',
       '/store/mc/RunIISummer16MiniAODv3/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/80000/FABE2F2D-5220-E911-B097-0CC47AFF0208.root',
] )
