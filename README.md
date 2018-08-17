# Condor_standalone
Submitting standalone exe on Wisconsin machines

Yurii prepared all code and instructions for me. It was all thanks to Yurii. 

Here are the instructions for my skimmer, but it is fairly general.
## Preparation:
1. important files: prepareScripts.py (check for doyeong - replace with your user name)

     directory Scripts <- the script above will put stuff in it
     
     directory Logs  <-  output logs for job debugging
     
     submitProduction.sh <- submission script, needs to be modified in line 14 with  your own grid proxy file  (see below)
     
2. How to get your grid proxy file on wisconsin machine:

   ```voms-proxy-init --voms=cms --valid=48:00```

   ```ls -lrt /tmp```

   Find your proxy  (you are owner and it  is most likely the bottom-most file in the list, i.e., most recently created).
modify the ```submitProduction.sh``` with your own proxy file name

3. How to run the code, say you want to process TT files:

   ```python prepareScripts.py TT /hdfs/store/user/ndev/LFV_feb18_mc/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_v6-v1 /hdfs/store/user/ymaravin/test```


   I run prepareScripts.py with the name "TT" (call  it anyway you want),
input directory with TT_Tune etc. then output area (must be in hdfs)

   This would create a lot of files in Scripts/  area, all named TT_*.sh (986 total).

   Each file is dedicated to process only  one file (takes  about 10  sec each).




You have to have a valid  proxy: ```voms-proxy-init --voms=cms --valid=48:00```

You can submit it  manually one by  one:
```source submitProduction.sh TT 0```

or run the code to submit all of them at once:
```source submit_TT.sh```
