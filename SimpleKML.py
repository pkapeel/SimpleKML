# CREATE A COPY OF THE .KML FILE WHICH IS TO BE USED
import shutil

try:
    kmlFile = input('Enter Name of .KML File: ')
    SimpleKML = kmlFile.split('.')[0] + '_Simple.kml'
    shutil.copy(kmlFile, SimpleKML)
except:
    print(kmlFile, 'Does Not Exist')

# READ THE NEW COPIED FILE ONE LINE AT A TIME

fin = open(SimpleKML, 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'Lines Read')

# CREATE A LIST OF OBJECTS TO KEEP

keep = ['xml', 'kml', 'Document', 'name', 'Style', 'Folder', 'Placemark', 
        'Point', 'coordinates', 'styleURL', 'color', 'LineStyle', 'width', 'LineString']

# DELETE LINES THAT DO NOT CONTAIN OBJECTS TO KEEP

for line in lines:
    for feature in keep:
        if 