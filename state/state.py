import mesop as me


@me.stateclass
class AppState:

    sidenav_open: bool = False
    
    name: str = "no name"