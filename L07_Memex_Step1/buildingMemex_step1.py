#import libraries
import yaml
import re
import os
import shutil
##########################################################################

settingsFile = "Memex_config.yml"
settings = yaml.safe_load(open(settingsFile))
bibKeys = yaml.safe_load(open("zotero_biblatex_keys.yml"))

def bibLoad(bibTexFile):

    bibDic = {}

    with open(bibTexFile, "r", encoding="utf8") as f1:
        records = f1.read().split("\n@")

        for record in records[1:]:
            # let process ONLY those records that have PDFs
            if ".pdf" in record.lower():

                record = record.strip().split("\n")[:-1]

                rType = record[0].split("{")[0].strip()
                rCite = record[0].split("{")[1].strip().replace(",", "")

                bibDic[rCite] = {}
                bibDic[rCite]["rCite"] = rCite
                bibDic[rCite]["rType"] = rType

                for r in record[1:]:
                    key = r.split("=")[0].strip()
                    val = r.split("=")[1].strip()
                    val = re.sub("^\{|\},?", "", val)

                    fixedKey = bibKeys[key]

                    bibDic[rCite][fixedKey] = val

    return(bibDic)

memex_data = bibLoad(settings["bib_all"]) 

#generate folders
start_path = "/home/lisnux/Desktop/UniWien/WS2021/070172_UEMethodologicalCourse/hw070172/MEMEX_SANDBOX/data"

folder_names = list(memex_data.keys())

for f in folder_names:
	folder1 = f[0]
	path1 = os.path.join(start_path, folder1) 
	if not os.path.exists(path1):
		os.makedirs(path1)
	folder2 = f[0]+f[1]
	path2 = os.path.join(path1, folder2)
	if not os.path.exists(path2):
		os.makedirs(path2)
	folder3 = f
	path3 = os.path.join(path2, folder3)
	if not os.path.exists(path3):
		os.makedirs(path3)

#copy PDF files

#source folder unclear -- unfortunately I don't know where the PDFs are

#if not os.path.isfile(dst):
#  shutil.copyfile(src, dst)





