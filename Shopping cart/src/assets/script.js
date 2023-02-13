/* Create an array named products which you will use to add all of your product object literals that you create in the next step. */


let product1 = {

  name: "Cherry",
  price: 15,
  quantity: 0,
  productId: 100,
  image: "images/cherry.jpg"
};
let product2 = {

  name: "Orange",
  price: 10,
  quantity: 0,
  productId: 101,
  image: "images/orange.jpg"
};
let product3 = {

  name: "strawberry",
  price: 7,
  quantity: 0,
  productId: 102,
  image: "images/strawberry.jpg"
};
let products = [product1, product2, product3];
function getProductByIdFromList(productId, productList) {
  return productList.find((product) => product.productId === productId);
}

/* Create 3 or more product objects using object literal notation 

   Each product should include five properties
   - name: name of product (string)
   - price: price of product (number)
   - quantity: quantity in cart should start at zero (number)
   - productId: unique id for the product (number)
   - image: picture of product (url string)
*/

/* Images provided in /images folder. All images from Unsplash.com
   - cherry.jpg by Mae Mu
   - orange.jpg by Mae Mu
   - strawberry.jpg by Allec Gomes
*/
let cart = [];
//let isThere = false; // boolean variable to check if item in cart or not 
/* Declare an empty array named cart to hold the items in the cart */
function addProductToCart(productId) {
  if (getProductByIdFromList(productId, products)) {
    if (getProductByIdFromList(productId, cart)) {
      increaseQuantity(productId);
      //isThere = true;
    }
    if (!cart.includes(getProductByIdFromList(productId, cart))) { //check if item is not in cart
      cart.push(getProductByIdFromList(productId, products)); //add item to cart 
      increaseQuantity(productId);//increase quantity
    }
  }
}





/* Create a function named addProductToCart that takes in the product productId as an argument
  - addProductToCart should get the correct product based on the productId
  - addProductToCart should then increase the product's quantity
  - if the product is not already in the cart, add it to the cart
*/
function increaseQuantity(productId) {
  let product = getProductByIdFromList(productId, cart)

  if (product) {
    product.quantity += 1;
  }

}
/* Create a function named increaseQuantity that takes in the productId as an argument
  - increaseQuantity should get the correct product based on the productId
  - increaseQuantity should then increase the product's quantity
*/
function decreaseQuantity(productId) {
  let product = getProductByIdFromList(productId, cart)
  if (product.quantity === 1) {
    removeProductFromCart(productId);
  } else {
    product.quantity -= 1;
  }
}
/* Create a function named decreaseQuantity that takes in the productId as an argument
  - decreaseQuantity should get the correct product based on the productId
  - decreaseQuantity should decrease the quantity of the product
  - if the function decreases the quantity to 0, the product is removed from the cart
*/
function removeProductFromCart(productId) {
  for (let i = 0; i < cart.length; i++) {
    if (cart[i].productId === productId) {
      cart[i].quantity = 0;
      cart.splice(i, 1);
    }
  }
}

/* Create a function named removeProductFromCart that takes in the productId as an argument
  - removeProductFromCart should get the correct product based on the productId
  - removeProductFromCart should update the product quantity to 0
  - removeProductFromCart should remove the product from the cart
*/
function cartTotal() {
  let sum = 0;
  cart.forEach(product => {
    sum += product.quantity * product.price
  });
  return sum;

}
/* Create a function named cartTotal that has no parameters
  - cartTotal should iterate through the cart to get the total of all products
  - cartTotal should return the sum of the products in the cart
*/
function emptyCart() {
  cart.splice(0, cart.length); //iterate over the array and delete every element
}
/* Create a function called emptyCart that empties the products from the cart */
let totalPayed = 0
function pay(payment) {
  //total after payment
  totalPayed += payment;
  return totalPayed - cartTotal();
}
/* Create a function named pay that takes in an amount as an argument
  - pay will return a negative number if there is a remaining balance
  - pay will return a positive number if money should be returned to customer
*/

/* Place stand out suggestions here (stand out suggestions can be found at the bottom of the project rubric.)*/


/* The following is for running unit tests. 
   To fully complete this project, it is expected that all tests pass.
   Run the following command in terminal to run tests
   npm run test
*/

module.exports = {
  products,
  cart,
  addProductToCart,
  increaseQuantity,
  decreaseQuantity,
  removeProductFromCart,
  cartTotal,
  pay,
  emptyCart,
  /* Uncomment the following line if completing the currency converter bonus */
  // currency
}
