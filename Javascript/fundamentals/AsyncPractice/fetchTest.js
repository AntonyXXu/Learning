const fetch = require("node-fetch");

const fetchData = async () => {
  try {
    const response = await fetch("https://restcountries.eu/rest/v2/alpha/col");
    const country = await response.json();
    console.log("success: ", country);
  } catch (err) {
    console.log(err);
  }
};

fetchData();
