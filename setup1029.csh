cmsenv
git cms-init
git cms-merge-topic cms-met:METFixEE2017_949_v2_backport_to_102X
git clone git@github.com:cms-jet/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_102X_v1
git cms-addpkg RecoMET/METFilters
git cms-merge-topic cms-egamma:EgammaPostRecoTools
git clone git@github.com:oiorio/B2GAnaFW.git Analysis/B2GAnaFW -b CMSSW_9_4_X_V2

# dataset dataset=/MET/*Run2018*/MINIAOD

#dataset=/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM
