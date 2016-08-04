from sys import argv

script, filename = argv

print "erasing %r" % filename
print "undo? CTRL-C (^C)."
print "continue? ENTER"

raw_input("?")

print ("Opening...")
target = open(filename, 'w')

print "Truncating the file. Goodbye!"

target.truncate()

print "I need three lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "writing to file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "closing..."
target.close()
