// Get status

pm.test("Status code is 200", function () {
  pm.response.to.have.status(200);
});

const res = pm.response.json();

pm.test("status is ok", () => {
  pm.expect(res.status).to.eql("OK");
});
