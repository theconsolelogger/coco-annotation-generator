class SegmentInfo:

	def __init__(self, segment_id, category_id, area, bbox, iscrowd):
		self.segment_id = segment_id
		self.category_id = category_id
		self.area = area
		self.bbox = bbox
		self.iscrowd = iscrowd

	def getSegmentId(self):
		return self.segment_id

	def getCategoryId(self):
		return self.category_id
	
	def getArea(self):
		return self.area
	
	def getBbox(self):
		return self.bbox

	def getIsCrowd(self):
		return self.iscrowd

	def toJson(self):
		return {
			'id': self.segment_id
			'category_id': self.category_id
			'area': self.area
			'bbox': self.bbox
			'iscrowd': self.iscrowd
		}
