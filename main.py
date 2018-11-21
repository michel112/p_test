from lxml import etree
class Xmlcheck():
	xml_file = "pom.xml"
	
	def valid_xml(self):
		xml_files = self.xml_file
		with open(xml_files, 'r') as xml_file:
			xml_data = xml_file.read()
			try:
				etree.fromstring(xml_data)
				print("Sucess!!! Valid Xml File")
			except etree.XMLSchemaError:
				print(XMLSchemaError)
				
# create a new object                                            
ob = Xmlcheck()

ob.valid_xml()