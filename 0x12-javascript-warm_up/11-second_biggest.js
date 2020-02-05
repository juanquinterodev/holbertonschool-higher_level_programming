#!/usr/bin/node
const args = process.argv;
const nonbig = [];
const nums = [];
let i;
let biggest1;
let biggest2;
if (args.length < 4) {
  console.log(0);
} else {
  for (i = 2; i < args.length; i++) {
    nums.push(parseInt(args[i]));
  }
  biggest1 = Math.max(...nums);
  for (i = 0; i < nums.length; i++) {
    if (nums[i] !== biggest1) {
      nonbig.push(parseInt(nums[i]));
    }
  }
  biggest2 = Math.max(...nonbig);
  console.log(biggest2);
}
