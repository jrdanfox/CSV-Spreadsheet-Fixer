import sys

#------------------------------ Address 2 stuff ------------------------------------#

# separate Address 2 part from Address column
# Takes Apt, Unit, Ste, #, Fl, Ph out of Address column and puts it into the next column
# Note: for this to work properly there must be an empty column to the right of Address
# TODO: only fix lines where address_2 string appears at the end of the address column
# 		(fixes bug when adress_2 string appears in street name, etc.)
def add_address_2(rows):
	line_no = 0
	for row in rows:
		address = row[1]

		if("Apt" in address):
			index = address.index("Apt")
			row[1] = address[0:index]
			row[2] = address[index:]
		if("Unit" in address):
			index = address.index("Unit")
			row[1] = address[0:index]
			row[2] = address[index:]
		if("Ste" in address):
			index = address.index("Ste")
			row[1] = address[0:index]
			row[2] = address[index:]
		if("#" in address):
			index = address.index("#")
			row[1] = address[0:index]
			row[2] = address[index:]
		if("Fl" in address):
			index = address.index("Fl")
			row[1] = address[0:index]
			row[2] = address[index:]
		if("Ph" in address):
			index = address.index("Ph")
			row[1] = address[0:index]
			row[2] = address[index:]

		line_no += 1

#-------------------------- duplicate lname + address stuff ------------------------#
	
def get_lname_address_tuples(lines):
	return 0
	

def remove_extra_lname_address(rows):
	return 0

#-------------------------- helper functions ---------------------------------------#

# takes an array of csv lines and parses it to a multidimensional array
def parse_csv_lines(lines):
	rows = []
	for line in lines:
		row = line.split(",")
		rows.append(row)
		
	return rows

# write a multidimensional array to a csv
def write_to_csv(rows):
	writefile = open("fixed.csv", 'w')

	for row in rows:
		string = ""
		for i in row:
			string += i + ","
		writefile.write(string[0:len(string) - 1] + "\n")

	writefile.close()
	
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
	add_address_2(rows)

if "-r" in sys.argv:
	print("Operation: Remove rows with same Last Name + Address")
	remove_extra_lname_address(rows)

write_to_csv(rows)
	
readfile.close()
print("Done.")
