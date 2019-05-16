# COCO Annotation Generator
Create annotations that follow the [COCO format](http://cocodataset.org) for a set of images.

## Quick start
From the root of the project run the following command:

python3 app

## Data
The data folder (/app/data) contains the images from which annotations will be generated. Place any folders, containing images, that you annotations to be generated for in this folder.

The expected structure for folders in the data folder is the following:
- Super category folder
  - Category folder
    - Image files

## Output
The annotations for the folders in the data folder will be placed in a file called
'instance_train.json' in the output folder (/app/output).
