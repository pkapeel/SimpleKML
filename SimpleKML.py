# CREATE A COPY OF THE .KML FILE WHICH IS TO BE USED
import shutil
import re

try:
    kmlFile = input('Enter Name of .KML File: ')
    SimpleKML = kmlFile.split('.')[0] + '_Simple.kml'
    TrashTXT = kmlFile.split('.')[0] + '_Trash.txt'
except:
    print(kmlFile, 'Does Not Exist')

# READ THE NEW COPIED FILE ONE LINE AT A TIME
fin = open(kmlFile, 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'Lines Read')
fout1 = open(SimpleKML, 'wt')
fout2 = open(TrashTXT, 'wt')

# CREATE A LIST OF OBJECTS TO KEEP
keep = ['<kml', 
        'kml>', 
        'xml ', 
        #'Document',    # CAUSES ERROR!
        'name', 
        'Style', 
        'Folder', 
        'Placemark', 
        'Point', 
        'coordinates', 
        'styleUrl', 
        'color>', 
        'LineStyle', 
        'width>', 
        'LineString',
        'scale',
        'MultiGeometry',
        'Polygon',
        'outerBoundaryIs',
        'LinearRing',
        # VERIFIED THE ABOVE WORKED ON TRACCAR SERVER
        'innerBoundaryIs',
        'href',
        'Icon',
        #'open',    # CAUSES ERROR!
        'Snippet',
        'description',
        'head',
        'META',
        'meta',
        'body',
        'table',
        'tr',
        'td',
        '-96']  # NOT SO ELEGANT WAY TO KEEP LINES WITH ONLY NORTHING/EASTING NUMBERS

# DELETE LINES THAT DO NOT CONTAIN KEYWORDS TO KEEP
i = 0
while i < len(lines):
    #print('Checking Line: ', line[i])
    for key in keep:
        #print('Searching for: ', key)
        m = re.search(key, lines[i])
        #print(m)
        if m:
            fout1.write(lines[i])
            #print('Wrote to File: ', line[i])
            i += 1
            break
        elif key == keep[-1]:
            #print('Line Removed: ', lines[i])
            fout2.write(lines[i])
            del lines[i]

# WRITE THE NEW FILE
fout1.close()
fout2.close()
print(len(lines), 'Lines Remaining')