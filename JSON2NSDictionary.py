

import json,sys,getopt
from collections import OrderedDict

Tab = 4*' '
Tab = '\t'

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          sys.exit()
       elif opt in ("-i", "--ifile"):
          inputfile = arg

    # inputfile = '/Users/didi/Desktop/ONEAppConfig.json'
    fopen = open(inputfile, 'r')
    objs = json.load(fopen, object_pairs_hook=OrderedDict)
    lines = translate(objs).split('\n')

    hierarchy = 0
    for line in lines:
        if '},' in line or '],' in line:
            hierarchy -= 1
        print hierarchy*Tab + line
        if '@{' in line or '@[' in line:
            hierarchy += 1

def translate(obj):
    tempStr = ''
    if isinstance(obj, dict):
        tempStr += '@{'
        for key, value in obj.iteritems():
            tempStr += '\n'
            tempStr += translate(key)
            tempStr += ' : '
            tempStr += translate(value)
            tempStr += ','
        tempStr += '\n}'

    elif isinstance(obj, list):
        tempStr += '@['
        for item in obj:
            tempStr += '\n'
            tempStr += translate(item)
            tempStr += ','
        tempStr += '\n]'

    elif isinstance(obj, str):
        tempStr += '@"'
        tempStr += obj
        tempStr += '"'

    elif isinstance(obj, unicode):
        tempStr = translate(obj.encode("utf-8"))

    elif isinstance(obj, int) or isinstance(obj, float):
        tempStr += '@('
        tempStr += str(obj)
        tempStr += ')'

    else:
        sys.exit()
    return tempStr


if __name__ == '__main__':
    main(sys.argv[1:])
