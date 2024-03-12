#!/usr/bin/node

const { argv } = require('node:process');

const mytext = argv[2] + ' is ' + argv[3];

console.log(mytext);
