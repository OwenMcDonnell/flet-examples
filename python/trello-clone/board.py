from turtle import color
from flet import (
    Column,
    Row,
    FloatingActionButton,
    Text,
    Checkbox,
    Switch,
    Container,
    TextField,
    TextButton,
    AlertDialog,
    Container,
    Switch,
    RadioGroup,
    Radio,
    Page,
    Icon,
    icons,
    border_radius,
    border,
    colors,
    padding,
    alignment,
    margin
)
from board_list import BoardList


class Board:
    def __init__(self, app, identifier: str):
        self.app = app
        self.identifier = identifier  # enforce uniqueness?
        self.boardListsHash = {}

        self.switch = Switch(
            label="Horizontal/Veritcal List View", value=False, label_position="left", on_change=self.toggle_view)
        self.boardListsHorizontal = Column(
            [
                FloatingActionButton(
                    icon=icons.ADD, text="add a list", height=30, on_click=self.addListDlg)
            ],
            # vertical_alignment="start",
            wrap=True,
            visible=False
        )
        self.boardListsVertical = Row(
            [
                FloatingActionButton(
                    icon=icons.ADD, text="add a list", height=30, on_click=self.addListDlg)
            ],
            vertical_alignment="start",
            wrap=True,
            # width=self.app.page.window_width
        )
        self.mainView = Column(
            controls=[
                self.switch,
                self.boardListsHorizontal,
                self.boardListsVertical
            ])

    def toggle_view(self, e):
        self.boardListsHorizontal.visible = e.control.value
        self.boardListsVertical.visible = not e.control.value
        for l in self.boardListsHash.values():
            l[0].visible = e.control.value
            l[1].visible = not e.control.value
        self.app.update()
        # self.mainView.update()

    def addList(self, list: BoardList):
        self.boardLists.append(list)
        # self.buildMainView(self.switch.value)
        self.app.update()

    def addListDlg(self, e):

        optionDict = {
            colors.RED_200: self.colorOptionCreator(colors.RED_200, "red"),
            colors.LIGHT_GREEN: self.colorOptionCreator(colors.LIGHT_GREEN, "green"),
            colors.LIGHT_BLUE: self.colorOptionCreator(colors.LIGHT_BLUE, "blue"),
            colors.ORANGE_300: self.colorOptionCreator(
                colors.ORANGE_300, "orange")
        }

        def set_color(e):
            chosenColor = e.control.data
            colorOptions.data = chosenColor
            print("colorOptions.data: ", colorOptions.data)
            #colorDisplay.value = f"Your chosen color: {colorOptions.data}"
            for k, v in optionDict.items():
                if k == e.control.data:
                    v.bgcolor = colors.BLACK12
                    #v.border = border.all(3, colors.BLACK26)
                    v.border_radius = border_radius.all(100)
                else:
                    v.bgcolor = None
            #optionDict[e.control.data].border = border.all(1, colors.BLACK26)
            dialog.content.update()
            # colorOptions.update()
            # self.app.update()

        #colorDisplay = Text(value="")
        colorOptions = Row(data="")

        for k, v in optionDict.items():
            colorOptions.controls.append(
                TextButton(
                    content=v,
                    on_click=set_color,
                    data=k
                )
            )

        def close_dlg(e):
            if (e.control.value in self.boardListsHash):
                print("duplicate list")
                return
            newListHorizontal = BoardList(
                self, e.control.value, True, colorOptions.data)
            newListVertical = BoardList(
                self, e.control.value, False, colorOptions.data)
            self.boardListsHash[e.control.value] = (
                newListHorizontal, newListVertical)
            print("self.boardListsHash: ", self.boardListsHash)

            self.boardListsHorizontal.controls.insert(
                len(self.boardListsHash) - 1, newListHorizontal.view)
            self.boardListsVertical.controls.insert(
                len(self.boardListsHash) - 1, newListVertical.view)

            self.mainView.update()

            self.app.update()
            dialog.open = False

            self.app.page.update()
        #colorOptions = self.createColorChoice()
        dialog = AlertDialog(
            title=Text("Name your new list"),
            content=Column(
                [Container(content=TextField(label="New List Name", on_submit=close_dlg), padding=padding.symmetric(horizontal=5)), colorOptions], tight=True),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.app.page.dialog = dialog
        dialog.open = True
        self.app.page.update()

    def removeList(self, list: BoardList, e):
        blTuple = self.boardListsHash.pop(list.title)
        self.boardListsHorizontal.controls.remove(blTuple[0].view)
        self.boardListsVertical.controls.remove(blTuple[1].view)
        self.mainView.update()

    def editListTitle(self, list: BoardList):
        print("edit list title: ", list.header)
        list.header.controls[0] = list.editField
        list.header.controls[1].visible = False
        list.header.controls[2].visible = False
        list.view.update()

    def saveListTitle(self, list: BoardList):
        blTuple = self.boardListsHash[list.title]
        list.title = list.editField.controls[0].value
        list.header.controls[0] = Text(value=list.title, style="titleMedium")
        list.header.controls[1].visible = True
        list.header.controls[2].visible = True
        for bl in blTuple:
            bl.title = list.title
        list.view.update()

    def moveBoard(self, list: BoardList, displacement: int):
        i = self.boardList.index(list)
        listToMove = self.boardList.pop(i)
        self.boardList.insert(i + displacement, list)

    def colorOptionCreator(self, color: str, name: str):

        return Container(
            content=Column(
                [
                    Icon(name=icons.CIRCLE, color=color),
                    Text(
                        value=name,
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
            padding=padding.all(20),
            margin=margin.all(10),
            alignment=alignment.center,
        )

    def createBoardNavDestination(self):
        pass


# colorOptions = Row(controls=[
#             TextButton(
#                 content=Container(
#                     content=Column(
#                         [
#                             Icon(name=icons.CIRCLE, color=colors.AMBER),
#                             Text(
#                                 value="Amber",
#                                 # size=12,
#                                 width=50,
#                                 no_wrap=True,
#                                 text_align="center",

#                                 # color=colors.ON_SURFACE_VARIANT,
#                             ),
#                         ],
#                         # spacing=5,
#                         alignment="center",
#                         horizontal_alignment="center",
#                     ),
#                     bgcolor=colors.ON_BACKGROUND if (
#                         colorDisplay.value == "Amber") else colors.BACKGROUND,
#                     padding=padding.all(10),
#                     alignment=alignment.center,
#                 ),

#                 on_click=set_color,
#                 data="Amber"
#             ),
#             TextButton(
#                 content=Container(
#                     content=Column(
#                         [
#                             Icon(name=icons.CIRCLE, color=colors.TEAL),
#                             # Container(
#                             #     content=Checkbox(),
#                             #     padding=-10,
#                             #     border=border.all(7, colors.BLACK),
#                             #     border_radius=border_radius.all(100)
#                             # )
#                             Text(
#                                 value="Teal",
#                                 # size=12,
#                                 width=50,
#                                 no_wrap=True,
#                                 text_align="center",
#                                 # color=colors.ON_SURFACE_VARIANT,
#                             ),
#                         ],
#                         # spacing=5,
#                         alignment="center",
#                         horizontal_alignment="center",
#                     ),
#                     bgcolor=colors.ON_BACKGROUND if (
#                         colorDisplay.value == "Teal") else colors.BACKGROUND,
#                     padding=padding.all(10),
#                     alignment=alignment.center,
#                 ),

#                 on_click=set_color,
#                 data="Teal"
#             ),
#             TextButton(
#                 content=Container(
#                     content=Column(
#                         [
#                             Icon(name=icons.CIRCLE, color=colors.INDIGO),
#                             Text(
#                                 value="Indigo",
#                                 # size=12,
#                                 width=50,
#                                 no_wrap=True,
#                                 text_align="center",
#                                 # color=colors.ON_SURFACE_VARIANT,
#                             ),
#                         ],
#                         # spacing=5,
#                         alignment="center",
#                         horizontal_alignment="center",
#                     ),
#                     bgcolor=colors.ON_BACKGROUND if (
#                         colorDisplay.value == "Indigo") else colors.BACKGROUND,
#                     padding=padding.all(10),
#                     alignment=alignment.center,
#                 ),

#                 on_click=set_color,
#                 data="Indigo"
#             )

#         ], data="")
