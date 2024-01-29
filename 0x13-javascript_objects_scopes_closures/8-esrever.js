#!/usr/bin/node
exports.esrever = function (list) {
  const resvList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    resvList.push(list[i]);
  }
  return resvList;
};
