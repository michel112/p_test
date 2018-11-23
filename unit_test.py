from lxml import etree
import unittest
import xml.etree.ElementTree as ET
from xml.dom import minidom

class TestStringMethods(unittest.TestCase):
	xml_file = "pom.xml"
	xml_file_valid = "valid.xml"
	xml_file_invalid = "invalid_pom.xml"
	
	def test_valid_xml(self):
		xml_files = self.xml_file
		xml_inv = self.xml_file_valid
		
		with open(xml_files, 'r') as xml_file:
			xml_data = xml_file.read()
		with open(xml_inv, 'r') as xml_invs:
			xml_data_inv = xml_invs.read()
			#call check_tag function
			chk_tag_vl = self.check_tag()
			print(chk_tag_vl)
			if chk_tag_vl == "tag_found":
				self.assertEqual(xml_data_inv,xml_data)
			
	def test_invalid_xml(self):
		xml_files = self.xml_file
		xml_inv = self.xml_file_invalid
		
		with open(xml_files, 'r') as xml_file:
			xml_data = xml_file.read()
		with open(xml_inv, 'r') as xml_invs:
			xml_data_inv = xml_invs.read()
			#call check_tag function
			chk_tag_vl = self.check_tag()
			print(chk_tag_vl)
			if chk_tag_vl == "tag_found":
				self.assertEqual(xml_data_inv,xml_data)
			
	def check_tag(self):
		xml_files = self.xml_file
		#val_nm = "ci_"+self.org_name+"_"+self.brn_name+"-SNAPSHOT"
		xmldoc = minidom.parse(self.xml_file)
		itemlist = xmldoc.getElementsByTagName("version") 
		if not itemlist:
			valid_vl = "No tag found"
			return valid_vl
		else:
			tag_val = itemlist[0].firstChild.nodeValue
			valid_vl = "tag_found"
			return valid_vl			
	
	def test_snap(self):
		xml_files = self.xml_file
		#val_nm = "ci_"+self.org_name+"_"+self.brn_name+"-SNAPSHOT"
		xmldoc = minidom.parse(self.xml_file)
		item_version = xmldoc.getElementsByTagName("version") 
		version_vl = item_version[0].firstChild.nodeValue
		if 'SNAPSHOT' in version_vl:
			self.assertTrue('SNAPSHOT is present')
		else:
			self.assertFalse('SNAPSHOT not present')
       

# create a new object                                            
if __name__ == '__main__':
    unittest.main()