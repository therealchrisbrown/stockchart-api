from flask import current_app, render_template
import yfinance as yf

def get_stock_chart(ticker):
    stock_data = yf.download(ticker, start="2018-01-01", end="2023-03-05")

    with current_app.app_context():
        import io
        import matplotlib.pyplot as plt
        from flask import Response

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