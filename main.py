from lxml import etree
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom
class Xmlcheck():
	xml_file = "valid.xml"
	org_name = "kbiz"
	brn_name = "test"
	
	def valid_xml(self):
		ET.register_namespace('', "http://maven.apache.org/POM/4.0.0")
		with open(self.xml_file, 'r') as xml_file:
			xml_data = xml_file.read()
			xmldoc = minidom.parse(self.xml_file)
			tree = ET.parse(self.xml_file)
			root = tree.getroot()
			#get version id
			item_version = xmldoc.getElementsByTagName("version") 
			if not item_version:
				version_vl = ""
			else:
				#get version node value
				version_vl = item_version[0].firstChild.nodeValue
			#check if snapshot is present in version tag	
			if 'SNAPSHOT' in version_vl:
				try:
					#call check_tag function
					chk_tag_vl = self.check_tag()
					print(chk_tag_vl)
					print("Sucess!!! Valid Xml File")
					for elem in root.getiterator():
						try:
							elem.text = elem.text.replace(version_vl, chk_tag_vl)
							tree.write('outputs_main.xml',  xml_declaration = True,encoding = 'utf-8',method = 'xml')
						except AttributeError:
							pass
				except etree.XMLSchemaError:
					print(XMLSchemaError)
			else:
				print("")
					
	def check_tag(self):
		xmldoc = minidom.parse(self.xml_file)
		#get tags if present in file
		item_artifactId = xmldoc.getElementsByTagName("artifactId") 
		item_groupid = xmldoc.getElementsByTagName("groupId") 
		valid_vl = "No tag found"
		#check if tag present groupid
		if not item_groupid:
			groupid_val = ""
		else:
			groupid_val = item_groupid[0].firstChild.nodeValue
		#check if tag present artifactId
		if not item_artifactId:
			artifactId_val = ""
		else:
			artifactId_val = item_artifactId[0].firstChild.nodeValue
		
		val_nm = "ci_"+groupid_val+"_"+artifactId_val+"-SNAPSHOT"
		return val_nm
			
				
# create a new object                                            
ob = Xmlcheck()

ob.valid_xml()