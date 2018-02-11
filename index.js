let csv = require('csv');
let fs = require('fs');
let request = require('superagent');

console.log("\nMAP THE COLLECTIONS go go geocoder");
console.log("==================================\n\n");

let cleanDatasetFile = './csvs/test100.csv';

let data = fs.readFileSync(cleanDatasetFile);


console.log("Data file opened. Parsing...");

console.time("Parse completed in");

let makeTableName = function(str) {
  return str.replace(/\W+/gi, '');
}

let desiredColumns = {
  'CatalogNumber': 'text',
  'AMNHAccNumber': 'text',
  'Class'        : 'text',
  'Subclass'     : 'text',
  'Latitude'     : 'double',
  'Longitude'    : 'double'
};

let x = 0;
csv.parse(data, (err, data) => {
  if (err) {
    throw new Error(err);
  }

  console.timeEnd("Parse completed in");

  console.log("Analyzing CSV file...");

  let headers = data[0];
  headers.forEach((header, idx) => {
    console.log([idx, header, makeTableName(header)].join(' '));
  });

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
