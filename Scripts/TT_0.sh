#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
source /afs/hep.wisc.edu/cms/setup/bashrc
export SCRAM_ARCH=slc6_amd64_gcc530
export HOME=/afs/hep.wisc.edu/home/doyeong
eval `scramv1 project CMSSW CMSSW_8_0_26_patch1`
cd CMSSW_8_0_26_patch1/src/
eval `scram runtime -sh`

cp /hdfs/store/user/ymaravin/test/skim_mt.exe .
cp /hdfs/store/user/ymaravin/test/TypeI-PFMet_Run2016BtoH.root .
chmod u+x skim_mt.exe
./skim_mt.exe mc TT_0.root /hdfs/store/user/ndev/LFV_feb18_mc/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_v6-v1/make_ntuples_cfg-000937CB-A2BE-E611-8C70-B083FEC76567.root 0
gfal-copy TT_0.root gsiftp://cms-lvs-gridftp.hep.wisc.edu:2811//hdfs/store/user/doyeong/test
