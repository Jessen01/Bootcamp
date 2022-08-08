//notes exercise 1

function age(myage) {
    // let prag_age = 22;
    let mum_age = myage * 2;
    let dad_age = mum_age *1.2;
    console.log("my mom age is " + mum_age + " my dad age is " + dad_age);
}

  age(22)


// notes exercise 2

function ageofmum(mynewage) {
    let momage = mynewage * 2;
    return momage;
}
let oldage = ageofmum(22);
console.log(oldage)




//exercise 1 part 1

function infoaboutme(){
    let name = 'Pragasen'
    let myage = 22;
    let hobby  = "coding";
    console.log("My name is " + name + " and " + " my age is " + myage + " and myhobby is " + hobby)
}

infoaboutme();

part2

function infoAboutPerson (personName, personAge, personFavoriteColor) {
  console.log("Your name is " + personName + ", you're " + personAge + " years old " + ",your favourite color is " + personFavoriteColor)

}

infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")


//exercise 2

function calculatetip(){
    let tip = [0.2, 0.15 ,0.1];
    let totaltip = 0;
    let billamout = prompt("What's the bill amount?");
    let billamout1 = Number(billamout);
    let totalamout = billamout1 + totaltip;
    if (billamout1 <50){
        totaltip = billamout1 * tip[0];
        console.log(totaltip,totalamout);
    }else if (billamout1 >= 50 && billamout1 <= 200){
        totaltip = billamout1 * tip[1];
        console.log(totaltip,totalamout);
    }else if (billamout1 >200){
        totaltip = billamout1 * tip[2];
        console.log(totaltip,totalamout);
    }


}

calculatetip()


                     //other way of doing
                     function calculateTip(){
                        let y = prompt("Enter bill amount")
                        let x = Number(y)
                        let tip = 0
                        if (x<50){
                            tip = (0.2*x)}
                        else if( x>=50 && x<=200 ){
                            tip = (0.15*x)}
                        else
                            tip = (0.1*x)
                        console.log("The tip is $"+tip+ " and the final bill is $"+ (tip+x) )}
                        calculateTip()

//exercise3  

function isDivisible(){
    let arr = [];
    let sum = 0;
    for ( let i=0 ; i<499; i++){
        if (i % 23 == 0){
            arr = [i];
            console.log(arr);
           
        }  
    }
    for (let i in arr){
        sum += arr[i];
       
      }
       console.log(sum);
}
isDivisible()





//exercise 4  shopping list 

let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ["banana","orange","apple"];

const myBill = () => {
    let billAmount = 0;
    for (let item of shoppingList){
        if (item in stock && stock[item] > 0) {
            billAmount += prices[item];
            stock[item] -= 1;
        }
    }
   return billAmount;
}

console.log(myBill());
console.log(stock);






//exercise 5  amountchange

function changeEnough(itemPrice, amountOfChange){
    if (amountOfChange >= itemPrice){
        return true;
    } else if (amountOfChange < itemPrice){
        return false;
    }

}
let change = [25,20,5,0].reduce((a, b) => a + b, 0);


changeEnough(4.25, change)



//exercise 6  Vacation costs


const hotelCost = () => {
    let nights = 0;
    while (nights === 0 || nights === '' || isNaN(nights)) {
        nights = Number(prompt('Number of nights in hotel: '));
    }

    return 140 * nights;
}


const planeRideCost = () =>{
    let destination = '';
    let priceList = {
        london: 183,
        paris: 220
    }
    let price = 0;

    while (destination === '' || typeof destination !== 'string') {
        destination = prompt('Destination: ');
    }

    if (destination.toLowerCase() in priceList) {
        price = priceList[destination];
    } else {
        price = 300;
    }

    return price;
}


const rentalCarCost = () => {
    let days = 0;
    let pricePerDay = 40;
    let discount = 5;
    let totalPrice = 0;

    while (days === 0 || days === '' || isNaN(days)) {
        days = Number(prompt('Number of days to rent a car: '));
    }

    if (days > 10) {
        totalPrice = (pricePerDay * days) - (pricePerDay * days * (discount / 100));
    } else {
        totalPrice = pricePerDay * days;
    }

    return totalPrice;
}


const totalVacationCost = () => {
    return `The car cost: ${rentalCarCost()}\nThe hotel cost: ${hotelCost()}\nThe plane tickets cost: ${planeRideCost()}`
}

console.log(totalVacationCost());
