const isAnagram = require("./anagram");

// beforeEach(() => {
//   return initDB();
// });
// afterEach(() => {
//   return closeDB();
// });

// beforeAll(() => {
//   return initDB();
// });
// afterAll(() => {
//   return closeDB();
// });

// const initDB = () => {
//   console.log("init db");
// };
// const closeDB = () => {
//   console.log("close DB");
// };
const nameCheck = () => {
  console.log("checking name");
};

describe("Checking Names", () => {
  beforeEach(() => {
    return nameCheck();
  });
  test("user is jeff", () => {
    const user = "jeff";
    expect(user).toEqual("jeff");
  });

  test("user is karen", () => {
    const user = "karen";
    expect(user).toEqual("karen");
  });
});

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
