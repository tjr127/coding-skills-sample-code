from urllib.request import Request, urlopen
#import xml.dom.minidom 
from xml.dom.minidom import parseString
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
req = Request('https://msesandbox.cisco.com/api/contextaware/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc==')
response = urlopen(req)
responseString = response.read().decode("utf-8")
dom = parseString(responseString)
xml = dom.toprettyxml()
print(xml)
floor_element = dom.firstChild
print(floor_element)
if floor_element.hasChildNodes :
 child = floor_element.firstChild
 while child is not None:
     if child.tagName == 'AccessPoint' :
         output = child.tagName + ": " + child.getAttribute('name') + '\t eth: ' + child.getAttribute('ethMacAddress')
         print(output)
     child = child.nextSibling
response.close()