// Get status

pm.test("Status code is 200", function () {
  pm.response.to.have.status(200);
});

const res = pm.response.json();

pm.test("status is ok", () => {
  pm.expect(res.status).to.eql("OK");
});

// Get Book ID
pm.test("Status code is 200", function () {
  pm.response.to.have.status(200);
});

const res = pm.response.json();

const nonFictionBooks = res.filter((book) => book.available == true);
const book = nonFictionBooks[0];
if (book) {
  pm.globals.set("bookID", book);
}
pm.test("book found", () => {
  pm.expect(book).to.be.an("object");
  pm.expect(book.available).to.be.true;
});
