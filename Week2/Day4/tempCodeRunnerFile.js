let shoppingcart = {
    total : 0,
    add_to_cart: function(itemname,itemprice) {
        this.total = this.total + itemprice
        console.log("You have bought " + itemname + " at Rs " + itemprice)
    },
    get_total: function(currency="rs") {
        if(currency == "rs")
            return "Your total amount due is Rs " + this.total
        else if(currency == "euro") {
            return "Your total amount due is euro " + this.total/45
        }
    }
}

shoppingcart.add_to_cart("bottle",100)
shoppingcart.add_to_cart("chocolate",200)
console.log(shoppingcart.get_total())
console.log(shoppingcart.get_total("euro"))