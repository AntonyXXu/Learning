const { default: fetch } = require("node-fetch");

loadJson = async (url) => {
  try {
    const data = await fetch(url);
    console.log(data);
    if (data.status == 200) {
      return await data.json();
    } else {
      throw new Error(data.status);
    }
  } catch (err) {
    alert(err);
  }
};

loadJson("test");
