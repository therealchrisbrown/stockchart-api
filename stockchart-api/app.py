from flask import Flask, Response, request
from stockchart import get_stock_chart

import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)

@app.route('/stock-chart')
def stock_chart():
    ticker = request.args.get('ticker')
    chart_bytes, content_type = get_stock_chart(ticker)
    return Response(chart_bytes, content_type=content_type)

if __name__ == '__main__':
    app.run(debug=True)