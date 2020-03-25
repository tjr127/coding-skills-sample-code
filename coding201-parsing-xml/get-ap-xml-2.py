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
print(dom)
print("*************************************")
xml = dom.toprettyxml()
print(xml)
response.close()