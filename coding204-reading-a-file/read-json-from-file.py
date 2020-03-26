# How to read json from a file

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

# import the json library.  This library provides many handy features for formatting, displaying
# and manipulating json.
import json, os


##Change the working environment to the local directory since VS Code messes it up. 
os.chdir('/home/tjr127/projects/coding-skills-sample-code/coding204-reading-a-file')


# use 'with" to open the file containing json
with open('my-json.json') as file:
    # read the whole file
    data = json.loads(file.read()) 
    
# access values from the json and loop through devices and display the network device id
i = 0
for item in data["response"]:
    print ("Network Device ID: " + data["response"][i]["networkDeviceId"] + "  Tag: " + data["response"][i]["tag"])
    i += 1

