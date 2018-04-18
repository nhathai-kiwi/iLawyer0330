# coding: utf-8

import os.path
path = os.path.dirname(os.path.abspath(__file__))
print path
path_inFile = path + '/inp.txt'
path_outFile = path + '/out.txt'

def process_ws(in_txt, out_txt):
    print "Tuan process ws"
    cmd = "ls"
    os.system(cmd)
    print "Second"
    cmd = "cd .."
    os.system(cmd)
    print "3rd"
    cmd = "ls"
    os.system(cmd)
    print "4"
    cmd = "java RDRsegmenter " + in_txt + " " + out_txt
    os.system(cmd)
    return 0
# DONE


def print_hello():
    print "Hello"
# process_ws(path_inFile, path_outFile)
