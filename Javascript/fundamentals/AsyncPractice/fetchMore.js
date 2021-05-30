const fetch = require("node-fetch");
const fetchData = async (country) => {
  try {
    const response = await fetch(
      `https://restcountries.eu/rest/v2/alpha/${country}`
    );
    const data = await response.json();
    return data;
  } catch (err) {
    console.log(err);
  }
};

const print = async (c) => {
  const country = await fetchData(c);
  console.log(country);
};

const neighbors = async (c) => {
  try {
    const country = await fetchData(c);

    const borders = await Promise.all(
      country.borders.map((border) => {
        return fetchData(border);
      })
    );

    console.log(borders);
    return borders;
  } catch (err) {
    console.log(err);
  }
};
// print("col");
neighbors("col").then((data) => {
  data.forEach((d) => {
    console.log(d.name);
  });
});
