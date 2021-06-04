const axios = require("axios");

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
    return axios
      .get("https://jsonplaceholder.typicode.com/users/1")
      .then((result) => result.data)
      .catch((error) => "error");
  },
};

module.exports = functions;
