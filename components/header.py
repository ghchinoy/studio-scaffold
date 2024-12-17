import mesop as me


@me.component
def header(title: str, icon: str):
    with me.box(
        style=me.Style(
            display="flex",
            justify_content="space-between",
        )
    ):
        with me.box(
            style=me.Style(display="flex", flex_direction="row", gap=5)
        ):
            me.icon(icon=icon)
            me.text(
                title,
                type="headline-5",
                style=me.Style(font_family="Google Sans"),
            )