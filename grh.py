from flask import Flask, make_response, send_file 
import datetime
from io import BytesIO
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
app = Flask(__name__)

@app.route("/simple.png")
def simple():
    

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

@app.route('/fig/<cropzonekey>')

def fig(cropzonekey):
    
    fig = plt.plot([1,2,3,4], [1,2,3,4])
    
    img = BytesIO()
    
    plt.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')



if __name__ == "__main__":
    app.run()