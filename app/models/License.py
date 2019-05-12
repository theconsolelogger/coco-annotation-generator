class License:
	def __init__(self, id, name, url):
		self.id = id
		self.name = name
		self.url = url

	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def getUrl(self):
		return self.url

	def toJson(self):
		return {
			'id': self.id,
			'name': self.name,
			'url': self.url
		}
