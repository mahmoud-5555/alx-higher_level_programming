#!/usr/bin/node

exports.esrever = function (list) {
  const data = [];
  for (let i = 0; i < list.lenth(); i++) {
    data.unshift(list[i]);
  }
  return data;
};
