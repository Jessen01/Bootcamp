//exercise 1

let x = 5;
let y = 2;
if (x > y) {
    console.log("x is the bigger number")
} else if (y > x){
    console.log("y is bigger")
}

//exercise 2
let newdog = "Chihuahua";
console.log(newdog.length);
console.log(newdog.toUpperCase());  //to make newdog uppercase
console.log(newdog.toLowerCase());  //to make newdog lowercase
 if (newdog === "Chihuahua"){
    console.log("I love Chihuahuas, it’s my favorite dog breed")
 } else {
    console.log("I dont care, I prefer cats")
 }


 //exercise3
 let x = prompt("input a number");
 if (x % 2 == 0) {
    console.log("x is an even number");
 } else
    console.log("x is an odd number");
 

//exercise4
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000", "james"];
if (users.length === 0){
    console.log("no one is online");
} else if (users.length === 1){
    console.log(users[0] + " is online");
} else if (users.length === 2) {
    console.log(users[0]+" "+users[1] + " are online");
} else if(users.length > 2) {
    let remainingusers = users.length-2
    console.log(users[0]+" "+users[1] + " and " + remainingusers +  " are online")
}


//exercise gold 
// exercise 1

let language = prompt("enter your language");
 
 response = language.toLowerCase();

 switch (response) {
    case "french" :
        console.log("Bonjour");
        break;
    case "english" :
        console.log("Hello");
        break;
    case "hebrew" :
        console.log("Shalom")
        break;
    default:
        console.log("01110011 01101111 01110010 01110010 01111001");
 }


 //exercise 2
 let grade = Number(prompt("input your number"));
 if (grade > 90 ){
    console.log("A");
 } else if (grade >= 80 && grade <= 90){
     console.log("B")
 } else if (grade >= 70 && grade <80){
     console.log("C")
 } else if (grade < 70){
    console.log ("D")
 }


 //exercise3
 let verb = prompt("Please enter a verb")
 let verb1 = verb.toLowerCase()
 let n =verb1.length
 let str = verb1;
 let part = /ing/i;
 let result = str.match(part);
console.log(result)
 if (n <3){
  console.log(verb1)
}
 else if (n >3 && result != null)
  console.log(verb1+"ly")
 else
  console.log(verb1+"ing")