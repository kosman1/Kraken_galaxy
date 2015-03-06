#!/usr/bin/env python

"""
Kraken wrapper in python - TODO: Describe
"""

import re,sys,optparse,fileinput
import subprocess,os,shutil

def stop_err(msg):
    sys.stderr.write("%s\n" % msg)
    sys.exit()


DBNAME = sys.argv[1]
inp = sys.argv[2]
out = sys.argv[3]

try:
    tmp_stdout = open(out,'wb')
    cmd = "karken --db %s %s > %s" % (DBNAME,inp,out)
    print cmd
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True)
    output, err = proc.communicate
    print output

except:
    sys.stdout.write("Could not run kraken \n")
