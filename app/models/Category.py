class Category:
	
	def __init__(self, category_id, name, supercategory):
		self.category_id = category_id
		self.name = name
		self.supercategory = supercategory

	def getCategoryId(self):
		return self.category_id
	
	def getName(self):
		return self.name

	def getSuperCategory(self):
		return self.supercategory
	
	def toJson(self):
		return {
			'id': self.category_id,
			'name': self.name,
			'supercategory': self.supercategory,
		}
