from flask import Flask, request, Response
import firebase_admin
from firebase_admin import credentials, firestore
import yfinance as yf
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_stock_chart(ticker):
    stock_data = yf.download(ticker, start="2018-01-01", end="2023-03-05")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(stock_data["Close"])
    ax.set_title(f"{ticker} Stock Chart")
    ax.set_xlabel("Date")
    ax.set_ylabel("Close Price")

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Return image bytes with 'image/png' Content-Type header
    return buffer.getvalue(), 'image/png'

@app.route('/stock-chart', methods=['GET'])
def stock_chart():
    ticker = request.args.get('ticker')
    chart_bytes, content_type = get_stock_chart(ticker)
    return Response(chart_bytes, content_type=content_type)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
