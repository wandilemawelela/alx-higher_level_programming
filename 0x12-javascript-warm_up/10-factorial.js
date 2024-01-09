#!/usr/bin/node

const num = process.argv[2];

const computeFactorial = (n) => {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * computeFactorial(n - 1);
  }
};

console.log(computeFactorial(num));
