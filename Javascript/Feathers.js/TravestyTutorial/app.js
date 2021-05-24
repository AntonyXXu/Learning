const feathers = require("@feathersjs/feathers");
const express = require("@feathersjs/express");
const socketio = require("@feathersjs/socketio");
const moment = require("moment");

//Ideas service
class IdeaService {
  constructor() {
    this.ideas = [];
  }

  async find() {
    return this.ideas;
  }

  async create(data) {
    const idea = {
      id: this.ideas.length,
      text: data.text,
      tech: data.tech,
      viewer: data.viewer,
    };

    idea.time = moment().format("h::mm:ss a");

    this.ideas.push(idea);
    return idea;
  }
}
const app = express(feathers());

//Parse json
app.use(express.json());

// Configure socket.io
app.configure(socketio());

//Enable REST api
app.configure(express.rest());

// Register Services
app.use("/ideas", new IdeaService());

// New connection to stream channel
app.on("connection", (connect) => {
  app.channel("stream").join(connect);
});

//Publish to stream
app.publish((data) => {
  app.channel("stream");
});

const PORT = process.env.PORT || 3030;

app.listen(PORT).on("listening", () => {
  console.log("Realtime server on port " + PORT);
});

app.service("ideas").create({
  text: "build an app",
  tech: "node.js",
  viewer: "abc",
  time: moment().format("h:mm:ss a"),
});
