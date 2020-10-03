import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/082F9834-5DB7-7845-8A7B-BBE763FA8DA9.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/130ED2C9-A10E-1444-B2C2-27219592054F.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/14A97F12-3244-8141-9437-D26B18FED246.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/1EAA322D-B4A6-464B-9D3D-1D75A522F147.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/208BB8EA-2B9D-414B-B0FB-D3323DC8F003.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/259EB4AB-AF5D-CF41-8B39-D7BE759EF771.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/2D95B1E8-B06F-684F-8C6D-3B2A3DC38705.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/3D670881-EFAB-3041-9791-5E4A7DECDC95.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/4080FB9F-994D-C64D-9CDC-DC56F5D10ED5.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/41BF7B28-91AD-8C4F-960B-E4DEA04F4E4B.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/434BB783-4F7B-FE42-9FCB-9BD34DA10CB7.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/7D601127-D2D2-8C4E-BC65-62AD89D3EBCD.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/84F225B4-6DC8-4D47-AB4F-E16DEEB623AD.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/897FE751-CDE4-5E47-A55D-A51FDF2DD739.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/91E6D24F-E1D8-994B-8296-72FAE29B6374.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/9852EFB6-CF26-8247-BE5D-1C4FC5161284.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/9BB8E901-6D33-A645-8A23-D164D989285F.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/9FE56247-9594-EE49-BB56-A8A6E92472DF.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/B813088C-EC44-0643-9C9B-DA8507070B7B.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/BBEB0441-27D3-FE41-9A19-0F5B4B674EB7.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/C2B4BC18-FDE6-FC4D-B35A-6479D2E5B4DE.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/C2DF4FB5-B7A5-914E-BC78-9D3312AF07A4.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/C8012C55-2D40-D14F-A560-9BAAFF25D2B4.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/D2EEFB31-9957-A74E-904E-B4C548C7BC8D.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/D56E9DAA-6F82-3541-962B-38CC6AABBC44.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/D95F1D5A-7CBF-F245-B7DF-C7A8368C5C8F.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/DCB81FDA-18C0-D644-8675-28F9CED4A0D5.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/DF620C48-E1CB-6E44-BFB8-697223DECB68.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/E1EE5548-99C2-0B40-B27B-D1FF07C389FE.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/10000/F900E53F-75BB-E048-A568-02F7C27FA40F.root',
] )
