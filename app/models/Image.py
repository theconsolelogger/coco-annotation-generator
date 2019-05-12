class Image:
	def __init__(self, id, width, height, file_name, license, date_captured):
		self.id = id
		self.width = width
		self.height = height
		self.file_name = file_name
		self.license = license
		self.flickr_url = ''
		self.coco_url = ''
		self.date_captured = date_captured

	def getId(self):
		return self.id

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def getFileName(self):
		return self.file_name

	def getLicense(self):
		return self.license

	def getFlickrUrl(self):
		return self.flickr_url

	def getCocoUrl(self):
		return self.coco_url

	def getDateCaptured(self):
		return self.date_captured

	def toJson(self):
		return {
			'id': self.id,
			'width': self.width,
			'height': self.height,
			'file_name': self.file_name,
			'license': self.license,
			'flickr_url': self.flickr_url,
			'coco_url': self.coco_url,
			'date_captured': self.date_captured
		}
