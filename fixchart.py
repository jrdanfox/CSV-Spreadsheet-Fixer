import sys

#------------------------------ Address 2 stuff ------------------------------------#

# helper method to fix one line
def fixline(line, string, startline, line_no):
	strindex = line.index(string)
	afterstr = line[line.index(string):len(line)]
	firstcommaindex = afterstr.index(",")
	#print("Fixed line " + str(line_no))
	return startline + line[0:strindex  - 1] + ","  + afterstr[0:firstcommaindex] + afterstr[firstcommaindex + 1:len(afterstr)]

# separate Address 2 part from Address column
# Takes Apt, Unit, Ste, #, Fl, Ph out of Address column and puts it into the next column
# Note: for this to work properly there must be an empty column to the right of Address
# TODO: only fix lines where address_2 string is found in Address column (currently
# 		searches the entire line)
# TODO: only fix lines where address_2 string appears at the end of the address column
# 		(fixes bug when adress_2 string appears in street name, etc.)
def add_address_2(filename):
	return 0


	''' TODO: rework to use rows[][]
	print("Fixing lines...")
	line_no = 0

	readfile = open(filename)
	lines = readfile.read().splitlines()
	writefile = open("fixed.csv", 'w')
	
	for someline in lines:
		startline = someline[0:someline.index(",")]
		line = someline[someline.index(","):len(someline)]
		
		if("Apt" in line):
			someline = fixline(line, "Apt", startline, line_no)
		if("Unit" in line):
			someline = fixline(line, "Unit", startline, line_no)
		if("Ste" in line):
			someline = fixline(line, "Ste", startline, line_no)
		if("#" in line):
			someline = fixline(line, "#", startline, line_no)
		if("Fl" in line):
			someline = fixline(line, "Fl", startline, line_no)
		if("Ph" in line):
			someline = fixline(line, "Ph", startline, line_no)
			
		writefile.write(someline + "\n")
	
		line_no = line_no + 1
		#print("Checked line " + str(line_no))	

	readfile.close()
	writefile.close()
	'''
	
#-------------------------- duplicate lname + address stuff ------------------------#
	
def get_lname_address_tuples(lines):
	return 0
	

def remove_extra_lname_address(filename):
	return 0


#-------------------------- helper functions ---------------------------------------#


# takes an array of csv lines and parses it to a multidimensional array
def parse_csv_lines(lines):
	rows = []
	for line in lines:
		row = line.split(",")
		rows.append(row)
		
	return rows

	
# ------------------------------ execute script ------------------------------------#

filename = sys.argv[1]

if (len(sys.argv) <= 2):
	print("Error: Must include filename of file to fix and execution arguments.")
	print("Usage: python fixchart.py <filename> [-a -r]")
	print("-a: Add Address 2 column")
	print("-r: Remove rows with the same Last Name + Address")
	print("Exiting.")
	sys.exit(1)
	
print("Fixing file: " + filename)

readfile = open(filename)
lines = readfile.read().splitlines()
rows = parse_csv_lines(lines)
print(rows[0:10])

if "-a" in sys.argv:
	print("Operation: Add Address 2 column")
	add_address_2(filename)

if "-r" in sys.argv:
	print("Operation: Remove rows with same Last Name + Address")
	remove_extra_lname_address(filename)
	
print("Done.")
