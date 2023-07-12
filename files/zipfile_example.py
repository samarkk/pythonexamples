# first create the directory structure for working with zipfile
'''
mkdir playground
cd playground
for x in {1..10};do echo "writing $x to file file$x" >file$x.txt;done
mkdir{dir1,dir2,dir3}
cp file{1..3}.txt dir1
cp file{4..6}.txt dir2
cp file{7..10}.txt dir1 
'''
import os
from zipfile import ZipFile
from datetime import datetime

# write the files in the directory to a zip archive
file_name = "D:/tmp/zipex.zip"
with ZipFile(file_name,'w') as zip:
    for root, directories, files in os.walk("D:/tmp/playground"):
        for file in files:
            filepath = os.path.join(root, file)
            basename, filename = os.path.split(filepath)
            print(filepath, basename, filename)
            zip.write(filepath)

#see the information about the contents of the zip file
with ZipFile(file_name, 'r') as zip:
    for info in zip.infolist():
            print(info.filename)
            print('\tModified:\t' + str(datetime(*info.date_time)))
            print('\tSystem:\t\t' + str(info.create_system) + '(0 = Windows, 3 = Unix)')
            print('\tZIP version:\t' + str(info.create_version))
            print('\tCompressed:\t' + str(info.compress_size) + ' bytes')
            print('\tUncompressed:\t' + str(info.file_size) + ' bytes')

# extract the zip
zip = ZipFile(file_name, 'r')

# see the structure
zip.printdir()

# make and change to a directory where the zip contents will be extracted
os.mkdir("D:/tmp/zipextr")
os.chdir("D:/tmp/zipextr")
os.getcwd()

# extract the zip conents and check
zip.extractall()
[file for file in os.walk(os.getcwd())]

# extract one file
open(zip.extract('tmp/playground/file1.txt')).readlines()

# use zip.read to extract the data of a specific file
zip.read('tmp/playground/file1.txt')