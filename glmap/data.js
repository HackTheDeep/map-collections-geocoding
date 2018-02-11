let csv = require('csv');
let fs = require('fs');
let request = require('superagent');
let moment = require('moment');
let _ = require('lodash');

let parsedms = require('./parsedms.js');



console.log("\nMAP THE COLLECTIONS go go geocoder");
console.log("==================================\n\n");

let cleanDatasetFile = '../csvs/clean_dataset_iz.csv';

let data = fs.readFileSync(cleanDatasetFile);


console.log("Data file opened. Parsing...");

console.time("Parse completed in");

let makeTableName = function(str) {
  return str.replace(/\W+/gi, '');
}


csv.parse(data, { columns: true }, (err, data) => {
  if (err) {
    throw new Error(err);
  }

  console.timeEnd("Parse completed in");

  console.log("Analyzing CSV file...");

  //console.log(data[0]);

  //console.log(data);

  let mapped = data.map(item => {
    let LL = {
      decimal: isNaN(parseFloat(item['decimal latitude'])) || isNaN(parseFloat(item['decimal longitude']))
        ? false
        : [item['decimal latitude'], item['decimal longitude']],
      degFrom: [
        parsedms.parse(item['Latitude (from)'],  item['Lat (from) NS']),
        parsedms.parse(item['Longitude (from)'], item['Long (from) EW'])
      ],
      degTo: [
        parsedms.parse(item['Latitude (to)'], item['Lat NS  (to)']),
        parsedms.parse(item['Longitude   (to) '], item['Long EW  (to)'])
      ]
    };

    if (LL.degFrom[0] === null || LL.degFrom[1] === null) {
      LL.degFrom = null;
    }
    if (LL.degTo[0] === null || LL.degTo[1] === null) {
      LL.degTo = null;
    }
    if (LL.degFrom) {
      console.log(LL);
    }
  
    return LL;
  });


  /*
  let uniqueNames = new Set();

  data.forEach((item, idx) => {
    // let fullLocality = item.slice(104,120);
    // let cleanLocalityString = fullLocality.filter(i => !!i).join(',');
    // uniqueNames.add(cleanLocalityString);

    let LLstring = item.slice(125,134).join(',');
    console.log(LLstring);
  });

  // console.log(uniqueNames);
  // console.log(uniqueNames.size);

  console.log("done");

  /*
  let createTableQuery = 'CREATE TABLE collection (\n';
  desiredColumns.forEach(col => {
    createTableQuery += col+',\n';
  });
  createTableQuery = createTableQuery.substring(0, createTableQuery.length - 2); 
  createTableQuery += ');';

  console.log(createTableQuery);

  const { Pool, Client } = require('pg');

  // pools will use environment variables
  // for connection information
  const pool = new Pool();

  pool.query(createTableQuery, (err, res) => {
    if (err) { throw new Error(err); }
    pool.end();
    console.log(res);
  });
  */
});


/*
request.get("http://api.geonames.org/searchJSON?q=solomon%20islands&username=***REMOVED***&format=json")
  .then(resp => {
    console.log(resp.body);
  });
  */
