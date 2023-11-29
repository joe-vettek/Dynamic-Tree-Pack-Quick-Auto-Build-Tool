# utlSimple/File.Getter.py
import inspect
import os

__all__ = ['getAllTextInFile', 'readDir']

import shutil


def getAllTextInFileWithSeek(path, seekPos):
    with open(path, "r", encoding="utf-8") as f:
        if seekPos > 0:
            f.seek(seekPos)
        allText = f.read()
        f.close()
        return allText


def getAllTextInFile(path):
    return getAllTextInFileWithSeek(path, 0)


def saveText(path,textC):
    with open(path, "w", encoding="utf-8") as f:
        f.write(textC)



def readDir(dirPath):
    allFiles = []
    __readDir__(dirPath, allFiles)
    return allFiles


def __readDir__(dirPath, allFiles):
    if len(dirPath) == 0:
        print(u'empty path')
        return
    if dirPath[-1] == '/':
        print(u'Not end with /')
        return
    if os.path.isdir(dirPath):
        fileList = os.listdir(dirPath)
        for f in fileList:
            __readDir__(dirPath + "\\" + f, allFiles)
            # allFiles.append(f)
        return
    else:
        allFiles.append(dirPath)


def getFileNameFromPath(path):
    return os.path.splitext(os.path.basename(path))[0]


def getFileTypeFromPath(path):
    return os.path.splitext(os.path.basename(path))[1]


def getFileParentPathFromPath(path):
    return os.path.split(path)[0]


def mycopyfile(srcfile, dstpath):
    print("Now Copy",srcfile,dstpath)
    if not os.path.exists(srcfile):
        return "%s not exist!" % (srcfile+dstpath)
    else:
        shutil.copy(srcfile, dstpath)
        return ""



def getRoot():
    return os.getcwd()

def join(parent,child):
    return os.path.join(parent,child)

def getCacheDirPath():
    return os.path.join(getRoot(),"cache")

def getOutputDirPath():
    return os.path.join(getRoot(),"output")


def getDriveLetter():
    return os.getcwd()[:1] + ":"

def initDir():
    if not os.path.exists(getCacheDirPath()):
        os.makedirs(getCacheDirPath())

def createDir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def find_variable_name(value):
    frame=inspect.currentframe()
    try:
        for varname, varvalue in frame.f_back.f_locals.items():
            if varvalue is value:
                return varname
    finally:
        del frame