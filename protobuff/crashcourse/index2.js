// google has protoC to compile proto files

const Schema = require("./employees_pb");
const fs = require("fs");
const ant = new Schema.Employee();
ant.setId(1000);
ant.setName("ant");
ant.setSalary(10000);

console.log(ant.getName());

const rick = new Schema.Employee();
rick.setId(1001);
rick.setName("rick");
rick.setSalary(10001);

const employees = new Schema.Employees();
employees.addEmployees(ant);
employees.addEmployees(rick);

bytes = employees.serializeBinary();
console.log("binary" + bytes);

// binary data is significantly smaller in size
fs.writeFileSync("employeesBinary", bytes);

const employeesRead = Schema.Employees.deserializeBinary(bytes);
console.log(employeesRead.toString());

/*********
 * Pros
 * - Can build a schema
 * - compact in size
 * - Language neutral
 * -- google has a compiler for it which is good
 *
 * Cons
 * takes a bit longer to build the schema (minor)
 * Potential to have undesired effects updating protoc
 * protobuf is overkill for small apps
 *********/
