#!/usr/bin/node

function isDigite(value)
{
	return /^\d+$/.test(value);
}

const { argv } = require("node:process");
const text =  "My number: " + argv[2];

if (isDigite(argv[2])){
	console.log(text);
}
else {
	console.log("Not a number");
}
