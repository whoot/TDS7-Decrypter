jTDS-Decrypter
==============

Decrypt jTDS (JDBC 3.0) Passwords

Installation
----

You can download the latest tarball by clicking [here](https://github.com/whoot/jTDS-Decrypter/tarball/master) or latest zipball by clicking  [here](https://github.com/whoot/jTDS-Decrypter/archive/master.zip).

Preferably, you can download Type-Enumerator by cloning the [Git](https://github.com/whoot/jTDS-Decrypter) repository:

    git clone https://github.com/whoot/jTDS-Decrypter.git

jTDS-Decrypter works out of the box with [Python](http://www.python.org/download/) version **2.6.x** and **2.7.x** on Debian/Ubuntu, RedHat and Windows platforms.

Usage
----

To get a list of all options use:

    python jtds_decrypt.py -h
    
Example:

	python jtds_decrypt.py -p "a2 a5 b3 a5 92 a5 92 a5 d2 a5 53 a5 82 a5 e3 a5"
	
	**************************************************
        jtds_cracker v0.1.1
        jTDS (JDBC 3.0) Password Cracker
        (c)2014 by it.sec (JaRu)
        Status: Development
        For legal purposes only!
	**************************************************
	
	Password is: password

Bug Reporting
----
Bug reports are welcome! Please report all bugs on the [issue tracker](https://github.com/whoot/jTDS-Decrypter/issues).
