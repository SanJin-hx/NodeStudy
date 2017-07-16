function get_primes(arr) {
  return arr.filter(function isPrime(number) {
   if (typeof number !== 'number' || number<2) {
      // 不是数字或者数字小于2
      return false;
   }

   if (number === 2) {//2是质数
      return true;
   } else if (number % 2 === 0) {//排除偶数
      return false;
   }
   var squareRoot = Math.sqrt(number);
   //console.log(number);
　　//因为2已经验证过，所以从3开始；且已经排除偶数，所以每次加2
   for(var i = 3; i <= squareRoot; i += 2) {
      if (number % i === 0) {
         return false;
      }
   }
   return true;
});
}
var
    x,
    r,
    arr = [];
for (x = 1; x < 100; x++) {
    arr.push(x);
}
r = get_primes(arr);
if (r.toString() === [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97].toString()) {
    console.log('测试通过!');
} else {
    console.log('测试失败: ' + r.toString());
}
var r,
    arr = ['apple', 'strawberry', 'banana', 'pear', 'apple', 'orange', 'orange', 'strawberry'];
    r = arr.filter(function (element, index, self) {
      //console.log(element);
    //  console.log(index);

    return self.indexOf(element) === index;
});
console.log(r.toString());
