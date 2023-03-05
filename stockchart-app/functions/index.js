const functions = require("firebase-functions");
const express = require("express");
const cors = require("cors");
const { spawn } = require("child_process");

const app = express();

app.use(cors());

app.get("/stock-chart", async (req, res) => {
    const ticker = req.query.ticker;
    const pythonProcess = spawn("python", [
        "main.py",
        "--ticker",
        ticker,
    ]);

    pythonProcess.stdout.on("data", (data) => {
        res.type("image/png").send(data);
    });
});

exports.app = functions.https.onRequest(app);
