const { default: fetch } = require("node-fetch");

class HttpError extends Error {
  constructor(response) {
    super(`${response.status} for ${response.url}`);
    this.name = "HttpError";
    this.response = response;
  }
}

async function loadJson(url) {
  const data = await fetch(url);
  if (data.status == 200) {
    return await data.json();
  } else {
    throw new HttpError(data);
  }
}

async function getGitUser() {
  try {
    var name = prompt("Enter name", "iliakan");
    const res = await loadJson(`https://api.github.com/users/${name}`);
    alert(res.name);
    return res;
  } catch (err) {
    if (err instanceof HttpError && err.response.status == 404) {
      alert("no user");
      return getGitUser();
    } else {
      throw err;
    }
  }
}

demoGithubUser();
