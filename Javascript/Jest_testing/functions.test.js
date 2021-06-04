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

test("user should be abc cde", () => {
  expect(functions.createUser()).toEqual({
    firstName: "abc",
    lastName: "cde",
  });
});

test("should be less than 50", () => {
  const a = 80;
  const b = -30;
  expect(functions.add(a, b)).toBeLessThanOrEqual(50);
});

test("there is no I in team", () => {
  expect("teami").not.toMatch(/I/);
});

test("c in username", () => {
  const usernames = ["a", "b", "c"];
  expect(usernames).toContain("c");
});

//Async
test("username should be Chelsey Dietrich", () => {
  expect.assertions(1);
  functions.fetchUser().then((data) => {
    expect(data.name).toEqual("Chelsey Dietrich");
  });
});
