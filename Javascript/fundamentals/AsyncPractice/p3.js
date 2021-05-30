// https://www.codingame.com/playgrounds/347/javascript-promises-mastering-the-asynchronous/the-last-challenge
let central = require("./central"),
  db1 = require("./db1"),
  db2 = require("./db2"),
  db3 = require("./db3"),
  vault = require("./vault"),
  mark = require("./mark");

const database = {
  db1: db1,
  db2: db2,
  db3: db3,
};

module.exports = function (id) {
  const prom = new Promise((resolve, reject) => {
    const db = Promise.all([
      central(id)
        .catch(() => {
          return Promise.reject("Error central");
        })
        .then((data) => {
          return database[data](id).catch(() => {
            return Promise.reject("Error " + data);
          });
        }),

      vault(id).catch(() => {
        return Promise.reject("Error vault");
      }),
    ]);
    db.then((data) => {
      resolve({
        id: id,
        username: data[0].username,
        country: data[0].country,
        firstname: data[1].firstname,
        lastname: data[1].lastname,
        email: data[1].email,
      });
      mark(id).catch();
    }).catch((err) => {
      reject(err);
    });
  });
  return prom;
};
