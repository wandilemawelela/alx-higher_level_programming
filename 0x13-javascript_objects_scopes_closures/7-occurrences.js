#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce(function (count, currentElement) {
    if (currentElement === searchElement) {
      count++;
    }
    return count;
  }, 0);
};
