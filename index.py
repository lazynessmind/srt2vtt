import sys
import re
from pathlib import Path

def convertType(srtFile):
    subtitlefile = open(srtFile, "r",  encoding='utf8')
    convertedFile = open(Path(srtFile).stem + '.vtt', "w",  encoding='utf8')

    lineArray = subtitlefile.read().splitlines()    
    
    convertedFile.write('WEBVTT\n\n')

    i = 1
    while i < len(lineArray):
        if not lineArray[i].isdigit():
            convline = re.sub(',(?! )', '.', lineArray[i])
            convertedFile.write(convline + '\n')
        i += 1
    convertedFile.close()

if __name__ == '__main__':
    convertType(sys.argv[1])