import mesop as me

from components.header import header
from components.page_scaffold import (
    page_scaffold,
    page_frame,
)


def another_content(app_state: me.state):
    """Another Mesop Page"""
    with page_scaffold():  # pylint: disable=not-context-manager
        with page_frame():
            header("Another Page", "looks_two")

            me.text(f"Hello, {app_state.name}!")
