#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const num = process.argv;
  let biggest = 0;
  for (let i = 0; i < num.length; i++) {
    if (num[i] > biggest) {
      biggest = num[i];
    }
  }
  console.log(parseInt(biggest));
}
