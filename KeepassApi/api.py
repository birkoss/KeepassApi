from tastypie.resources import Resource
from tastypie import fields

#from KeepassReader.main import OpenKdbx

import xml.etree.ElementTree as ET

class KeepassEntry(object):
	def __init__(self, pk=None, name=None, username=None, password=None):
		self.pk = pk
		self.name = name
		self.username = username
		self.password = password

class KeepassResource(Resource):
	username = fields.CharField(attribute='username')
	name = fields.CharField(attribute='name')
	password = fields.CharField(attribute='password')

	class Meta:
		resource_name = "keepass"
		
	def obj_get_list(self, bundle, **kwargs):
		entries = []

#		xml = OpenKdbx('../../keepass2.kdbx', bundle.request.GET['password'])

		#entries.append( KeepassEntry(e['Pk'], e['Title'], e['UserName'], e['Password']))

		return entries
