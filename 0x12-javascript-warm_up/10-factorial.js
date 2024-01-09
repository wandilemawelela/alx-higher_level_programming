#!/usr/bin/node

const num = process.argv[2];

const computeFactorial = (num) => {
  if (isNaN(num)) {
    return 1;
  } else if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * computeFactorial(num - 1);
  }
};

console.log(computeFactorial(num));
