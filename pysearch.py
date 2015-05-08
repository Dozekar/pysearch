# Parses the given directory and all subdirectories looking for the Target data

import os
import argparse


def parse_source(input_dir, input_file, output_file, arg):


	# This function will parse either the root's path for the list search_values or the file inputFile
	# files are opened in binary mode to avoid hosing windows.
	
	if arg.input_file:
		print 'Inputting a file as the source for the search list is not yet Functional.  Planned in version 0.2'
		quit()
	else:
		search_list = arg.search_values
		
	#this block determines if printing to std out occurs - allows processing multiple flags once and clearly
	if arg.print_flag or arg.no_file_output:
		print_flag = True
		print ''
	else:
		print_flag = False
	
	# Parses of the directory's name enter False for inputFile
	if not input_file:
		for search_val in search_list:
			if search_val.lower() in input_dir.lower():
				output_file.write('Dir - ' + input_dir)
				if print_flag:
					print 'Directory - ' +  input_dir
	else:
	
		# Checks the input_file for hits first, this is the filename
		for search_val in search_list:
			if search_val.lower() in input_file.lower():
				if not arg.no_file_output:
					output_file.write('File - ' + os.path.join(input_dir, input_file) )
				if print_flag:
					print 'File - ' + os.path.join(input_dir, input_file)
					
		#flag that indicates not to search in files - from cli arguments
		if not arg.names_only:
			#file interaction - Error city
			try:
				#opens input_file for searching
				input_file_handler = open(os.path.join(input_dir, input_file), 'rb')
				line_count = 0
				for line in input_file_handler:
					line_count = line_count + 1
					for search_val in search_list:
						#loops through file and search list to compare all permutations
						if search_val.lower() in line.lower():
							if not arg.no_file_output:
								output_file.write('Line - ' + os.path.join(input_dir, input_file) + ' - line #: ' + str(line_count) + " - " + line)
							if print_flag:
								print 'Line - ' + os.path.join(input_dir, input_file) + ' - line #: ' + str(line_count) + '\n' + line
			except IOError as e:
				print 'IO Error in parse_source:'
				print errno + ' - ' + strerror
				print 'Data dump - input_file: %r,  output_file: %r' % input_file, output_file
		
		if arg.binary_file_mode:
			print 'Support for this feature is not yet implemented.  Planned in version 0.3'
			quit()

			
def Main():
	# Main program control function
	parser = argparse.ArgumentParser(description='Process a directory for parsable text lines.', prog='pysearch')
	
	output_options = parser.add_mutually_exclusive_group()
	#creates a group to allow for mutual exclusion for a few of the args
	
	parser.add_argument('-t', action='store', dest='target_directory', default=os.getcwd(), help='Path to target Directory. Targets pwd if not provided.')
	parser.add_argument('-f', action='store', dest='input_file', default=False, help='Input from a file. Takes a relative or absolute filepath.')
	parser.add_argument('-b', action='store_true', dest='binary_file_mode', default=False, help='Searches for through files in binary mode.  Works best with file input for obvious reasons.')
	parser.add_argument('-n', action='store_true', dest='names_only', default=False, help='Searches only directory and file names, not content.')
	parser.add_argument('-p', action='store_true', dest='print_flag', default=False, help='Print to the stdout. Defaults to off. Potentially lots of system alarms printing.')
	output_options.add_argument('-o', action='store', dest='output_file', default='pySeachLog.txt', help='File for output.  Will default to pySearchLog.txt')
	output_options.add_argument('-pO', action='store_true', dest='no_file_output', default=False, help='Print only. Does not write to the output file.')
	parser.add_argument('search_values', action='store', nargs='+', help='Values to search for.')
	
	args = parser.parse_args()
	#parses the arguments as set above, see argparse docs if not familiar with syntax
	
	# This initializes the output file when one is in use
	# While file IO is notorious for errors, honestly we'd rather just crash here with default error handling usually.	
	if not args.no_file_output:
		search_output_file = open(args.output_file, 'wb')
	else:
		search_output_file = False 

	# Runs through the directory and all subdirectories and provides a record for each of them. 
	# Note that by default this ignores symbolic links to avoid infinite recursion problems
	walk_record = os.walk(args.target_directory)
	
	#main loop on the walk record
	for root, dirs, files in walk_record:
		#This will search the directory name
		parse_source(root, False, search_output_file, args)
		# This loop runs through the file name and file itself for each entry
		for file in files:
			parse_source(root, file, search_output_file, args)
			
		print 'Completed.'

#runs program when the file is run
Main()