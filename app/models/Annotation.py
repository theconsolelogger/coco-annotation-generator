class Annotation:

	def __init__(self, annotation_id, image_id, category_id, segmentation, area, bbox, iscrowd):
		self.annotation_id = annotation_id
		self.image_id = image_id
		self.category_id = category_id
		self.segmentation = segmentation
		self.area = area
		self.bbox = bbox
		self.iscrowd = iscrowd

	def getAnnotationId(self):
		return self.annotation_id

	def getImageId(self):
		return self.image_id

	def getCategoryId(self):
		return self.category_id

	def getSegmentation(self):
		return self.segmentation
	
	def getArea(self):
		return self.area

	def getBbox(self):
		return self.bbox

	def getIscrowd(self):
		return self.iscrowd

	def toJson(self):
		return {
			'id': self.annotation_id,
			'image_id': self.image_id,
			'category_id': self.category_id,
			'segmentation': self.segmentation,
			'area': self.area,
			'bbox': self.bbox,
			'iscrowd': self.iscrowd
		}
