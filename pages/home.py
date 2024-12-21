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
from components.header import header


@me.stateclass
class PageState:
    """ Local Page State"""
    temp_name: str = ""


def on_blur_set_name(e: me.InputBlurEvent):
    """input handler"""
    state = me.state(PageState)
    state.temp_name = e.value


def on_click_change_name(e: me.ClickEvent):  # pylint: disable=unused-argument
    """change name button handler"""
    state = me.state(PageState)
    app_state = me.state(AppState)
    app_state.name = state.temp_name
    yield


def home_page_content(app_state: me.state):
    """Home Page"""
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
                me.box(style=me.Style(height=16))
                with me.box(
                    style=me.Style(
                        display="flex",
                        flex_direction="row",
                        gap=5,
                        align_items="center",
                    )
                ):
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
