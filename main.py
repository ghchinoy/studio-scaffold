import mesop as me

from state.state import AppState
from components.page_scaffold import page_scaffold
from pages.home import home_page_content


def on_load(e: me.LoadEvent):
  """On load event"""
  me.set_theme_mode("system")


@me.page(
  path="/",
  title="Scaffold - Home",
  on_load=on_load,
)
def home_page():
    """Main Page"""
    state = me.state(AppState)
    with page_scaffold():
        home_page_content(state)
