# coding: utf-8

import os.path
path = os.path.dirname(os.path.abspath(__file__))
print path
path_inFile = path + '/inp.txt'
path_outFile = path + '/out.txt'

def process_ws(in_txt, out_txt):
    cmd = "java RDRsegmenter " + in_txt + " " + out_txt
    os.system(cmd)
    return 0
# DONE


def print_hello():
    print "Hello"
# process_ws(path_inFile, path_outFile)
