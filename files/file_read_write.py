# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:51:25 2017

@author: Samar
"""
import os
import pandas as pd
from calendar import month_abbr
import pickle
import binascii
import io

shak = open('D:\\ufdata\\shakespeare.txt', 'r', encoding='utf-8')
print(type(shak))
print(shak.fileno())
counter = 0
# iterator implicitly calls readline
for line in shak:
    #if(line.strip() != ''):
    print(counter, line)
    counter += 1
    if counter == 20:
        break
shak.close()

shak2 = open('D:\\ufdata\\shakespeare.txt', 'r', encoding='utf-8')
print(shak2.tell())

# explicitly calling read line
for x in range(20):
    print(shak2.readline())
    print('position as given by tell: ', shak2.tell())

shak2.close()

# read lines into a list
shak_lines = open('D:\\ufdata\\shakespeare.txt', 'r',
                  encoding='utf-8').readlines()
print('No of lines in shakespeare.txt ', len(shak_lines))

# read a file as a binary stream
shak_bin = open('D:\\ufdata\\shakespeare.txt', 'rb')
print(shak_bin.tell())
for x in range(20):
    print(shak_bin.readline())
    print('position as given by tell: ', shak_bin.tell())

shak3 = open('D:\\ufdata\\shakespeare.txt', 'r', encoding='utf-8')
file_for_writing = open('D:\\ufdata\\shak_new.txt', 'w')
counter = 0
try:
    for line in shak3:
        if(line.strip() != ''):
            counter += 1
            file_for_writing.write('Line number ' + str(counter) + ': ')
            file_for_writing.write(line)
            if(counter == 20):
                file_for_writing.close()
                break
except Exception as exc:
    print('Exception occured ', exc)
finally:
    file_for_writing.close()
    shak3.close()

# open a binary file a jpgeg and check signature to identify

jpeg_signatures = [
    binascii.unhexlify(b'FFD8FFD8'),
    binascii.unhexlify(b'FFD8FFE0'),
    binascii.unhexlify(b'FFD8FFE1')
]

file_loc = 'D:/tmp/spyder.jpg'
binf = open(file_loc, 'rb')
first_four_bytes = binf.read(4)
print(first_four_bytes in jpeg_signatures)

second_binf = open(file_loc, 'rb')
print(binf == second_binf)
print(binf.read() == second_binf.read())
binf.close()
second_binf.close()

binf2 = open(file_loc, 'rb')
second_binf2 = open(file_loc, 'rb')
print(binf2.read() == second_binf2.read())
print(binf2)
binf2.close()
second_binf2.close()

# read a csv file using pandas
wine_df = pd.read_csv('D:\\ufdata\\winequality-red.csv', sep=';')
wine_df.head()
wine_df.iloc[:5, :]
wine_df_row1 = wine_df.loc[0]
print('fixed acidity ', wine_df_row1['fixed acidity'])
print('quality ', wine_df_row1.quality)

# read excel file using pandas
wine_xlsx = pd.read_excel('D:\\ufdata\\winequality-red.xlsx', 'dummy_data')
print(wine_xlsx)
print(len(wine_xlsx))


# read all sheets in excel file
xls_file = pd.ExcelFile('D:\\ufdata\\winequality-red.xlsx')
wines = xls_file.parse(0)
print(wines)
movies = xls_file.parse(1)
print(movies)

code_dir = os.path.join('/', 'Users', 'Samar', 'OneDrive', 'pycodes')
code_dir
os.listdir(code_dir)

exec(open('C:\\Users\\Samar\\OneDrive\\pycodes\\os_path_ex.py').read())

# serialization and deserialization - pickle module
mnames = [x for x in enumerate(month_abbr) if x[0] != 0]
print(mnames)
pickle.dump(mnames, open('D:\\ufdata\\mnames.p', 'wb'))
mnames_from_pickle = pickle.load(open('D:\\ufdata\\mnames.p', 'rb'))
print(mnames_from_pickle)
print(mnames == mnames_from_pickle)

# using StringIO to carry out ops in memory
# wwe have an api that accepts file objects
# and we'd like to pass it dynamically created inputs
# the stringio creates file-like objects that can
# be passed to existing api without distrubing it
output = io.StringIO()
for n in range(10):
    output.write('line ' + str(n) + '\n')
str_input_fm_output = io.StringIO(output.getvalue())
for line in str_input_fm_output.readlines():
    print(line)
