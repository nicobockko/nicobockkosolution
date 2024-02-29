
import dash
dash.register_page(__name__)

from dash import  html, callback, Input, Output,State,callback_context
from flask import g
from sqlalchemy import text

from datetime import datetime

def layout():
    db_session = getattr(g, 'db_session', None)
    query = text("SELECT * FROM test")
    result = db_session.execute(query)
    user_table = html.Table([
        html.Thead(html.Tr([html.Th(column) for column in result.keys()])),
        html.Tbody([
            html.Tr([
                html.Td(row[column]) for column in result.keys()
            ]) for row in result
        ])
    ])
    lay = html.Div([html.Button(id='btn-a',children='aa'),html.Div(datetime.now()),html.Div(id='abcd',children=user_table)])

    return lay

@callback(
    Output('btn-a', 'children'),
    [Input('btn-a', 'n_clicks')],
)
def display_table(n_clicks):
    print('콜백')
    return datetime.now()

