from lxml import etree
import xml.etree.ElementTree as ET
from xml.dom import minidom

class Xmlcheck():
	xml_file = "pom.xml"
	srch_var = "version"
	pr_key = "ci_"
	su_key = "SNAPSHOT"
	nspace = "http://maven.apache.org/POM/4.0.0"
	
	def valid_xml(self):
		xml_files = self.xml_file
		with open(xml_files, 'r') as xml_file:
			xml_data = xml_file.read()
			xmldoc = minidom.parse(self.xml_file)
			tree = ET.parse(self.xml_file)
			root = tree.getroot()
			item_version = xmldoc.getElementsByTagName(self.srch_var) 
			#call check_tag function
			try:
				etree.fromstring(xml_data)
				print("Success!!! Valid Xml File")
				#chk snapshot
				if item_version:
					#get version node value
					version_vl = item_version[0].firstChild.nodeValue
					#check if snapshot is present in version tag	
					if 'SNAPSHOT' in version_vl:
						try:
							print("Output string created")
							#update POM file
							self.update_xmlVer( version_vl )
							print("Version Updated")
						except etree.XMLSchemaError:
							print(XMLSchemaError)
					else:
						print("SNAPSHOT missing")
				else:
					version_vl = ""
					print("Version missing")
			except etree.XMLSchemaError:
							print(XMLSchemaError)		

	#modify xml file
	def update_xmlVer( self, version_vl ):
		ET.register_namespace('', self.nspace)
		xml_files = self.xml_file
		chk_tag_vl = self.check_tag()
		tree = ET.parse(self.xml_file)
		root = tree.getroot()
		for elem in root.getiterator():
			try:
				elem.text = elem.text.replace(version_vl, chk_tag_vl)
				tree.write(self.xml_file,  xml_declaration = True,encoding = 'utf-8',method = 'xml')
			except AttributeError:
				pass
		
	
	def check_tag(self):
		xmldoc = minidom.parse(self.xml_file)
		#get tags if present in file
		branch_name = xmldoc.getElementsByTagName("artifactId") 
		org_name = xmldoc.getElementsByTagName("groupId") 
		#check if tag present groupid
		if not org_name:
			org_val = ""
		else:
			org_val = org_name[0].firstChild.nodeValue
		#check if tag present artifactId
		if not branch_name:
			branch_val = ""
		else:
			branch_val = branch_name[0].firstChild.nodeValue
		
		val_nm = self.pr_key+org_val+"_"+branch_val+"-"+self.su_key
		return val_nm
# create a new object                                            
ob = Xmlcheck()

ob.valid_xml()