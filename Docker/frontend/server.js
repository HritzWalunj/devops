const express = require("express");
const axios = require("axios");
const app = express();

app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: true }));

const BACKEND_URL = process.env.BACKEND_URL || "http://backend:5000/submit";

app.get("/", (req, res) => {
  res.render("form", { error: null });
});

app.post("/submit", async (req, res) => {
  try {
    await axios.post(BACKEND_URL, req.body);
    res.redirect("/success");
  } catch (err) {
    res.render("form", {
      error: err.response?.data?.error || "Submission failed"
    });
  }
});

app.get("/success", (req, res) => {
  res.render("success");
});

app.listen(3000, () => {
  console.log("Frontend running on port 3000");
});
