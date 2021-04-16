const posts = [
  {
    title: "post 1",
    body: "this is post two",
  },
  {
    title: "post 2",
    body: "this is post two",
  },
];

function getPosts() {
  setTimeout(() => {
    let output = "";
    posts.forEach((post, index) => {
      output += `<li>${post.title}</li>`;
    });
    document.body.innerHTML = output;
  }, 1000);
}

function createPost(post) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      posts.push(post);
      const error = false;
      if (!error) {
        resolve();
      } else {
        reject("something went wrong");
      }
    }, 2000);
  });
}

// createPost({
//   title: "post3",
//   body: "this is post3",
// })
//   .then(getPosts)
//   .catch((err) => console.log(err));

// async/await
async function init() {
  await createPost({
    title: "post3",
    body: "this is post3",
  });
  getPosts();
}

init();

// async await with fetch

async function fetchUsers() {
  const res = await fetch("http://jsonplaceholder.typicode.com/users");
  const data = await res.json();
  console.log(data);
}
fetchUsers();

// Promise.all
// const promise1 = Promise.resolve("hello");
// const promise2 = 10;
// const promise3 = new Promise((resolve, reject) => {
//   setTimeout(resolve, 2000, "goodbye");
// });
// const promise4 = fetch(
//   "http://jsonplaceholder.typicode.com/users"
// ).then((res) => res.json());

// Promise.all([promise1, promise2, promise3, promise4]).then((values) => {
//   console.log(values);
// });
