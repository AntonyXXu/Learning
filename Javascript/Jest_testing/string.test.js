const reverseString = require("./string");

test("fcn exists", () => {
  expect(reverseString).toBeDefined();
});

test("fcn works", () => {
  expect(reverseString("abc")).toEqual("cba");
});

test("fcn works", () => {
  expect(reverseString("Abc").toLowerCase()).toEqual("cba");
});
