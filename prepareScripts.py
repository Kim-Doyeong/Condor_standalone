import os, sys, re

# Usage python prepareScripts.py <name> <locationOfInputFiles> <outputDirectory>
# outputDirectory has to be in /hdfs area, like so: /hdfs/store/user/doyeong for example

if len(sys.argv) != 4:
    print len(sys.argv)
    print "Usage python prepareScripts.py <name> <locationOfInputFiles> <outputDirectory>"
    sys.exit(-1)

name = sys.argv[1]
filesToProcess = os.popen("ls " + sys.argv[2] + "/*root").readlines()
outputDir = sys.argv[3]

# A chunk of a execution script that is the same for every file to be skimmed
# Essentially a preparatory stuff  - what needs to be setup for  the job to run
scriptHeader = """#!/bin/bash
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
"""

# Counter for files
counter = 0
# For each file in the list create a  submission script
for item in filesToProcess:
    file = open("Scripts/" + name + "_" + str(counter) + ".sh", "w")
    # write  the header
    file.write(scriptHeader)
    # execute script with a given input variables
    file.write("./skim_mt.exe mc " +  name + "_" + str(counter) + ".root " + item[:-1] + " 0\n")
    # copy the output to hdfs
    file.write("gfal-copy " + name + "_" + str(counter) + ".root gsiftp://cms-lvs-gridftp.hep.wisc.edu:2811/" + outputDir + "\n")
    file.close()
    counter += 1

# Create a submission script
file = open("submit_" + name + ".sh", "w")
for i in range(0, counter):
    file.write("source submitProduction.csh " + name + " " + str(i)  + "\n")
