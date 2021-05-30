const inventory = {
  sunglasses: 1900,
  pants: 1088,
  bags: 1344,
};

// Write your code below:
const myExecutor = (res, rej) => {
  if (inventory.sunglasses > 0) {
    res("Sunglasses order processed.");
  } else {
    rej("That item is sold out.");
  }
};

const order = () => {
  return new Promise(myExecutor);
};

const orderS = order();

console.log(orderS);
