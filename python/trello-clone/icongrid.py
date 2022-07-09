
import flet
from flet import (
    Column,
    Container,
    Checkbox,
    alignment,
    padding,
    ElevatedButton,
    Radio,
    RadioGroup,
    GridView,
    Text,
    TextButton,
    Row,
    Icon,
    colors,
    icons)


def main(page):
    options = Row(controls=[
        TextButton(
            content=Container(
                content=Column(
                    [
                        Icon(name=icons.CIRCLE, color=colors.AMBER),
                        Text(
                            value="Amber",
                            # size=12,
                            width=50,
                            no_wrap=True,
                            text_align="center",
                            # color=colors.ON_SURFACE_VARIANT,
                        ),
                    ],
                    # spacing=5,
                    alignment="center",
                    horizontal_alignment="center",
                ),
                padding=padding.all(10),
                alignment=alignment.center,
            ),

            # on_click=copy_to_clipboard,
            data="icons.CIRCLE"
        ),
        TextButton(
            content=Container(
                content=Column(
                    [
                        Icon(name=icons.CIRCLE, color=colors.TEAL),
                        # Container(
                        #     content=Checkbox(),
                        #     padding=-10,
                        #     border=border.all(7, colors.BLACK),
                        #     border_radius=border_radius.all(100)
                        # )
                        Text(
                            value="Teal",
                            # size=12,
                            width=50,
                            no_wrap=True,
                            text_align="center",
                            # color=colors.ON_SURFACE_VARIANT,
                        ),
                    ],
                    # spacing=5,
                    alignment="center",
                    horizontal_alignment="center",
                ),
                padding=padding.all(10),
                alignment=alignment.center,
            ),

            # on_click=copy_to_clipboard,

            data="icons.CIRCLE"
        ),
        TextButton(
            content=Container(
                content=Column(
                    [
                        Icon(name=icons.CIRCLE, color=colors.INDIGO),
                        Text(
                            value="Indigo",
                            # size=12,
                            width=50,
                            no_wrap=True,
                            text_align="center",
                            # color=colors.ON_SURFACE_VARIANT,
                        ),
                    ],
                    # spacing=5,
                    alignment="center",
                    horizontal_alignment="center",
                ),
                padding=padding.all(10),
                alignment=alignment.center,
            ),

            # on_click=copy_to_clipboard,
            data="icons.CIRCLE"
        )

    ])

    page.add(Text("Select a color for your list:"), options)


flet.app(target=main)
