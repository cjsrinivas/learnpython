import os

def openFile(filename, mode):
	f = open(filename,mode)
	return f

def writeFile(f, str):
	f.write(str)

def closeFile(f):
	f.close()

def deleteFile(filePath):
	os.remove(filePath)