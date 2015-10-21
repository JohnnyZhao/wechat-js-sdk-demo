import xml.etree.ElementTree as ET

def parse_xml(string):
    from_user = content = None
    root = ET.fromstring(string)
    print root.tag
    print root.attrib
    for child in root:
	if child.tag == 'FromUserName':
	    from_user = child.text
	if child.tag == 'Content':
	    content = child.text
    print from_user, content
    return from_user, content
