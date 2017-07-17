'use strict';
class Animal {
    constructor(name) {
        this.name = name;
    }
}
class Cat extends Animal{
  constructor(name){
    super(name);
  }
  say(){
    return('Hello, '+this.name+'!');
  }
}
var kitty = new Cat('Kitty');
var doraemon = new Cat('哆啦A梦');
if (kitty && kitty.name === 'Kitty' && kitty.say && typeof kitty.say === 'function' && kitty.say() === 'Hello, Kitty!' && kitty.say === doraemon.say) {
    console.log('测试通过!');
} else {
    console.log('shibai');
}
/*function Cat(name){
  this.name = name;
}
Cat.prototype.say = function(){
  return('Hello, '+this.name+'!');
};

var kitty = new Cat('Kitty');
var doraemon = new Cat('哆啦A梦');
if (kitty && kitty.name === 'Kitty' && kitty.say && typeof kitty.say === 'function' && kitty.say() === 'Hello, Kitty!' && kitty.say === doraemon.say) {
    console.log('测试通过!');
} else {
    console.log('shibai');
}*/
