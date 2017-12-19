#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version information 
__version__ = "0.1.1"
__program__ = "jtds_decrypt v" + __version__
__description__ = "jTDS (JDBC 3.0) Password Decrypter"
__author__ = "whoot"
__licence__ = "BSD Licence"
__status__ = "Final"


import datetime
import argparse

encoding = {'b3':'a',
			'83':'b',
			'93':'c',
			'e3':'d',
			'f3':'e',
			'c3':'f',
			'd3':'g',
			'23':'h',
			'33':'i',
			'03':'j',
			'13':'k',
			'63':'l',
			'73':'m',
			'43':'n',
			'53':'o',
			'a2':'p',
			'b2':'q',
			'82':'r',
			'92':'s',
			'e2':'t',
			'f2':'u',
			'c2':'v',
			'd2':'w',
			'22':'x',
			'32':'y',
			'02':'z',
			'b1':'A',
			'81':'B',
			'91':'C',
			'e1':'D',
			'f1':'E',
			'c1':'F',
			'd1':'G',
			'21':'H',
			'31':'I',
			'01':'J',
			'11':'K',
			'61':'L',
			'71':'M',
			'41':'N',
			'51':'O',
			'a0':'P',
			'b0':'Q',
			'80':'R',
			'90':'S',
			'e0':'T',
			'f0':'U',
			'c0':'V',
			'd0':'W',
			'20':'X',
			'30':'Y',
			'00':'Z',
			'b6':'1',
			'86':'2',
			'96':'3',
			'e6':'4',
			'f6':'5',
			'c6':'6',
			'd6':'7',
			'26':'8',
			'36':'9',
			'a6':'0',
			'a7':' ',
			'b7':'!',
			'87':'"',
			'd7':'\'',
			'df':'§',
			'e7':'$',
			'f7':'%',
			'c7':'&',
			'57':'/',
			'60':'\\',
			'27':'(',
			'37':')',
			'76':'=',
			'56':'?',
			'77':'-',
			'50':'_',
			'17':'+',
			'a1':'@',
			'06':':',
			'16':';',
			'67':',',
			'47':'.' 
			}

# Main
def main(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument('-p', '--pass', dest='password', type=str, nargs='+', help='Password-Hash to crack.')
	args = parser.parse_args()

	try:
		if args.password:
			# get rid of every additional symbol, caused by input
			password = str(args.password).replace('\'', '')
			password = password.replace('[', '')
			password = password.replace(']', '')
			password = password.replace(' ', '')
			# get rid of delimiter
			password = password.replace('a5', '')
			# start decoding
			for char in encoding:
				password = password.replace(char, encoding[char])
			# print password
			print "\n\nPassword is: " + password

	except KeyboardInterrupt:
		print Fore.RED + "\nReceived keyboard interrupt.\nQuitting..." + Fore.RESET
		exit(1)
	except Exception, e:
		import traceback
		print ('generic exception: ', traceback.format_exc())

	finally:
		print '\n'
		now = datetime.datetime.now()
		print __program__ + ' finished at ' + now.strftime("%Y-%m-%d %H:%M:%S") + '\n'
		return True

if __name__ == "__main__":
	import sys
	print('\n' + 50*'*')
	print('\t' + __program__ )
	print('\t' + __description__ )
	print('\t' + '(c)2014 - 2017 by ' + __author__)
	print('\t' + 'Status:\t' + __status__)
	print('\t' + 'For legal purposes only!')
	print(50*'*')
	sys.exit( not main( sys.argv ) )
