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
from components.page_scaffold import page_scaffold
from pages.home import home_page_content
from pages.another import another_content
#from pages.gemini2 import gemini_page_content


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


# @me.page(
#     path="/gemini",
#     title="Scaffold - Gemini",
#     on_load=on_load,
# )
# def gemini_page():
#     """Gemini 2.0 Flash Page"""
#     state = me.state(AppState)
#     with page_scaffold():  # pylint: disable=not-context-manager
#         gemini_page_content(state)
