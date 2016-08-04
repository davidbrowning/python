from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

indata = open(from_file).read()
out_file = open(to_file, 'w').write(indata)
print "finished"

out_file.close()
in_file.close()
