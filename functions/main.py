const functions = require("firebase-functions");
const admin = require("firebase-admin");
const express = require("express");
const yf = require("yfinance");
const { CanvasRenderService } = require("chartjs-node-canvas");

admin.initializeApp();

const app = express();

const getStockChart = async (ticker) => {
  const chartSize = 500;

  const canvasRenderService = new CanvasRenderService(chartSize, chartSize);
  const config = {
    type: "line",
    data: {
      labels: [],
      datasets: [
        {
          label: `${ticker} Stock Chart`,
          fill: false,
          borderColor: "rgb(75, 192, 192)",
          lineTension: 0.1,
          data: [],
        },
      ],
    },
    options: {
      scales: {
        xAxes: [
          {
            type: "time",
            time: {
              displayFormats: {
                month: "MMM YYYY",
              },
            },
          },
        ],
      },
    },
  };

  const data = await yf.download(ticker, {
    period: "5y",
  });

  data.forEach((row) => {
    config.data.labels.push(row.Date.toISOString());
    config.data.datasets[0].data.push(row.Close);
  });

  const chart = await canvasRenderService.renderToBuffer(config);
  return chart;
};

app.get("/stock-chart", async (req, res) => {
  try {
    const ticker = req.query.ticker;
    const chart = await getStockChart(ticker);
    res.set("Content-Type", "image/png");
    res.send(chart);
  } catch (error) {
    console.error(error);
    res.status(500).send(error.message);
  }
});

exports.app = functions.https.onRequest(app);