#!/usr/bin/python

import string

def isbn10(isbn):
	if(len(isbn)==10):
		if(isbn.isdigit()):
			sum = 0
			modulo = 11
			for i in range(9):
				sum += int(isbn[i]) * (i+1)
			if sum % modulo == int(isbn[9]):
				return True
			else:
				# print "Check digit is not matched."
				return False 
		else:
			# print "Must be a number collection"
			return False
	else:
		# print "Must has 10 digits"
		return False

def main():
	isbn = raw_input("Enter 10 digits ISBN: ")
	if isbn10(isbn):
		print isbn + " is correct."
	else:
		print isbn + " is not correct."
	main()

if __name__ == '__main__':
	main()
