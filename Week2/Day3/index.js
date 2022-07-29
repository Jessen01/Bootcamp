//exercise1
let people = ["Greg", "Mary", "Devon", "James"];
people.splice(0,1)
people[3] = "Jason"
people.push("pragasen")
console.log(people)
console.log(people.indexOf("Mary"))
let people1 = people.slice(1,4)
console.log(people1)
// console.log(people.indexof("Foo"))
//because its not a function

let last = people1[people1.length- 1]
console.log(last)

for (let i in people1){
    console.log(people1[i])
}
for (i=0; i<people1.length; i++){
 if ( people1[i].match("Jason")){
    console.log("Jason")
    break;
 }

} 

//exercise2

var colors = ["red","blue","yellow","green"]
var choice = ["My 1st choice”, “My 2nd choice”, “My 3rd choice"]
for (i=0; i<colors.length; i++){
    console.log("my #"+ i + " choice is " + colors[i])
}

//exercise3
let num = prompt("please enter a number")
typeof(num)
num2 = parseInt(num)
typeof(num2)

while (num2 <10){
    num++;
   prompt("enter a new number")
}


// let num = prompt("please enter a number")
// typeof(num)
// num = parseInt(prompt)
// typeof(num)

// do {
//     prompt("enter a new number")

// while(num < 10);

// }

//exercise4
let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}
console.log(building.numberOfFloors);
console.log(building.numberOfAptByFloor.firstFloor, building.numberOfAptByFloor.thirdFloor);
console.log(building.nameOfTenants[1], building.numberOfRoomsAndRent.dan)
var sum = building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1]
var sum1 = parseInt(sum);
console.log(sum);
if( sum1 > building.numberOfRoomsAndRent.dan[1]) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
}
    console.log( building.numberOfRoomsAndRent.dan[1]);





//exercise5

let family = {father : 1, mother: 2, son : 3}
for (let i in family ){
    console.log((Object.keys(family)))
}
for (let i in family){
    console.log((Object.values(family)))
}

//exercise6

let details = {
    my: 'name ',
    is: 'Rudolf ',
    the: 'raindeer'
  }
  let str = []
  for (let i in details){
    str = str + i+ " " + details[i]
       
      }
    
  


  //exercise7

  let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
  


