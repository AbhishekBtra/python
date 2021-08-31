from mmap import ACCESS_WRITE, mmap
import os

def create_sample_file():
    size = 1000000
    with open('file io/write/binary_file','wb') as f: #create a sample binary file
        f.seek(size-1)
        f .write(b'\x00')

def memory_map(filepath,access=ACCESS_WRITE):
    size = os.path.getsize(filepath)
    fd = os.open(filepath,os.O_RDWR)
    return mmap(fd,size,access=access)

if not os.path.exists('file io/write/binary_file'):
    create_sample_file()

m = memory_map('file io/write/binary_file')
print(len(m)) #1000000
print(m[0:10]) #b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'