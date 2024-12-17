import mesop as me

from state.state import AppState
from components.header import header


@me.stateclass
class PageState:
    temp_name: str = ""


def on_blur_set_name(e: me.InputBlurEvent):
    """input handler"""
    state = me.state(PageState)
    state.temp_name = e.value


def on_click_change_name(e: me.ClickEvent):
    """change name button handler"""
    state = me.state(PageState)
    app_state = me.state(AppState)
    app_state.name = state.temp_name
    yield


def home_page_content(app_state: me.state):
    with me.box(
        style=me.Style(
            display="flex",
            flex_direction="column",
            height="100%",
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
            with me.box(
                style=me.Style(
                    background=me.theme_var("background"),
                    padding=me.Padding(top=24, left=24, right=24, bottom=24),
                    display="flex",
                    flex_direction="column",
                )
            ):
                header("Home Page", "home")

                me.text(f"Hello, {app_state.name}!")
                me.input(
                    label="change the name",
                    on_blur=on_blur_set_name,
                    on_enter=on_click_change_name,
                )
                me.button(
                    label="change",
                    type="flat",
                    on_click=on_click_change_name,
                )
