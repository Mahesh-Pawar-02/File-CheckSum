# Problem Statements : Design automation script which accept diectory name and display checksum of all files.

# Usage : DirectoryChecksum.py "Demo"
 
import sys
import os
import hashlib

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DisplayChecksum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    
    exists = os.path.isdir(path)

    if exists:
        for DirName, SubDir, fileList in os.walk(path):
            print('\n-------------------------------------------------------------------')
            print("Current folder is : "+DirName,"\n")

            for filen in fileList:
                path = os.path.join(DirName,filen)
                FileHash = hashfile(path)
                print(path)
                print("Checksum of file : ",FileHash)
                print(" ")
    else:
        print("Invalid path...")

def main():
    print('-------------------------------------------------------------------')
    print("Created by Mahesh Pawar")
    print("Application name:" +sys.argv[0])
    print('-------------------------------------------------------------------')

if (len(sys.argv) != 2):
    print("Error: Invalid number of arguments")
    exit()

if (sys.argv[1] == "-h") or (sys.argv[1] == "-H"):
    print("This Script is used to traverse specific directory and display checksum of files")
    exit()

if (sys.argv[1] == "-u") or (sys.argv[1] == "-U"): 
    print("usage: ApplicationName AbsolutePath_of_Directory ")
    exit()

try:
    arr = DisplayChecksum(sys.argv [1])

except ValueError:
    print("Error: Invalid datatype of input")

except Exception as E:
    print("Error: Invalid input",E)

if __name__ =="__main__":
    main()