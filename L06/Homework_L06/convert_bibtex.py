#This program converts a biblatex file to another format

#create dic
bibDic = {}

#read file as string
with open ("zotero_biblatex_sample.bib", "r") as myfile:
    records=myfile.read()
    #split records
    records = records.split('\n@')

#for r in records:
#	recordList = r.split(',\n')
input(records)

#import json
#import yaml
