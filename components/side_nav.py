# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import mesop as me
from state.state import AppState
from styles.styles import (
    SIDENAV_MAX_WIDTH,
    SIDENAV_MIN_WIDTH,
    _FANCY_TEXT_GRADIENT,
    DEFAULT_MENU_STYLE,
)


page_json = [
    {"display": "Home", "icon": "home", "route": "/"},
    {"display": "Another", "icon": "looks_two", "route": "/another"},
    {"display": "Gemini", "icon": "auto_awesome", "route": "/gemini"},
]

def on_sidenav_menu_click(e: me.ClickEvent):  # pylint: disable=unused-argument
    """Side navigation menu click handler"""
    state = me.state(AppState)
    state.sidenav_open = not state.sidenav_open

def navigate_to(e: me.ClickEvent):
    """navigate to a specific page"""
    s = me.state(AppState)
    idx = int(e.key)
    print(f"idx: {idx}")
    if idx > len(page_json):
        print(f"requested {idx}, but not in list (len: {len(page_json)})")
        return
    page = page_json[idx]
    print(f"navigating to: {page}")
    s.current_page = page["route"]
    me.navigate(s.current_page)
    yield

@me.component
def sidenav(current_page: str):
    """Render side navigation"""
    app_state = me.state(AppState)
    #print(f"received current page: {current_page}")

    with me.sidenav(
        opened=True,
        style=me.Style(
            width=SIDENAV_MAX_WIDTH if app_state.sidenav_open else SIDENAV_MIN_WIDTH,
            background=me.theme_var("secondary-container"),
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
                    me.text("STUDIO", style=_FANCY_TEXT_GRADIENT)
            me.box(style=me.Style(height=16))
            for idx, page in enumerate(page_json):
                menu_item(
                    idx, page["icon"], page["display"], not app_state.sidenav_open
                )

def menu_item(
    key: int,
    icon: str,
    text: str,
    minimized: bool = True,
    content_style: me.Style = DEFAULT_MENU_STYLE,
):
    """render menu item"""
    if minimized:  # minimized
        with me.box(
            style=me.Style(
                display="flex",
                flex_direction="row",
                gap=5,
                align_items="center",
            ),
        ):
            with me.content_button(
                key=str(key),
                on_click=navigate_to,
                style=content_style,
                type="icon",
            ):
                with me.tooltip(message=text):
                    me.icon(icon=icon)

    else:  # expanded
        with me.content_button(
            key=str(key),
            on_click=navigate_to,
            style=content_style,
        ):
            with me.box(
                style=me.Style(
                    display="flex",
                    flex_direction="row",
                    gap=5,
                    align_items="center",
                ),
            ):
                me.icon(icon=icon)
                me.text(text)
