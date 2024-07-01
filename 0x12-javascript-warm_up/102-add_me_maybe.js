#!/usr/bin/node
function addMeMaybe(x,f){
    x++;
    f(x);
}
module.exports.addMeMaybe = addMeMaybe;