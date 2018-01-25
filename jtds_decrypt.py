#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/](http://www.gnu.org/licenses/)
#-------------------------------------------------------------------------------

# Version information 
__version__ = "1.0"
__program__ = "jtds_decrypt v" + __version__
__description__ = "jTDS (JDBC 3.0) Password Decrypter"
__author__ = 'https://github.com/whoot'
__licence__ = "BSD Licence"
__status__ = "Final"

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
	parser.add_argument('-p', '--pass', dest='password', type=str, nargs='+', help='Passwordhash to crack.')
	args = parser.parse_args()

	try:
		if args.password:
			# get rid of delimiter
			password = str(args.password).replace('a5', '')
			# start decoding
			for char in encoding:
				password = password.replace(char, encoding[char])

			password = password.replace(' ', '')
			password = password.replace('\'', '')
			password = password.replace('[', '')
			password = password.replace(']', '')
			password = password.replace(' ', '')
			print '\nPassword is: %s\n' %password

	except Exception, e:
		import traceback
		print ('generic exception: ', traceback.format_exc())


if __name__ == "__main__":
	import sys
	print('\n' + 50*'*')
	print('\t' + __program__ )
	print('\t' + __description__ )
	print('\t' + __author__)
	print('\t' + 'Status:\t' + __status__)
	print('\t' + 'For legal purposes only!')
	print(50*'*')
	sys.exit( not main( sys.argv ) )
