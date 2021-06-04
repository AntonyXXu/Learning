const chunkArray = require("./chunkify");

test("fcn exists", () => {
  expect(chunkArray).toBeDefined();
});

test("chunkify array of size 10 and length 2", () => {
  const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const len = 2;
  const chunkedArr = chunkArray(nums, len);
  expect(chunkedArr).toEqual([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10],
  ]);
});

test("chunkify array of size 10 and length 2", () => {
  const nums = [1, 2, 3];
  const len = 1;
  const chunkedArr = chunkArray(nums, len);
  expect(chunkedArr).toEqual([[1], [2], [3]]);
});
