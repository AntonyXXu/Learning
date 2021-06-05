const niagaraWinery = {
  clientID: "niagara-winery",
  clientName: "Niagara Winery",
  brand: {
    name: "ONW",
    domain: "Food & Drink",
    category: "primary",
  },
  industry: {
    primary: "Food",
    secondary: "Drink",
  },
  status: "Active",
  country: "Canada",
};

const facebook = {
  providerID: "facebook",
  name: "facebook",
  type: "Third Party",
  status: "Active",
};

let clients = {};
let providers = {};
let expectedData = {};
expectedData.clients = clients;
expectedData.providers = providers;

module.exports.expectedData = expectedData;
