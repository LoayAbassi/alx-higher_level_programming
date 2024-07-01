#!/usr/bin/node
function callMeMoby (x, f) {
  for (let index = 0; index < x; index++) {
    f();
  }
}
module.exports.callMeMoby = callMeMoby;
