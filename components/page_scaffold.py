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


@me.content_component
def page_frame():
    """Page Frame"""
    with me.box(style=MAIN_COLUMN_STYLE):
        with me.box(style=PAGE_BACKGROUND_STYLE):
            with me.box(style=PAGE_BACKGROUND_PADDING_STYLE):
                me.slot()


MAIN_COLUMN_STYLE = me.Style(
    display="flex",
    flex_direction="column",
    height="100%",
)

PAGE_BACKGROUND_STYLE = me.Style(
    background=me.theme_var("background"),
    height="100%",
    overflow_y="scroll",
    margin=me.Margin(bottom=20),
)

PAGE_BACKGROUND_PADDING_STYLE = me.Style(
    background=me.theme_var("background"),
    padding=me.Padding(top=24, left=24, right=24, bottom=24),
    display="flex",
    flex_direction="column",
)
