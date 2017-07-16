var mynum = 13579;
var arr = (mynum+'').split('');
var arrnum = [];
for (var value in arr) {
  arrnum[value] =parseInt(arr[value]);
  //console.log(arr[value]);
}

console.log(arrnum.reduce(function (x,y) {
  return x*10 + y;
}));
