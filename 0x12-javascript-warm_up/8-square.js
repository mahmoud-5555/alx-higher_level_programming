#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length < 3) {
  console.log('Missing size');
} else {
  const input = argv[2];
  const num = +input; // Convert the argument to a number

  if (isNaN(num)) {
    console.log('Missing size');
  } else {
    // the logic of drowing
    for (let y = 0; y < num; y++) {
      console.log('X'.repeat(num));
    }
  }
}
