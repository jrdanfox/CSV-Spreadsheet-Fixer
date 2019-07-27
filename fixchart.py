import sys, collections

#------------------------------ Address 2 stuff ------------------------------------#

# separate Address 2 part from Address column
# Takes Apt, Unit, Ste, #, Fl, Ph out of Address column and puts it into the next column
# Note: for this to work properly there must be an empty column to the right of Address
def add_address_2(rows):
	line_no = 0
	address_2_strings = ["Apt ", "Unit ", "Ste ", "#", "Fl ", "Ph "]
	for row in rows:
		address = row[1]

		for address_2_string in address_2_strings:
			if (address_2_string in address):
				index = address.index(address_2_string)
				row[1] = address[0:index]
				row[2] = address[index:]

		line_no += 1

#-------------------------- duplicate lname + address stuff ------------------------#
	

# returns a dictionary of {(address, lname), (count(address, lname), line_no)}
# TODO: maybe use (row[1].strip(), row[8].strip()) if whitespaces causes issues
#			hint: "a " != "a"
# TODO: dynamically get address, lname columns
def get_lname_address_pairs(rows):
	pairs = collections.OrderedDict()
	for i, row in enumerate(rows, start = 0):
		pair = (row[1], row[8])
		default_value = (1, i)
		if pair in pairs:
			pairs[pair] = (pairs[pair][0] + 1, i)
		else:
			pairs[pair] = default_value
	return pairs
	
def remove_extra_lname_address(rows):
	pairs = get_lname_address_pairs(rows)

	for x, y in reversed(pairs.items()):
		if y[0] > 1 and x[0] != "" and x[1] != "":
			rows[y[1] - 1][5] = rows[y[1]][4]
			rows[y[1] - 1][7] = rows[y[1]][6]
			del rows[y[1]]

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

if "-a" in sys.argv:
	print("Operation: Add Address 2 column")
	add_address_2(rows)

if "-r" in sys.argv:
	print("Operation: Remove rows with same Last Name + Address")
	remove_extra_lname_address(rows)

write_to_csv(rows)
	
readfile.close()
print("Done.")
