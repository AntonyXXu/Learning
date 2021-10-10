const fs = require("fs");

employees = [];
employees.push({
  name: "ant",
  salary: 1000,
  id: 0001,
});

employees.push({
  name: "bob",
  salary: 2000,
  id: 0002,
});

fs.writeFileSync("jsonData.json", JSON.stringify(employees));
