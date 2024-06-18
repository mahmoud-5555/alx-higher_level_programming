#!/usr/bin/node

const args = process.argv.slice(2); // Slice to skip the first two elements

if (args.length === 0) {
  console.log('Missing size');
} else {
  const input = args[0];
  const num = +input; // Convert the argument to a number

  if (isNaN(num)) {
    console.log('Missing size');
  } else {
    // the logic of drowing
    for (let i = 0; i < num; i++) {
      for (let y = 0; y < num; y++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
}
