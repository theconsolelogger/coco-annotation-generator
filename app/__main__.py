from datetime import datetime
from PIL import Image
import json
import os
from models.Annotation import Annotation
from models.Category import Category
from models.Coco import Coco
from models.Image import Image as CocoImage
from models.Info import Info
from models.License import License

def main():
	currentDateTime = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
	rootFolder = os.getcwd() + '/app/data'
	annotationNumber = 1

	coco = Coco()

	info = Info(2019, '1.0.0', 'COCO format', 'Jon', '', currentDateTime)
	coco.setInfo(info)

	copyrightedLicense = License(1, 'Copyrighted', '')
	coco.addLicense(copyrightedLicense)

	# Go through every folder found in /data folder (including symlink)
	superCategoryFolders = os.listdir(rootFolder)

	for superCategory in superCategoryFolders:
		categoryFolders = os.listdir(os.path.join(rootFolder, superCategory))
		
		for categoryFolder in categoryFolders:
			# Filter unwanted folders
			if (not checkFolder(categoryFolder)):
				continue

			# Create category
			category_id = categoryFolder.split('_', 1)[0]
			category_name = categoryFolder.split('_', 1)[1]

			category = Category(category_id, category_name, superCategory)
			coco.addCategory(category)

			# Go through every file in the folders and covnert to objects
			imageFiles = os.listdir(os.path.join(rootFolder, superCategory, categoryFolder))

			for imageFile in imageFiles:
				# Filter unwanted files
				if (not checkFile(imageFile)):
					continue
				
				# Extract ID from file name
				fileId = int(imageFile.split('.', 1)[0])

				# Create image
				image = Image.open(os.path.join(rootFolder, superCategory, categoryFolder, imageFile))
				width, height = image.size

				cocoImage = CocoImage(fileId, width, height, imageFile,
				copyrightedLicense.getId(), currentDateTime)
				coco.addImage(cocoImage)

				# Create annotation for image
				annotation = Annotation(annotationNumber, cocoImage.getId(), category.getCategoryId(), [], 0.00, [0, 0, width, height], 0)
				coco.addAnnotation(annotation)
				annotationNumber += 1

	# Write output to file
	output(coco.toJson())

# Checks folder meets certain criteria
def checkFolder(folderName):
	if ('invalid' in folderName):
		return False

	return True

# Checks file meets certain criteria
def checkFile(fileName):
	if ('@' in fileName):
		return False

	splitFileName = fileName.split('.', 1)[0]

	if (splitFileName == 'SYNOFILE_THUMB_M'):
		return False
	
	return True

def output(text):
	with open(os.getcwd() + '/app/output/annotation.txt', 'w') as outputFile:
		stringOutput = json.dumps(text)
		outputFile.write(stringOutput)

if __name__ == "__main__":
	main()
