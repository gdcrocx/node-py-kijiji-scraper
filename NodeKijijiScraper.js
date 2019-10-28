// A Node.Js library from @mwpenny with some additions to write to file as a single huge JSON Ads Object
// The library parses Kijiji.ca for Ads that match the given params and returns a JSON file onto the filesystem for further Python processing.
// Refer to https://github.com/gdcrocx/kijiji-scraper/blob/master/README.md for improved documentation of the file.
// Credits - @mwpenny, @gdcrocx

const fs = require('fs');
var kijiji = require("kijiji-scraper")

let options = {
    minResults: 220,
    maxResults: -1
};

let params = {
    locationId: 1700273,
    categoryId: 36,
    maxPrice: 750, 
    radius: 10,
    address: "M5R1M3",
    adType: "OFFER",    
    hasImages: true,
    "attributeMap[furnished_s]": "[1]"
};

//// This will be the sample URL generated by the qs.stringify(params) function in the initFirstResultPagePath function on search.js
// https://www.kijiji.ca/b-search.html?locationId=1700273&categoryId=36&maxPrice=750&radius=7&address=M5R1M3&adType=OFFER&hasImages=true&attributeMap%5Bfurnished_s%5D=%5B1%5D&formSubmit=true&siteLocale=en_CA

let jsonArray = []

// Scrape using returned promise
kijiji.search(params, options).then(function (ads) {
    // Use the ads array
    for (let i = 0; i < ads.length; ++i) {
        console.log(JSON.stringify(ads[i]));
    }
}).catch(console.error);

// Scrape using optional callback parameter
function callback(err, ads) {
    if (!err) {
        // Use the ads array
        for (let i = 0; i < ads.length; ++i) {
            // console.log(JSON.stringify(ads[i]));
            jsonArray.push(ads[i]);
        }
    }
}

kijiji.search(params, options, callback).then(() => {
    // console.log(jsonArray.length);
    if (jsonArray.length > 0) {
        writeJsonFile(jsonArray);
    };
});

function writeJsonFile(jsonArray) {
    let dateObj = new Date();
    fs.writeFileSync("./" + dateObj.getFullYear() + "-" + (((dateObj.getMonth() + 1) < 10) ? '0' + (dateObj.getMonth() + 1) : (dateObj.getMonth() + 1)) + "-" + ((dateObj.getDate() < 10) ? '0' + (dateObj.getDate()) : (dateObj.getDate())) + "-kijiji-scraped-raw.json", JSON.stringify(jsonArray), function (err) {
        if (err) {
            return console.log(err);
        }
        console.log("Err: The file save had some errors!");
    });
    console.log("The file was saved!");
}