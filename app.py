# pngデータをレスポンスで返す
from flask import Flask, render_template, make_response, jsonify
from io import BytesIO
import urllib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


app = Flask(__name__)

@app.route('/')
def index():
    render_template('index_html')

@app.route('/graph1.png')
def graph1():
    # データからグラフをプロットする 
　　x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.title('サンプル')
    plt.grid(which='both')
    plt.legend()
    plt.plot(x,y)
    # canvasにプロットした画像を出力
    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    data = png_output.getvalue()
    # HTML側に渡すレスポンスを生成する
    response = make_response(data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Length'] = len(data)
    return response


if __name__ == "__main__":
    app.run(debug=True)
