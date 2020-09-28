# format for dict entries:
#                                                data: [0,  ['sample'] , []]
#                                                  MC: [1, ['sample'] , []]
#                                      MC w/ wrong PU: [2, ['sample'] , []]
#                               MC w/ extended sample: [1, ['sample','sample_ext'] , []]
#                   MC w/ negative weights (amcatnlo): [1, ['sample'] , [neff]]
# MC w/ negative weights (amcatnlo) + extended sample: [1, ['sample','sample_ext'] , [neff, neff_ext]]

flist = [
# [1, ['/TChiWZ_800_100/hatake-TChiWZ_800_100_step3-36647d14426d868d82af2cc449946ac8/USER'] , []],
# [1, ['/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM'] , []],
[1, ['/SMS-TChiWH_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChiWH_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChiWH_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChiWZ_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChiWZ_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChiWZ_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChipmWW_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChipmWW_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChipmWW_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'] , []],
[1, ['/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'] , []],
[1, ['/SMS-TChiWH_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'] , []],
[1, ['/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'] , []],
[1, ['/SMS-TChiWH_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'] , []],
[1, ['/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'] , []],
[1, ['/SMS-TChiWH_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'] , []],
[1, ['/SMS-TChiWH_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'] , []],
[1, ['/SMS-TChiWZ_mNLSP-400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'] , []],
[1, ['/SMS-TChiWZ_mNLSP-400_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'] , []],
[1, ['/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'] , []],
[1, ['/SMS-TChiWZ_mNLSP-800_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'] , []],
[1, ['/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'] , []],
[1, ['/SMS-TChiWZ_mNLSP-800_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'] , []],
]
