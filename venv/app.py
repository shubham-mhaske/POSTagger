import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import base64
import tagger

#Create icon data
image_filename = "logo.png"
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

#Training
tagger.train()


navbar = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), height="30px")),
                    dbc.Col(dbc.NavbarBrand("Hindi POS Tagger", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
        )
    ],
    color="dark",
    dark=True


)


app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY], )
app.layout = html.Div([navbar, dbc.Container([

    dbc.Card([
        dbc.CardHeader("Sentence"),
        dbc.CardBody([
            dbc.Row(dbc.Input(placeholder="Enter sentence here", id='input')),
            html.Br(),
            dbc.Row(dbc.Button("Get Results", color="info", block=True, id='button')),
            html.Br(),
            html.Div(id='output')

        ])
    ],color='secondary'
    )
],
    className="p-5",
)
                       ])


@app.callback(Output("output", "children"), [Input("button", "n_clicks")], state=[State("input", "value")])
def output_text(n_clicks, value):
    table_header = [
        html.Thead(html.Tr([html.Th("Symbol"), html.Th("POS Tag")]))
    ]

    table_data = list()
    for word, pos in tagger.get_result(value):
        table_data.append(html.Tr([html.Td(word), html.Td(pos)]))

    table_body = [html.Tbody(table_data)]
    table = dbc.Table(table_header + table_body,
                      bordered=True,

                      hover=True,
                      responsive=True,
                      striped=True,

                      )
    return [dbc.Alert("Procesed Result", color="success"), html.Br(), table]


if __name__ == "__main__":
    app.run_server(debug=True)
