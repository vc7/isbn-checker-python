#!/usr/bin/python

import string

def isbn13(isbn):
	if(len(isbn)==13):
		if(isbn.isdigit()):
			sum = 0
			modulo = 10
			for i in range(13-1):
				subsum = 0
				if i%2:
					subsum = int(isbn[i]) * 3 
				else:
					subsum = int(isbn[i]) * 1
				print subsum
				sum += subsum
			if (modulo - (sum % modulo)) == int(isbn[13-1]):
				return True
			else:
				# print "Check digit is not matched."
				return False 
		else:
			# print "Must be a number collection"
			return False
	else:
		# print "Must has 13 digits"
		return False

def main():
	isbn = raw_input("Enter 13 digits ISBN: ")
	if isbn13(isbn):
		print isbn + " is correct."
	else:
		print isbn + " is not correct."
	main()

if __name__ == '__main__':
	main()
