#!/usr/bin/node

let count = 0;
let args = process.argv

for(let i in args){
	count += 1
}
if (count === 2){
	console.log("No argument");
}
else if (count > 2){
	console.log(args[2]);
}
