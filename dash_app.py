import dash
from dash import html
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output

from eda import calculate_basic_statistics


def show_dashboard(data):
    app = dash.Dash('Product Reviews')

    nr_of_all_reviews, nr_of_all_clothes = calculate_basic_statistics(data)

    text_style = dict(color='#444', fontFamily='sans-serif', fontWeight=300)
    plotly_figure = px.histogram(data, x="Age", title='Number of reviews per Age:')
    rating_pie = px.pie(data, values=data['Rating'].value_counts().values, names=data['Rating'].value_counts().index,
                        title='Rating')

    class_name_nr_reviews = px.histogram(data, x="Class Name", title='Number of reviews per Class Name:')

    app.layout = html.Div([
        html.H2('Product Reviews', style=text_style),
        html.P('Number of analyzed reviews: ' + str(nr_of_all_reviews), style=text_style),
        html.P('Number of rating clothes: ' + str(nr_of_all_clothes), style=text_style),
        dcc.Graph(id='plot1', figure=class_name_nr_reviews),
        dcc.Graph(id='plot2', figure=plotly_figure),
        dcc.Dropdown(
            id='names',
            value=data['Class Name'].value_counts().index,
            options=[{'value': x, 'label': x}
                     for x in set(data['Class Name'])],
            clearable=False
        ),
        dcc.Graph(id='plot3', figure=rating_pie)
    ])

    @app.callback(
        Output("plot3", "figure"),
        Input("names", "value"))
    def generate_chart(names):
        fig = px.pie(data, values=data[data['Class Name'] == str(names)]['Rating'].value_counts().values,
                     names=data[data['Class Name'] == str(names)]['Rating'].value_counts().index,
                     title='Rating')
        return fig

    app.server.run(debug=True)
