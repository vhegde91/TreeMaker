import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/0E13372A-2942-E811-825A-002590D9D894.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/2A6FFBB4-1B42-E811-82F4-002590FD5A72.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/38865700-4F42-E811-BDAE-0CC47A0AD74E.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/8E85803F-4B42-E811-90AB-0CC47A0AD6E0.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/9860FB4A-1242-E811-A708-0CC47AA53D8A.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/9A9DA968-4842-E811-B9AA-002590D9D84A.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/B6AC5A08-4542-E811-96E3-002590FD5694.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/C295EB56-4D42-E811-A5FB-0CC47A0AD4A5.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/CC53D89E-3242-E811-8981-002590D9D8B2.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/D0A1C463-3E42-E811-A093-0CC47AA53D6E.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/D4832A32-3D42-E811-BD8E-00259075D708.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/1EDC12D9-4742-E811-A484-0CC47AA53D6E.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/221241BA-8042-E811-BCA5-0CC47A57D164.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/3A8BD42F-2342-E811-A776-00259048AC9A.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/8A76CF62-AF42-E811-A6D8-003048CB8610.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/A6F966EA-AF42-E811-936B-00259048AD6A.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/B48D4BF8-C042-E811-8413-0025905A60E0.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/B8D9D5FA-C042-E811-99B5-0CC47AA53D60.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/D407550A-B642-E811-AFDE-0CC47AD24D32.root',
       '/store/mc/RunIIFall17MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/E47D84AF-2442-E811-B841-00259029E7FC.root',
] )
