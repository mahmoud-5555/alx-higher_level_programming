#!/usr/bin/node

const { argv } = require('node:process');
const numberOfArgumant = argv.length - 2;

if (numberOfArgumant === 0) {
  console.log('No argument');
} else if (numberOfArgumant === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
