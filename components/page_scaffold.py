import mesop as me

from state.state import AppState

from components.side_nav import sidenav
from components.styles import (
    SIDENAV_MAX_WIDTH,
    SIDENAV_MIN_WIDTH,
)

@me.content_component
def page_scaffold():
    """page scaffold component"""

    app_state = me.state(AppState)

    sidenav("")

    with me.box(
        style=me.Style(
            display="flex",
            flex_direction="column",
            height="100%",
            margin=me.Margin(
                left=SIDENAV_MAX_WIDTH if app_state.sidenav_open else SIDENAV_MIN_WIDTH,
            ),
        ),
    ):
        with me.box(
            style=me.Style(
                background=me.theme_var("background"),
                height="100%",
                overflow_y="scroll",
                margin=me.Margin(bottom=20),
            )
        ):
            me.slot()
