import mesop as me

from state.state import AppState
from components.styles import (
    SIDENAV_MAX_WIDTH,
    SIDENAV_MIN_WIDTH,
    _FANCY_TEXT_GRADIENT,
)


def on_sidenav_menu_click(e: me.ClickEvent):
    state = me.state(AppState)
    state.sidenav_open = not state.sidenav_open


def sidenav(current_page: str):
    app_state = me.state(AppState)
    print(f"received current page: {current_page}")
    with me.sidenav(
        opened=True,
        style=me.Style(
            width=SIDENAV_MAX_WIDTH if app_state.sidenav_open else SIDENAV_MIN_WIDTH,
            background=me.theme_var("secondary-container")
        ),
    ):
        with me.box(
            style=me.Style(
                margin=me.Margin(top=16, left=16, right=16, bottom=16), 
                display="flex", 
                flex_direction="column",
                gap=5,
            ),
        ):
            with me.box(
                style=me.Style(
                    display="flex", 
                    flex_direction="row",
                    gap=5,
                    align_items="center",
                ),
            ):
                with me.content_button(
                    type="icon", 
                    on_click=on_sidenav_menu_click,
                ):
                    with me.box():
                        with me.tooltip(message="Expand menu"):
                            me.icon(icon="menu")
                if app_state.sidenav_open:
                    me.text("APP SCAFFOLD", style=_FANCY_TEXT_GRADIENT)
            me.box(style=me.Style(height=16))

