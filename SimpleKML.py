# keep the typical xml heading information
# read the file line by line
# determine which lines to delete and which lines to keep

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
print(lines[0])

