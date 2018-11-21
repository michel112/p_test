from lxml import etree
import unittest

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
			self.assertEqual(xml_data_inv,xml_data)
			
	def test_invalid_xml(self):
		xml_files = self.xml_file
		xml_inv = self.xml_file_invalid
		
		with open(xml_files, 'r') as xml_file:
			xml_data = xml_file.read()
		with open(xml_inv, 'r') as xml_invs:
			xml_data_inv = xml_invs.read()
			self.assertEqual(xml_data_inv,xml_data)
			
				
# create a new object                                            
if __name__ == '__main__':
    unittest.main()