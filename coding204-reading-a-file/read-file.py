# Most basic example of reading from a file

# amwhaley@cisco.com
# twitter: @mandywhaley
# http://developer.cisco.com
# http://developer.cisco.com/learning
# Jan 15, 2015

# * THIS SAMPLE APPLICATION AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY
# * OF ANY KIND BY CISCO, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED
# * TO THE IMPLIED WARRANTIES OF MERCHANTABILITY FITNESS FOR A PARTICULAR
# * PURPOSE, NONINFRINGEMENT, SATISFACTORY QUALITY OR ARISING FROM A COURSE OF
# * DEALING, LAW, USAGE, OR TRADE PRACTICE. CISCO TAKES NO RESPONSIBILITY
# * REGARDING ITS USAGE IN AN APPLICATION, AND IT IS PRESENTED ONLY AS AN
# * EXAMPLE. THE SAMPLE CODE HAS NOT BEEN THOROUGHLY TESTED AND IS PROVIDED AS AN
# * EXAMPLE ONLY, THEREFORE CISCO DOES NOT GUARANTEE OR MAKE ANY REPRESENTATIONS
# * REGARDING ITS RELIABILITY, SERVICEABILITY, OR FUNCTION. IN NO EVENT DOES
# * CISCO WARRANT THAT THE SOFTWARE IS ERROR FREE OR THAT CUSTOMER WILL BE ABLE
# * TO OPERATE THE SOFTWARE WITHOUT PROBLEMS OR INTERRUPTIONS. NOR DOES CISCO
# * WARRANT THAT THE SOFTWARE OR ANY EQUIPMENT ON WHICH THE SOFTWARE IS USED WILL
# * BE FREE OF VULNERABILITY TO INTRUSION OR ATTACK. THIS SAMPLE APPLICATION IS
# * NOT SUPPORTED BY CISCO IN ANY MANNER. CISCO DOES NOT ASSUME ANY LIABILITY
# * ARISING FROM THE USE OF THE APPLICATION. FURTHERMORE, IN NO EVENT SHALL CISCO
# * OR ITS SUPPLIERS BE LIABLE FOR ANY INCIDENTAL OR CONSEQUENTIAL DAMAGES, LOST
# * PROFITS, OR LOST DATA, OR ANY OTHER INDIRECT DAMAGES EVEN IF CISCO OR ITS
# * SUPPLIERS HAVE BEEN INFORMED OF THE POSSIBILITY THEREOF.-->
from pathlib import Path
import sys, os
here = Path(__file__).parent.absolute()
print(here)
repository_root = (here / ".." ).resolve()
print(repository_root)
file_to_write = here / "my-file.txt"
print(file_to_write)

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, filename = os.path.split(full_path)
print(path + ' --> ' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path))

sys.path.insert(0, str(repository_root))
sys.path.insert(0, str(here))

# Use the open method to open a file
# Pass in the name of the file to open and mode. 'r' for read only 'w' if you want to write to the file
my_file_object = open("my-file.txt", "r")

print ("Read the whole file at once:")

# read() reads in the entire file.  In this line of code, we read in the contents of the file and print it to the screen.
print (my_file_object.read())
print ("\n")

# .close closes the file object
my_file_object.close()