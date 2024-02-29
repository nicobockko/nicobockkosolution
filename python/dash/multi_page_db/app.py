import dash
import dash_bootstrap_components as dbc
from flask import g,Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# 데이터베이스 연결 설정
engine = create_engine('mysql+pymysql://root:1234@localhost:3306/junsik')
Session = sessionmaker(bind=engine)

server = Flask(__name__)
app = dash.Dash(
    __name__,server=server, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True,suppress_callback_exceptions=True
)

@server.before_request
def before_request():
    g.db_session = Session()

@server.teardown_request
def teardown_request(exception=None):
    db_session = getattr(g, 'db_session', None)
    if db_session is not None:
        db_session.close()


navbar = dbc.NavbarSimple(
    dbc.Nav(
        [
            dbc.NavLink(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
    ),
    brand="Multi Page App Demo: Query Strings",
    color="primary",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Container(
    [navbar, dash.page_container],
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)
