#!/usr/bin/node
const fs = require('fs');

const readAndPrintFile = (filePath) => {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.log(`An error occurred: ${err.message}`);
    } 
    else {
      console.log(data);
    }
  });
};

if (process.argv.length !== 3) {
  console.log('Usage: node readFile.js <file_path>');
} 
else {
  const filePath = process.argv[2];
  readAndPrintFile(filePath);
}
