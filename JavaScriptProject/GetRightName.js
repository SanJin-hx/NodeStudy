var namearr = ['adam','LISA','batT'];//名字数组
var CorrectName = [];//保存规范后名字
function SpecificationName(name) {
    var FamilyNmae = name.substring(0,1);//名字首字母大写
    var Name = name.substring(1,4);//剩余字母小写
    var allname = FamilyNmae.toUpperCase()+Name.toLowerCase();//组合名字
    //  CorrectName[x] = allname;
    //console.log(allname);
    //console.log(name);
}
namearr.map(SpecificationName);
//console.log(CorrectName);
