import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from eda import calculate_basic_statistics


def show_dashboard(data):
    app = dash.Dash('Product Reviews')

    nr_of_all_reviews = calculate_basic_statistics(data)

    text_style = dict(color='#444', fontFamily='sans-serif', fontWeight=300)
    plotly_figure = px.histogram(data, x="Age", title='Number of reviews per Age:')

    app.layout = html.Div([
        html.H2('Product Reviews', style=text_style),
        html.P('Number of analyzed reviews: ' + str(nr_of_all_reviews), style=text_style),
        dcc.Graph(id='plot1', figure=plotly_figure),
    ])
    app.server.run()

