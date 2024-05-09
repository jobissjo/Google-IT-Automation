#!/usr/bin/env py
import os
import datetime

with open('managing_file.txt', 'w') as file:
    file.write("Hello how are you???")

print(os.path.exists('managing_file.txt'))

os.remove('managing_files.txt')
os.rename('managing_file.txt', 'managing_files.txt')

print(os.path.getsize('managing_files.txt'))

timestamp = os.path.getmtime('managing_files.txt')

print(datetime.datetime.fromtimestamp(timestamp))

print(os.path.abspath('managing_files.txt'))

############################################

print(os.getcwd())

os.makedirs("Jobi_dummy", exist_ok=True)

os.chdir("Jobi_dummy")
with open('myfile.txt', 'w') as file:
    file.write("I am not going to do that")

with open("my_file_2.txt", 'w') as file:
    file.write("this is my second file")

os.mkdir("newer_dir")
os.rmdir('newer_dir')
print(os.getcwd())

os.chdir("..")
dirname = 'Jobi_dummy'
for name in os.listdir(dirname):
    fullname = os.path.join(dirname, name)

    if(os.path.isdir(fullname)):
        print(f"'{fullname}' is a directory")
    else:
        print(f"'{fullname}' is a file")

from pathlib import Path

dest_dir = Path(dirname)

if not dest_dir.exists():
    dest_dir.mkdir()

src_file = Path('./sample_data/README.md')
des_file = dest_dir/ 'README.md'


src_file.rename(des_file)