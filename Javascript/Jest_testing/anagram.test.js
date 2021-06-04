const isAnagram = require("./anagram");

test("fcn exists", () => {
  expect(typeof isAnagram).toBe("function");
});

test("'cinema' is an anagram of 'iceman'", () => {
  expect(isAnagram("cinema", "iceman")).toBeTruthy();
});

test("'dormitory' is an anagram of 'dirty rooms'", () => {
  expect(isAnagram("dormitory", "dirty room##")).toBeTruthy();
});

test("'dormitory' is an anagram of 'dirty rooms'", () => {
  expect(isAnagram("dormitory", "dirty rooms")).toBeFalsy();
});
