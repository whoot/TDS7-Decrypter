TDS7-Decrypter
==============

Decrypt TDS7 Login Passwords

Installation
----

You can download the latest tarball by clicking [here](https://github.com/whoot/TDS7-Decrypter/tarball/master) or latest zipball by clicking  [here](https://github.com/whoot/TDS7-Decrypter/archive/master.zip).

Preferably, you can download Type-Enumerator by cloning the [Git](https://github.com/whoot/TDS7-Decrypter) repository:

    git clone https://github.com/whoot/TDS7-Decrypter.git

TDS7-Decrypter works out of the box with [Python](http://www.python.org/download/) version **2.7** on Debian/Ubuntu, RedHat and Windows platforms.

Usage
----

To get a list of all options use:

    python tds_decrypt.py -h
    
Example:

	python tds_decrypt.py -p "a2 a5 b3 a5 92 a5 92 a5 d2 a5 53 a5 82 a5 e3 a5"
	
	**************************************************
		tds_decrypt v1.0
		TDS Password Decrypter
		https://github.com/whoot
		Status:	Final
		For legal purposes only!
	**************************************************

	Password is: password

Bug Reporting
----
Bug reports are welcome! Please report all bugs on the [issue tracker](https://github.com/whoot/TDS7-Decrypter/issues).
