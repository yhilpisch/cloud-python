#
# Historical Stock Prices
# Plotted with Plotly & D3.js
#
# stock_interactive.py
#
# (c) Dr. Yves J. Hilpisch
# The Python Quants GmbH
#

import pandas as pd
import pandas.io.data as web
import plotly.plotly as ply
from plotly.graph_objs import Figure, Layout, XAxis, YAxis
from flask import Flask, request, render_template, redirect, url_for
from forms import SymbolSearch

#
# Needed for plotly usage
#

ply.sign_in('Python-Demo-Account', 'gwt101uhh0')

def df_to_plotly(df):
    '''
    Converting a pandas DataFrame to plotly compatible format.
    '''
    if df.index.__class__.__name__=="DatetimeIndex":
        x = df.index.format()
    else:
        x = df.index.values
    lines = {}
    for key in df:
        lines[key] = {}
        lines[key]['x'] = x
        lines[key]['y'] = df[key].values
        lines[key]['name'] = key
    lines_plotly = [lines[key] for key in df]
    return lines_plotly

#
# Main app
#

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    form = SymbolSearch(csrf_enabled=False)
    if request.method == 'POST' and form.validate():
        return redirect(url_for('results', symbol=request.form['symbol'],
                            trend1=request.form['trend1'],
                            trend2=request.form['trend2']))
    return render_template('selection.html', form=form)

@app.route("/symbol/<symbol>+<trend1>+<trend2>")
def results(symbol, trend1, trend2):
    data = web.DataReader(symbol, data_source='yahoo')
    data['Trend 1'] = pd.rolling_mean(data['Adj Close'], window=int(trend1))
    data['Trend 2'] = pd.rolling_mean(data['Adj Close'], window=int(trend2))
    layout = Layout(
        xaxis=XAxis(showgrid=True, gridcolor='#bdbdbd', gridwidth=2),
        yaxis=YAxis(showgrid=True, gridcolor='#bdbdbd', gridwidth=2)
    )
    fig = Figure(data=df_to_plotly(data[['Adj Close', 'Trend 1', 'Trend 2']]),
                layout=layout)
    plot = ply.plot(fig, auto_open=False)
    table = data.tail().to_html()
    return render_template('plotly.html', symbol=symbol,
                            plot=plot, table=table)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777)
