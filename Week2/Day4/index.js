//notes exercise 1

// function age(myage) {
//     // let prag_age = 22;
//     let mum_age = myage * 2;
//     let dad_age = mum_age *1.2;
//     console.log("my mom age is " + mum_age + " my dad age is " + dad_age);
// }

//   age(22)


//notes exercise 2

// function ageofmum(mynewage) {
//     let momage = mynewage * 2;
//     return momage;
// }
// let oldage = ageofmum(22);
// console.log(oldage)




//exercise 1 part 1

// function infoaboutme(){
//     let name = 'Pragasen'
//     let myage = 22;
//     let hobby  = "coding";
//     console.log("My name is " + name + " and " + " my age is " + myage + " and myhobby is " + hobby)
// }

// infoaboutme();

//part2

// function infoAboutPerson (personName, personAge, personFavoriteColor) {
//   console.log("Your name is " + personName + ", you're " + personAge + " years old " + ",your favourite color is " + personFavoriteColor)

// }

// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")


//exercise 2

// function calculatetip(){
//     let tip = [0.2, 0.15 ,0.1];
//     let totaltip;
//     let totalamout = billamout + totaltip;
//     let billamout = number(prompt("What's the bill amount?"));
//     if (billamout <50){
//         totaltip = billamout * tip[0];
//         console.log(totaltip,totalamout);
//     }else if (billamout >= 50 && <= 200){
//         totaltip = billamout * tip.[1];
//         console.log(totaltip,totalamout);
//     }else if (billamout >200){
//         totaltip = billamout * tip[2];
//         console.log(totaltip,totalamout);
//     }


// }

// calculatetip()


//exercise3

// function isDivisible(){
//     let arr = [];
//     let sum = 0;
//     for ( let i=0 ; i<499; i++){
//         if (i % 23 == 0){
//             arr = [i];
//             console.log(arr);
           
//         }  
//     }
//     for (let i in arr){
//         sum += arr[i];
       
//       }
//        console.log(sum);
// }
// isDivisible()

//exercise 4

// let stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// let prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

// let shoppingList = ["banana","orange","apple"];

// function mybill(){
//     for (let i = 0; i<shoppingList.length; i++){
//         if ( i in stock[1] && stock[2] > 0){
//             continue;
//         }
//         let instockprice = indexof(i)
//         if (instockprice == prices[1]){
//             console.log(prices[2]);
//         }
//     }
// }
// mybill()



//exercise 5

function changeEnough(itemPrice, amountOfChange){
    if (amountOfChange >= itemPrice){
        return true;
    } else if (amountOfChange < itemPrice){
        return false;
    }

}
let change = [25,20,5,0].reduce((a, b) => a + b, 0);


changeEnough(4.25, change)
