import os

class search_results(object):
	""" This is a class for holding and processing search results to allow generic handling more easily 
		while not terribly complex this is a separate file for readability and to make it easier to add to.
		This module may be added to the base code of pysearch if it isn't too hard to read or long, 
		but for not it's separate"""
	
	def __init__(self):
		# Generic constructor This can by validated by testing for type = False
		self.file_name = False
		self.dir_path = False
		self.line_contents = False
		self.file_result_location = False
		self.result_type = False
		
	def __init__(self, in_dir_path)
		# Directory result constructor
		self.file_name = False
		self.dir_path = in_dir_path
		self.line_contents = False
		self.file_result_location = False
		self.result_type = "Directory"
	
	def __init__(self, in_file_name, in_dir_path)
		# File result constructor
		self.file_name = in_file_name
		self.dir_path = in_dir_path
		self.line_contents = False
		self.file_result_location = False
		self.result_type = "File"
		
	def __init__(self, in_file_name, in_dir_path, in_line_contents, in_file_result_location)
		# Line result constructor
		self.file_name = in_file_name
		self.dir_path = in_dir_path
		self.line_contents = in_line_contents
		self.file_result_location = in_file_result_location
		self.result_type = "Line"
		
	def set_dir(self, in_dir_path)
		#	Sets this object to a Dir result with the input as the passed data
		# Removes no longer Valid data as well values are checked for false first
		if self.file_name:
			self.file_name = False
		self.dir_path = in_dir_path
		if self.line_contents:
			self.line_contents = False
		if self.file_result_location:
			self.file_result_location = False
		self.result_type = "Directory"
	
	def get_dir(self)
		# Returns Dir info as a string
		return self.dir_path
	
	def set_file_name(self, in_file_name, in_dir_path)
		#	Sets this object to a File result with the input as the passed data
		# Removes no longer Valid data as well values are checked for false first
		self.file_name = in_file_name
		self.dir_path = in_dir_path
		if self.line_contents:
			self.line_contents = False
		if self.file_result_location:
			self.file_result_location = False
		self.result_type = "File"
		return self
	
	def get_file_name(self)
		# Returns File info as a string
		return self.file_name
		
		
	def set_line(self, in_file_name, in_dir_path, in_line_contents, in_file_result_location)
		# Sets result to a line with the input values
		self.file_name = self.in_file_name
		self.dir_path = self.in_dir_path
		self.line_contents = self.in_line_contents
		self.file_result_location = self.in_file_result_location
		self.result_type = "Line"
		return self
		
	def get_line_contents(self)
		# Return line info as a string
		return self.line_conents
		
	def get_file_result_location(self)
		return self.file_result_location
		
	def get_type()
		return self.type
	
	def get_result()
	#formatting to make reading easier is the real benefit here
		if get_type() == 'Directory':
			output = self.get_type()+ ': ' + self.get_dir()
		else:
			if get_type() == 'File':
				output = self.get_type() + ': ' + os.path.join(self.get_dir(), self.get_file_name())
			else:
				#note: \ continues the line if it ends it
				output = self.get_type() + ': ' + os.path.join(self.get_dir(), self.get_file_name()) + \
				' - ' + get_file_result_location() + ' - ' + get_line_contents()
		return output
		
	def get_result_no_contents()
		if get_type() == 'Directory':
			output = self.get_type()+ ': ' + self.get_dir()
		else:
			if get_type() == 'File':
				output = self.get_type() + ': ' + os.path.join(self.get_dir(), self.get_file_name())
			else:
				#note: \ continues the line if it ends it
				output = self.get_type() + ': ' + os.path.join(self.get_dir(), self.get_file_name()) + \
				' - ' + get_file_result_location()
		return output
		