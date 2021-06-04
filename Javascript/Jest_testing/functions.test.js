const functions = require("./functions");

test("Add nums", () => {
  expect(functions.add(2, 2)).toBe(4);
});

test("Add nums", () => {
  expect(functions.add(2, 2)).not.toBe(6);
});

test("return null", () => {
  expect(functions.isNull(null)).toBeFalsy();
});
