import mesop as me


@me.stateclass
class AppState:
    """Mesop Application State"""
    sidenav_open: bool = False

    name: str = "no name"