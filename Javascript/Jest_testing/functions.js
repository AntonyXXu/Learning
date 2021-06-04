const functions = {
  add: (a, b) => {
    return a + b;
  },
  isNull: (x) => {
    return x;
  },
  createUser = () => {
      const user = {firstName: "abc"}
      user["lastName"] = "cde"
      return user
  }
};

module.exports = functions;
