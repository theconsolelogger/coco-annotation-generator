class Coco:

	def __init__(self):
		self.info = {}
		self.licenses = []
		self.images = []
		self.annotations = []
		self.categories = []

	def setInfo(self, info):
		self.info = info

	def addLicense(self, license):
		self.licenses.append(license)
	
	def addImage(self, image):
		self.images.append(image)

	def addAnnotation(self, annotation):
		self.annotations.append(annotation)

	def addCategory(self, category):
		self.categories.append(category)

	def toJson(self):
		annotations = []
		categories = []
		licenses = []
		images = []

		# Convert images to JSON
		for image in self.images:
			images.append(image.toJson())

		# Convert licenses to Json
		for license in self.licenses:
			licenses.append(license.toJson())

		# Convert annotations
		for annotation in self.annotations:
			annotations.append(annotation.toJson())

		# Convert categories
		for category in self.categories:
				categories.append(category.toJson())
		
		return {
			'info': self.info.toJson(),
			'licenses': licenses,
			'images': images,
			'annotations': annotations,
			'categories': categories 
		}
