import os,sys,shutil,datetime,time
import getpass
from ROOT import *

start_time = time.time()
shift = sys.argv[1]

#IO directories must be full paths
foldnum = '-1'
relbase   = '/home/wzhang/work/fwljmet_201905/CMSSW_10_2_16_UL/'
inputDir = '/isilon/hadoop/store/group/bruxljm/FWLJMET102X_1lep2018_Oct2019_4t_redJECs_040922_step1hadds/'+shift+'/'
#inputDir = '/isilon/hadoop/store/group/bruxljm/FWLJMET102X_1lep2016_Jan2021_4t_redJECs_040922_step1hadds/'+shift+'/'
outputDir = '/isilon/hadoop/store/group/bruxljm/FWLJMET102X_1lep2018_Oct2019_4t_redJECs_05202022_step2/'+shift+'/'
runDir=os.getcwd()
gROOT.ProcessLine('.x compileStep2.C')

sfFileName = 'HT_njets_SF_FourTops_sys_Run2017.root'
if '1lep2018' in inputDir:
    sfFileName = 'HT_njets_SF_FourTops_sys_Run2018.root' 
if '1lep2016' in inputDir:
    sfFileName = 'HT_njets_SF_FourTops_sys_Run2016.root'

cTime=datetime.datetime.now()
date='%i_%i_%i_%i_%i_%i'%(cTime.year,cTime.month,cTime.day,cTime.hour,cTime.minute,cTime.second)

condorDir=runDir+'/'+outputDir.split('/')[-3]+'_condorLogs/'+shift+'/'
print 'Starting submission'
count=0

rootfiles = os.popen('ls '+inputDir)
os.system('mkdir -p '+outputDir)
os.system('mkdir -p '+condorDir)

for file in rootfiles:
#    if 'hdamp' in file: continue 
    if 'root' not in file: continue
    rawname = file[:-6]
    count+=1
    dict={'sfFile':sfFileName, 'RUNDIR':runDir, 'CONDORDIR':condorDir, 'INPUTDIR':inputDir, 'FILENAME':rawname, 'CMSSWBASE':relbase, 'OUTPUTDIR':outputDir}
    jdfName=condorDir+'/%(FILENAME)s.job'%dict
    print jdfName
    jdf=open(jdfName,'w')
    jdf.write(
"""universe = vanilla
Executable = %(RUNDIR)s/makeStep2.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
request_memory = 3072
Transfer_Input_Files = %(RUNDIR)s/%(sfFile)s, %(RUNDIR)s/S2HardcodedConditions.cc, %(RUNDIR)s/S2HardcodedConditions.h, %(RUNDIR)s/makeStep2.C, %(RUNDIR)s/step2.cc, %(RUNDIR)s/step2.h, %(RUNDIR)s/step2_cc.d, %(RUNDIR)s/step2_cc.so, %(RUNDIR)s/Davismt2.cc, %(RUNDIR)s/Davismt2.h, %(RUNDIR)s/Davismt2_cc.d, %(RUNDIR)s/Davismt2_cc.so
Output = %(FILENAME)s.out
Error = %(FILENAME)s.err
Log = %(FILENAME)s.log
JobBatchName = step2_wzhang
Notification = Never
Arguments = %(FILENAME)s.root %(FILENAME)s.root %(INPUTDIR)s %(OUTPUTDIR)s
Queue 1"""%dict)
    jdf.close()
    os.chdir('%s/'%(condorDir))
    os.system('condor_submit %(FILENAME)s.job'%dict)
    os.system('sleep 0.5')                                
    os.chdir('%s'%(runDir))
    print count, "jobs submitted!!!"


print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))

