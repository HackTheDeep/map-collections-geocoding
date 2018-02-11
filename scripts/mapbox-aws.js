var AWS = require('aws-sdk');
var fs = require('fs');
var MapboxClient = require('mapbox');

// Run with "node mapbox-aws.js <ACCESS-KEY-WITH-UPLOAD-SCOPE>
var client = new MapboxClient(process.argv[2]);

client.createUploadCredentials(function(err, credentials) {
  // Use aws-sdk to stage the file on Amazon S3
  console.log("Retrieving S3 credentials");
  var s3 = new AWS.S3({
    accessKeyId: credentials.accessKeyId,
    secretAccessKey: credentials.secretAccessKey,
    sessionToken: credentials.sessionToken,
    region: 'us-east-1'
  });
  console.log("Adding object to S3");
  s3.putObject({
    Bucket: credentials.bucket,
    Key: credentials.key,
    Body: fs.createReadStream('./make-pipeline/ornithology.geojson')
  }, function(err, resp) {
    console.log(resp);
    console.log("Uploading...");
    client.createUpload({
      tileset: ["bgun", 'ornithology'].join('.'),
      url: credentials.url,
      name: 'ornithology'
    }, function(err, upload) {
      console.log("Upload status", upload);
    });
  });
});
