const functions = require("firebase-functions");
const fetch = require("node-fetch");

exports.getStockChart = functions.https.onRequest(async (req, res) => {
  const ticker = req.query.ticker;
  const appEngineUrl = "https://stockchart-api.appspot.com/stock-chart";
  const url = `${appEngineUrl}?ticker=${ticker}`;

  try {
    const response = await fetch(url);
    const imageBuffer = await response.buffer();
    res.set("Content-Type", "image/png");
    res.send(imageBuffer);
  } catch (error) {
    console.error(error);
    res.status(500).send("Error fetching stock chart.");
  }
});
