#!/bin/csh

rm -f condor_${1}_${2}
cat > condor_${1}_${2} <<EOF

universe = vanilla
executable = Scripts/${1}_${2}.sh
should_transfer_files = yes
WhenToTransferOutput = on_exit
Requirements = TARGET.Arch == "x86_64" && HasAFS_OSG && TARGET.UWCMS_CVMFS_Exists && TARGET.CMS_CVMFS_Exists && HAS_CMS_HDFS
Arguments = ${2}
Output = Logs/${1}_${2}.out
Error = Logs/${1}_${2}.err
Log = Logs/${1}_${2}.log
x509userproxy = /tmp/x509up_u23241
Queue 
EOF

condor_submit condor_${1}_${2}
