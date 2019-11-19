import os, commands
import subprocess


crabStatus = "crab status "
crabResubmit = "crab resubmit "
cmdls = "ls "
import optparse 

usage = 'usage: %prog -d dirName'
parser = optparse.OptionParser(usage)
parser.add_option("-d","--dir",dest="dir",type="string",help="Crab project folder")

(opt, args) = parser.parse_args()


if opt.dir is None:
    parser.error('Please define the crab project folder with the option -d')

path = opt.dir + "/"

cmd = cmdls + path
status,ls_la = commands.getstatusoutput( cmd )
dirs = ls_la.split(os.linesep)


if(not os.path.isdir("Logs")): os.system('mkdir Logs')
writer =open("DAS_Names.log", 'w') 
for d in dirs:
    cmd = crabStatus + path + d + ' | grep "Output dataset:" | cut -c 16-1000'
    
    print "command is ", cmd
    process = subprocess.call(cmd, shell = True, stdout=writer)
writer.close()
    
