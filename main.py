import mesop as me

from state.state import AppState
from components.page_scaffold import page_scaffold
from pages.home import home_page_content
from pages.another import another_content
from pages.gemini2 import gemini_page_content


def on_load(e: me.LoadEvent):  # pylint: disable=unused-argument
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
    with page_scaffold():  # pylint: disable=not-context-manager
        home_page_content(state)


@me.page(
    path="/another",
    title="Scaffold - Another Page",
    on_load=on_load,
)
def another_page():
    """Another Page"""
    another_content(me.state(AppState))        


@me.page(
    path="/gemini",
    title="Scaffold - Gemini",
    on_load=on_load,
)
def gemini_page():
    """Gemini 2.0 Flash Page"""
    state = me.state(AppState)
    with page_scaffold():  # pylint: disable=not-context-manager
        gemini_page_content(state)
