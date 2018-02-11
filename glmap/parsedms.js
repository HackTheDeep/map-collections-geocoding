

let degreesToDecimals = function(degrees, minutes, seconds, direction) {
  let dd = degrees + (minutes/60) + (seconds/(60*60));
  if (direction === 'S' || direction === 'W') dd *= -1
  return dd;
}

// assumes we have direction already
let parse = function(str, direction) {
  let re = new RegExp(/[^0-9]/g);

  let parts = str.split(re)
    .filter(part => !!part); // filter out empty strings, often seconds are missing

  if (parts.length === 3) {
    return degreesToDecimals(parseInt(parts[0]), parseInt(parts[1]), parseInt(parts[2]), direction);
  } else if (parts.length == 2) {
    return degreesToDecimals(parseInt(parts[0]), parseInt(parts[1]), 0, direction);
  } else {
    return null;
  }
};

let runTest = function() {
  const tests = [
    "38ø56\'20",
    "33 31\'30Ó",
    "38ø33\'"
  ];
  tests.forEach(test => {
    console.log(parse(test));
  });
}

module.exports = {
  parse: parse,
  runTest: runTest
}

// run this file
runTest();
