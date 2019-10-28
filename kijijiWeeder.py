'''
    kijijiWeeder.py removes Ads from the raw JSON file that has the following excludedWords in the Ad title or description. Works for a well refined search on Kijiji listings. Since this is a word exclusion technique, you could block any feature that you dont want to see in the resulting ads like "damaged", "damage", "broken" and so on...

    Run after NodeKijijiScraper.py

    Credits - @gdcrocx
'''

import json
import datetime

date = datetime.date.today()

f = open('./' + str(date) + '-kijiji-scraped-raw.json', 'r', encoding="utf8")
jsonObject = json.loads(f.read())
f.close()

excludedWords = ["women", "woman", "female", "lady", "ladies", "girl", "girls", "july", "august", "aug", "sept", "september"] # Looking for an apartment without female friends ;) and excluding any open places that are available between July and September
isExclude = 0

jsonExcludeAdsList = []
jsonExcludeAdsCounter = 0
jsonNormalAdsList = []
jsonNormalAdsCounter = 0

for jsonObj in jsonObject:    

    if jsonObj["attributes"]["type"] == "OFFER" and jsonObj["attributes"]["furnished"] == 1 and jsonObj["image"] != None:

        isExclude = 0
        for word in excludedWords:

            # print(str(type(jsonObj["title"])))

            if word in jsonObj["title"].lower() or word in jsonObj["description"].lower():

                isExclude = 1

        if isExclude == 1:

            if len(jsonExcludeAdsList) > 0:
            #    # print("\n"+str(jsonObj["title"]))
            #    for jsonExcludeItem in jsonExcludeAdsList:
            #        # print(str(jsonExcludeItem["title"]))
            #        # print(str(jsonObj["title"]))
            #        if str(jsonObj["title"]) != str(jsonExcludeItem["title"]):
                jsonExcludeAdsList.append(jsonObj)
                jsonExcludeAdsCounter += 1
            else:
                jsonExcludeAdsList.append(jsonObj)
                jsonExcludeAdsCounter += 1

        else:

            if len(jsonNormalAdsList) > 0:
            #    # print("\n"+str(jsonObj["title"]))
            #    for jsonNormalItem in jsonNormalAdsList:
            #        # print(str(jsonNormalItem["title"]))
            #        # print(str(jsonObj["title"]))
            #        if str(jsonObj["title"]) != str(jsonNormalItem["title"]):
                jsonNormalAdsList.append(jsonObj)
                jsonNormalAdsCounter += 1
            else:
                jsonNormalAdsList.append(jsonObj)
                jsonNormalAdsCounter += 1

            print("\nNormal Ads Counter - " + str(jsonNormalAdsCounter))
            print("\nExcluded Ads Counter - " + str(jsonExcludeAdsCounter))


fileExclude = open('./' + str(date) + '-kijiji-excluded-ads.json', 'w', encoding="utf8")
fileExclude.write(json.dumps(jsonExcludeAdsList))
fileExclude.close()

fileInclude = open('./' + str(date) + '-kijiji-normal-ads.json', 'w', encoding="utf8")
fileInclude.write(json.dumps(jsonNormalAdsList))
fileInclude.close()

print("\nNormal Ads - " + str(jsonNormalAdsCounter))
print("\nExcluded Ads - " + str(jsonExcludeAdsCounter))
