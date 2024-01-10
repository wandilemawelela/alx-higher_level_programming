#!/usr/bin/node

let printedArguments = 0;

exports.logMe = function (item) {
    console.log(`${printedArguments}: ${item}`);
    printedArguments++;
};
