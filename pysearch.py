# Parses the given directory and all subdirectories looking for the Target data

# Standard library imports
import os
import argparse

# Custom search results class to simplify passing details and making sure all needed data is associated with results objects
# Made by me, probably will be buggy initially
from searchresults import search_results

def handle_output(output_file, result, arg):
	"""output handler function, output is getting too complicated and making the code hard to read"""
	
	#this block determines if printing to std out occurs - allows processing multiple flags once and clearly
	if arg.print_flag or arg.no_file_output:
		print_flag = True
		# A valid print detection drops a newline so that results can more easily be read/parsed
		print''
	else:
		print_flag = False
	

	output = result.get_result()
			
	#drops output into the specificed output
	if not arg.no_file_output:
		output_file.write(output)
	if print_flag:
		print output
		

def parse_source(input_dir, input_file, output_file, arg, target_type):


	"""This function will parse either the root's path for the list search_values or the file inputFile
	files are opened in binary mode to avoid hosing windows."""
	#this passes
	search_list = arg.search_values
	#how to handle input
	try:
		if arg.input_file:
			#binary mode flag from command line
			if not arg.binary_file_mode:
				search_input_file = open(arg.input_file, 'rb')
				for line in search_input_file:
					search_list = search_list.append(line)
				search_input_file.close()
			#binary file handling
			else:
				#note that any the file input handler is appended to the end
				search_input_handler = open(arg.input_file, 'rb')
				#should provide a sufficiently small memory base to iterate over the ~ 1mb chunks taken from searched files
				for stream in search_input_handler.read(16384):
					search_list.append(input_stream)
				
			
	#Error handling block for this try
	except IOError as e:
		print 'IO Error in parse_source:'
		print errno + ' - ' + strerror
		print 'Data dump - input_file: %r,  output_file: %r' % input_file, output_file
		raise


	# Parses of the directory's name enter False for inputFile
	if target_type == 'Dir':
		for search_val in search_list:
			if search_val.lower() in input_dir.lower():
				#search_results is the class defined in searchresults.py to handle output data
				handle_output(output_file, search_results(input_dir), arg)
	else:
	
		# Checks the input_file for hits first, this is the file name
		for search_val in search_list:
			if search_val.lower() in input_file.lower():
				handle_output(output_file, search_results(input_dir, input_file), arg)
		#flag that indicates not to search in files - from cli arguments
		if not arg.names_only:
			#file interaction - Error city
			try:
			
				if not arg.binary_file_mode:
					#opens input_file for searching
					input_file_handler = open(os.path.join(input_dir, input_file), 'rb')
					line_count = 0
					
					for line in input_file_handler:
						line_count = line_count + 1
						
						for search_val in search_list:
							#loops through file and search list to compare all permutations
							
							if search_val.lower() in line.lower():
								handle_output(output_file, search_results(input_dir, input_file, line, line_count), arg)
				else:
					for search_val in search_list:
						for data in input_file.read(1048576):
							# Should provide a sufficiently large memory base to iterate over for search results
							if search_val in data:
							
								handle_output(output_file, search_results(input_dir, input_file, line, data.tell()))
					
			except IOError as e:
				print 'IO Error in parse_source:'
				print errno + ' - ' + strerror
				print 'Data dump - input_file: %r,  output_file: %r' % input_file, output_file
				raise

# Main program control function			
def Main():
	
	parser = argparse.ArgumentParser(description='Process a directory for parsable text lines.', prog='pysearch')
	#creates a group to allow for mutual exclusion for a few of the args
	output_options = parser.add_mutually_exclusive_group()
	
	parser.add_argument('-t', action='store', dest='target_directory', default=os.getcwd(), help='Path to target Directory. Targets pwd if not provided.')
	parser.add_argument('-f', action='store', dest='input_file', default=False, help='Input from a file. Takes a relative or absolute filepath.')
	parser.add_argument('-b', action='store_true', dest='binary_file_mode', default=False, help='Searches for through files in binary mode.  Works best with file input for obvious reasons.')
	parser.add_argument('-n', action='store_true', dest='names_only', default=False, help='Searches only directory and file names, not content.')
	parser.add_argument('-p', action='store_true', dest='print_flag', default=False, help='Print to the stdout. Defaults to off. Potentially lots of system alarms printing.')
	parser.add_argument('-l', action='store_false', dest='record_line', default=True, help='By default the program provides the line that gets the searh hit to output. -r prevents that.')
	output_options.add_argument('-o', action='store', dest='output_file', default='pySeachLog.txt', help='File for output.  Will default to pySearchLog.txt')
	output_options.add_argument('-pO', action='store_true', dest='no_file_output', default=False, help='Print only. Does not write to the output file.')
	parser.add_argument('search_values', action='store', nargs='+', help='Values to search for.')
	#parses the arguments as set above, see argparse docs if not familiar with syntax
	args = parser.parse_args()
	
	
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
		parse_source(root, False, search_output_file, args, 'Dir')
		# This loop runs through the file name and file itself for each entry
		for file in files:
			parse_source(root, file, search_output_file, args, 'File')
	#closes output file		
	search_output_file.close()
	print 'Completed.'

#runs program when the file is run
Main()