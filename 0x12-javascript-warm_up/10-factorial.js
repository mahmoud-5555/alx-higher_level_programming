#!/usr/bin/node
const { argv } = require("node:process");

function factorial(result, input){
if (input === 0 || input === 1) {
  return result;
}
else {
  return factorial(result * input, input - 1);
 }
}

let input = +argv[2];
if (isNaN(input)){
  console.log(1);
} else {
	console.log(factorial(1, input));
}