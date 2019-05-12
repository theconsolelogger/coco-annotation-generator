class Info:
	def __init__(self, year, version, description, contributor, url, date_created):
		self.year = year
		self.version = version
		self.description = description
		self.contributor = contributor
		self.url = url
		self.date_created = date_created

	def getYear(self):
		return self.year

	def getVersion(self):
		return self.version

	def getDescription(self):
		return self.description

	def getContributor(self):
		return self.contributor

	def getUrl(self):
		return self.url

	def getDateCreated(self):
		return self.date_created
	
	def toJson(self):
		return {
			'year': self.year,
			'version': self.version,
			'description': self.description,
			'contributor': self.contributor,
			'url': self.url,
			'date_created': self.date_created
		}
