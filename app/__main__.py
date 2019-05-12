from datetime import datetime
from PIL import Image
import json
import os
from models.Image import Image as CocoImage
from models.Info import Info
from models.License import License

def main():
	currentDateTime = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
	info = Info(2019, '1.0.0', 'COCO format', 'Jon', '', currentDateTime)
	copyrightedLicense = License(1, 'Copyrighted', '')
	rootFolder = os.getcwd() + '/app/data'
	images = []
	
	# Go through every folder found in /data folder (including symlink)
	for dirpath, dirs, files in os.walk(rootFolder, True, None, True):
		for folder in dirs:

			# Go through every file in the folders and covnert to objects
			for folderPath, folderDirs, folderFiles in os.walk(os.path.join(rootFolder,folder)):
				for fileName in folderFiles:
					splitFileName = fileName.split('.', 1)[0]

					# Remove thumb nail files
					if (splitFileName == 'SYNOFILE_THUMB_M'):
						continue

					# Extract id from file name
					fileId = int(splitFileName)

					image = Image.open(os.path.join(folderPath, fileName))
					width, height = image.size
					cocoImage = CocoImage(fileId, width, height, fileName, copyrightedLicense.getId(), currentDateTime)
				
					images.append(cocoImage)
	output(info, copyrightedLicense, images)

def output(info, license, images):
	jsonImages = []

	for image in images:
		jsonImages.append(image.toJson())

	output = {
		'info': info.toJson(),
		'licenses': license.toJson(),
		'images': jsonImages
	}

	with open(os.getcwd() + '/app/output/annotation.txt', 'w') as outputFile:
		stringOutput = json.dumps(output)
		print(stringOutput)
		outputFile.write(stringOutput)

if __name__ == "__main__":
	main()
