try:
	import chardet
except ImportError:
	chardet = None

if chardet:
	print("chardet exists")
else:
	print("no it doesn't")

try:
	from lxml import etree
except ImportError:
	import xml.etree.ElementTree as etree

