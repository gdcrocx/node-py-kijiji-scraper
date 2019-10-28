'''
    kijijiDeduplication.py removes the duplicates in the Kijiji Ads that are extracted from the KijijiWeeder python script based on matching or similar attributes like title.

    Use after kijijiWeeder.py

    Credits - @gdcrocx
'''

import traceback
import json
import copy
import datetime

date = datetime.date.today()

f = open('./' + str(date) + '-kijiji-normal-ads.json', 'r')
jsonObject = json.loads(f.read())
f.close()

print(str(len(jsonObject)))

newList = []
uniqueList = []

try:

    for jsonObj in jsonObject:

        tempObj = copy.deepcopy(jsonObj)
        tempObj["images"] = []
        tempObj["image"] = ""
        tempObj["url"] = ""
        tempObj["date"] = ""
        if "attributes" in tempObj.keys() and "visits" in tempObj["attributes"].keys():
            tempObj["attributes"]["visits"] = 0
        # print(str(tempObj))
        newList.append(tempObj)

    print(str(len(newList)))
    
    for tempObj in newList:

        # print(str(tempObj))
        if tempObj not in uniqueList:

            uniqueList.append(tempObj)

    print(str(len(uniqueList)))
    # print(str(uniqueList))

    for uniqueItem in uniqueList:

        for jsonObj in jsonObject:

            if uniqueItem["title"] == jsonObj["title"]:
                
                uniqueList[uniqueList.index(uniqueItem)]["url"] = jsonObj["url"]
                uniqueList[uniqueList.index(uniqueItem)]["image"] = jsonObj["image"]
                uniqueList[uniqueList.index(uniqueItem)]["images"] = jsonObj["images"]
                uniqueList[uniqueList.index(uniqueItem)]["date"] = jsonObj["date"]     
                if "attributes" in uniqueList[uniqueList.index(uniqueItem)].keys() and "visits" in uniqueList[uniqueList.index(uniqueItem)]["attributes"].keys() and "attributes" in jsonObj.keys() and "visits" in jsonObj["attributes"].keys(): 
                    uniqueList[uniqueList.index(uniqueItem)]["attributes"]["visits"] = jsonObj["attributes"]["visits"]
                    # print(str(jsonObj["attributes"]["visits"]))
                    # print(str(uniqueList[uniqueList.index(uniqueItem)]["attributes"]["visits"]))

    print(str(len(uniqueList)))

    f = open('./' + str(date) + '-kijiji-normal-ads-unique.json', 'w', encoding="utf8")
    f.write(json.dumps(uniqueList))
    f.close()

except Exception:

    print("Errored out" + str(traceback.format_exc()))

