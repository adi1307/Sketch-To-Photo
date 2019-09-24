console.log("server file");
var express = require("express");
var cors = require("cors");
var fs = require("fs");

var bodyparser = require("body-parser");

var app = express();
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header(
    "Access-Control-Allow-Headers",
    "Origin,X-Requested-With,Content-Type,Accept"
  );
  next();
});
//app.use(cors());
//cors({ credentials: true, origin: true });
app.use(bodyparser.json());

app.post("/send", (req, res) => {
  console.log(req.body);
  const data = req.body;
  fs.writeFileSync("data.json", JSON.stringify(data));
  res.send("send from the server.js");
});

app.listen("8888", () => {
  console.log("CONNECTED TO THE PORT !!!!!!");
});
