import os, commands
import subprocess


crabStatus = "crab status "
crabResubmit = "crab resubmit "
cmdls = "ls "
import optparse 

usage = 'usage: %prog -d dirName'
parser = optparse.OptionParser(usage)
parser.add_option("-d","--dir",dest="dir",type="string",help="Crab project folder")
parser.add_option("-v","--verbose",dest="verbose",action="store_true",default=False, help="verbose ")
parser.add_option("-n","--dryrun",dest="dryrun",action="store_true",default=False, help="dry run ")

(opt, args) = parser.parse_args()


if opt.dir is None:
    parser.error('Please define the crab project folder with the option -d')

path = opt.dir + "/"

cmd = cmdls + path
status,ls_la = commands.getstatusoutput( cmd )
dirs = ls_la.split(os.linesep)


if(not os.path.isdir("Logs")): os.system('mkdir Logs')

for d in dirs:
    cmd = crabStatus + path + d
    writer =open("Logs/"+d+".log", 'w') 
    process = subprocess.call(cmd, shell = True, stdout=writer)
    writer.close()
    ifile = open("Logs/"+d+".log", 'r')
    lines = ifile.readlines()
    isFailed = False
    doRemove = False
    if opt.verbose: print "path is ", path+d, " failed jobs"
    print "checking path ", d 
    for l in lines:
        if "SUBMITFAILED" in l:
            print "submit failedfor ", path+d, " removing it now! Please resubmit it "
            isFailed = True
            doRemove = True
            break
        if "failed" in l and not "the max jobs runtime is less than" in l:
            if opt.verbose: print l 
            isFailed = True
            break
        if "idle" in l : print "idle jobs! ", l
        if ("Jobs status"in l) and ("100.0" in l): print " 100% jobs for "+d+" project are Finished"
        if ("Publication status"in l) and ("100.0" in l): print "---> 100% jobs for "+d+" project are Published"
    if (isFailed and not opt.dryrun):
        cmdResub = crabResubmit + path + d
        print "Resubmitting ", d
        writerResub =open("Logs/"+d+"_resub.log", 'w')
        if not doRemove:
            process = subprocess.call(cmdResub, shell = True, stdout=writerResub)
            writerResub.close()
        if doRemove:
            cmdrm="rm -rf "+path+d
            print cmdrm
            
