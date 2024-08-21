#!/usr/bin/python
import sys

try:
    filename = sys.argv[1]
except IndexError:
    print("No file provided.")
    sys.exit()

dds = open(filename, "r+b")
header = dds.read(3)
print(str(header))
if str(header) == "b\'DDS\'":
    print("Valid DDS header found.")
else:
    sys.exit() 

if 'd5comp' in filename:
    print("Assuming file is compressed with DXT5 / BC3_UNorm.")
    dds.seek(8, 0)
    dds.write(b'\x07\x10\x00\x00')
    dds.seek(20, 0)
    dds.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x00\x00\x00\x04\x00\x00\x00\x44\x58\x54\x35\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
elif 'nocomp' in filename:
    print("Assuming file is uncompressed.")
    dds.seek(8, 0)
    dds.write(b'\x07\x10\x00\x00')
    dds.seek(20, 0)
    dds.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x00\x00\x00\x41\x00\x00\x00\x00\x00\x00\x00\x20\x00\x00\x00\x00\x00\xFF\x00\x00\xFF\x00\x00\xFF\x00\x00\x00\x00\x00\x00\xFF\x02\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
else:
    print("Did not find compression method in filename. Please ensure your file is named correctly.")
    sys.exit()