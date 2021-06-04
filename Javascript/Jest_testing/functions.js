const { default: axios } = require("axios");

const functions = {
  add: (a, b) => {
    return a + b;
  },
  isNull: (x) => {
    return x;
  },
  createUser: () => {
    const user = { firstName: "abc" };
    user["lastName"] = "cde";
    return user;
  },
  fetchUser: () => {
    axios
      .get("http://jsonplaceholder.typicode.com/users//5")
      .then((result) => result.data)
      .catch((error) => error);
  },
};

module.exports = functions;
