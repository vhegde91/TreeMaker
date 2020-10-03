import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/064BD8E2-D8E4-E811-9705-002590E7DF2A.root',
       '/store/mc/RunIISummer16MiniAODv3/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/147C8B36-F2E4-E811-88F9-0CC47A1DF806.root',
       '/store/mc/RunIISummer16MiniAODv3/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/28546A8A-F1E4-E811-B6C8-002590E7E07A.root',
       '/store/mc/RunIISummer16MiniAODv3/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/3214826F-E4E4-E811-9E6F-20CF3027A6CB.root',
       '/store/mc/RunIISummer16MiniAODv3/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/44A9F032-F2E4-E811-A356-002590E7DEBE.root',
       '/store/mc/RunIISummer16MiniAODv3/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/54BB50AC-E2E4-E811-BE69-0025904B0468.root',
       '/store/mc/RunIISummer16MiniAODv3/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/7A9F5EC8-F4E4-E811-BDAC-002590E7D5A6.root',
       '/store/mc/RunIISummer16MiniAODv3/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/88A9EBE9-F1E4-E811-8321-0CC47A1E0470.root',
       '/store/mc/RunIISummer16MiniAODv3/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/A660011C-DFE4-E811-9C07-002590E7E050.root',
       '/store/mc/RunIISummer16MiniAODv3/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/CA467C3B-26E5-E811-BD01-0025902D14B0.root',
       '/store/mc/RunIISummer16MiniAODv3/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/CCE89FCE-E9E4-E811-98D6-002590E7E02E.root',
       '/store/mc/RunIISummer16MiniAODv3/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/DC5138F6-F6E4-E811-BC98-002590E7E012.root',
       '/store/mc/RunIISummer16MiniAODv3/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/DE1F487C-F0E4-E811-B50B-AC1F6B0DE3EE.root',
       '/store/mc/RunIISummer16MiniAODv3/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/E8C5DE2E-F2E4-E811-87F2-0CC47A1DF5FA.root',
       '/store/mc/RunIISummer16MiniAODv3/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/EEF42838-DDE4-E811-8202-0CC47ABD6C6C.root',
       '/store/mc/RunIISummer16MiniAODv3/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/1010000/A8EB6E96-07E8-E811-B0CA-00259073E53A.root',
] )
