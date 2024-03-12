#!/usr/bin/node 


function isDigite (value) {
	return /^-?\d+$/.test(value);
  }
  
  const { argv } = require('node:process');
  
  if (isDigite(argv[2])) {
	let loopOf = parseInt(argv[2]);
	for (let i = 0; i < loopOf; i++){
		console.log("C is fun")
	}
  } else {
	console.log('Missing number of occurrences');
  }