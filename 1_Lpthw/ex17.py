# -- coding: utf-8 --
from sys import argv
"""
from os.path import exists

script, from_file, to_file = argv

print "coping from %s to %s" %(from_file, to_file)

indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" %exists(to_file)
print "Ready,hit Return to continue, CTRL-C to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

output.close()
"""
script, from_file, to_file = argv
open(to_file, 'w').write(open(from_file).read())

