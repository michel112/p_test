from lxml import etree
import unittest
import xml.etree.ElementTree as ET
from xml.dom import minidom

class TestStringMethods(unittest.TestCase):
	xml_file = "pom.xml"
	xml_file_valid = "valid.xml"
	xml_file_invalid = "invalid_pom.xml"
	org_name = "kbiz"
	brn_name = "test"
	
	def test_valid_xml(self):
		print("valid")
		ET.register_namespace('', "http://maven.apache.org/POM/4.0.0")
		xml_files = self.xml_file
		xml_inv = self.xml_file_valid
		tree = ET.parse(self.xml_file_valid)
		root = tree.getroot()
		xmldoc = minidom.parse(self.xml_file_valid)
		item_version = xmldoc.getElementsByTagName("version")
		if not item_version:
			version_vl = ""
		else:
			#get version node value
			version_vl = item_version[0].firstChild.nodeValue
		with open(xml_files, 'r') as xml_file:
			xml_data = xml_file.read()
		with open(xml_inv, 'r') as xml_invs:
			xml_data_inv = xml_invs.read()
			#call check_tag function
			chk_tag_vl = self.check_tag()
			if 'SNAPSHOT' in version_vl:
				try:
					#call check_tag function
					chk_tag_vl = self.check_tag()
					print(chk_tag_vl)
					for elem in root.getiterator():
						try:
							elem.text = elem.text.replace(version_vl, chk_tag_vl)
							#create new xml file for result
							tree.write('output_valid.xml',  xml_declaration = True,encoding = 'utf-8',method = 'xml')
							#use of Unittest case
							self.assertEqual(xml_data_inv,xml_data)
						except AttributeError:
							pass
					print("Sucess!!! Valid Xml File")
				except etree.XMLSchemaError:
					print(XMLSchemaError)
				
			
	def test_invalid_xml(self):
		ET.register_namespace('', "http://maven.apache.org/POM/4.0.0")
		xml_files = self.xml_file
		xml_inv = self.xml_file_invalid
		
		with open(xml_files, 'r') as xml_file:
			xml_data = xml_file.read()
		with open(xml_inv, 'r') as xml_invs:
			xml_data_inv = xml_invs.read()
			#call check_tag function
			chk_tag_vl = self.check_tag()
			xmldoc = minidom.parse(self.xml_file_valid)
			#get version by id
			item_version = xmldoc.getElementsByTagName("version")
			if not item_version:
				version_vl = ""
			else:
				#get version node value
				version_vl = item_version[0].firstChild.nodeValue
			print(chk_tag_vl)
			if 'SNAPSHOT' in version_vl:
				self.assertEqual(xml_data_inv,xml_data)
			else:
				print("Snapshot not found in version tag")
			
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
if __name__ == '__main__':
    unittest.main()