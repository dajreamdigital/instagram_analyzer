from cStringIO import StringIO

from flask import Flask, render_template, request, \
    url_for, redirect, make_response

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from forms import InstagramAnalyzerForm
from instagram_analyze import instagram_analyzer
from instagram_graphs import instagram_graph


app = Flask(__name__)
app.config.from_object('instagram_analyzer_app.config')

# routes


@app.route('/', methods=['GET', 'POST'])
def main():
    form = InstagramAnalyzerForm(request.form)
    if form.validate_on_submit():
        text = form.keyword.data
        return redirect(url_for('instagram_analyze', user_input=text))
    return render_template('index.html', form=form)


@app.route("/instagram_analyze/<user_input>")
def instagram_analyze(user_input):

    return render_template(
        'instagram_analyzer.html',
        input=user_input,
        filename=user_input+".png"
    )


@app.route("/instagram_analyze/<image_name>.png")
def image(image_name):

    # Pulls in the analyzer and creates the DataFrame
    data = instagram_analyzer(image_name, 0)

    # formats the DataFrame to display plots
    instagram_graph(data)

    # renders matplotlib image to Flask view
    canvas = FigureCanvas(plt.gcf())
    output = StringIO()
    canvas.print_png(output)

    response = make_response(output.getvalue())
    response.mimetype = 'image/png'

    return response