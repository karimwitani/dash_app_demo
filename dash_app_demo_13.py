"""
Passing Components Into Callbacks Instead of IDs
When creating app layouts in earlier examples, we assigned IDs to components within the layout and later referenced 
these in callback inputs and outputs.

In the first example, there is a dcc.Input component with the id 'my-input' and a html.Div with the id 'my-output'

You can also provide components directly as inputs and outputs without adding or referencing an id. 
Dash autogenerates IDs for these components.

Here is the first example again. Prior to declaring the app layout, we create two components, assigning each one to a 
variable. We then reference these variables in the layout and pass them directly as inputs and outputs to the callback.

from : https://dash.plotly.com/basic-callbacks
"""

from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)

my_input = dcc.Input(value='initial value', type='text')
my_output = html.Div()

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        my_input
    ]),
    html.Br(),
    my_output
])


@callback(
    Output(my_output, component_property='children'),
    Input(my_input, component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'

if __name__ == '__main__':
    app.run_server(port=8051,debug=True)

"""
In Python 3.8 and higher, you can use the walrus operator to declare the component variables within the app layout
"""

# app.layout = html.Div([
#     html.H6("Change the value in the text box to see callbacks in action!"),
#     html.Div([
#         "Input: ",
#         my_input := dcc.Input(value='initial value', type='text')
#     ]),
#     html.Br(),
#     my_output := html.Div(),
# ])

# @callback(
#     Output(my_output, component_property='children'),
#     Input(my_input, component_property='value')
# )
# def update_output_div(input_value):
#     return f'Output: {input_value}'
