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
        self.boardLists = [
            FloatingActionButton(
                icon=icons.ADD, text="add a list", height=30, on_click=self.addListDlg)
        ]
        self.horizontalWrap = Column(
            self.boardLists,
            # vertical_alignment="start",
            wrap=True,
            visible=self.switch.value
        )
        self.verticalWrap = Row(
            self.boardLists,
            vertical_alignment="start",
            wrap=True,
            visible=(not self.switch.value)
            # width=self.app.page.window_width
        )
        self.mainView = Column(
            controls=[
                self.switch,
                self.horizontalWrap,
                self.verticalWrap
            ])

    # this method should ask the BoardLists to change view
    # for each list in BoardLists list.horizontalView.visible = false, list.verticalView.visible = true
    def toggle_view(self, e):
        print("self.switch.value from change handler: ", self.switch.value)

        # false means horizontal.
        index = 0
        for k, v in self.boardListsHash.items():

            print("horizontal value from hash before: ", v.horizontal)
            #v.horizontal = (not v.horizontal)
            v.toggleView()
            self.boardLists[index] = v.view
            index += 1
            print("horizontal value from hash after: ", v.horizontal)

        # for l in self.boardLists[:-1]:
        #     print("l in self.boardLists: ",
        #           l)
        #     l.controls[1].visible = not l.controls[1].visible
        #     l.controls[2].visible = not l.controls[2].visible
        #     l.update()

        self.horizontalWrap.visible = self.switch.value
        self.verticalWrap.visible = (not self.switch.value)

        # for l in self.boardListsHash.values():
        #     l[0].visible = e.control.value
        #     l[1].visible = not e.control.value
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
            colors.ORANGE_300: self.colorOptionCreator(colors.ORANGE_300, "orange"),
            colors.PINK_300: self.colorOptionCreator(colors.PINK_300, "pink"),
            colors.YELLOW_400: self.colorOptionCreator(colors.YELLOW_400, "yellow"),
        }

        def set_color(e):
            chosenColor = e.control.data
            colorOptions.data = chosenColor
            print("colorOptions.data: ", colorOptions.data)
            for k, v in optionDict.items():
                if k == e.control.data:
                    v.bgcolor = colors.BLACK12
                    #v.border = border.all(3, colors.BLACK26)
                    v.border_radius = border_radius.all(100)
                else:
                    v.bgcolor = None
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
            # if (e.control.value in self.boardListsHash):
            #     print("duplicate list")
            #     return
            # newListHorizontal = BoardList(
            #     self, e.control.value, True, colorOptions.data)
            # newListVertical = BoardList(
            #     self, e.control.value, False, colorOptions.data)
            print("self.switch.value: ", self.switch.value,
                  type(self.switch.value))
            newList = BoardList(self, e.control.value, self.switch.value,
                                color=colorOptions.data)

            self.boardListsHash[e.control.value] = newList
            # self.boardListsHash[e.control.value] = (
            #     newListHorizontal, newListVertical)
            #print("self.boardListsHash: ", self.boardListsHash)
            self.boardLists.insert(-1, newList.view)
            # self.boardListsHorizontal.controls.insert(
            #     len(self.boardListsHorizontal.controls) - 1, newListHorizontal.view)
            # self.boardListsVertical.controls.insert(
            #     len(self.boardListsVertical.controls) - 1, newListVertical.view)
            # self.boardListsHorizontal.controls.insert(
            #     len(self.boardListsHash) - 1, self.boardListsHash[e.control.value][0].view)
            # self.boardListsVertical.controls.insert(
            #     len(self.boardListsHash) - 1, self.boardListsHash[e.control.value][1].view)

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
        #blTuple = self.boardListsHash.pop(list.title)
        # self.boardListsHorizontal.controls = [
        #     i for i in self.boardListsHorizontal.controls[1:] if i.data != list.title]
        # self.boardListsVertical.controls = [
        #     i for i in self.boardListsVertical.controls[1:] if i.data != list.title]
        if list.horizontal:
            index = self.boardListsHorizontal.controls.index(list.view)
        else:
            index = self.boardListsVertical.controls.index(list.view)
        del self.boardListsHorizontal.controls[index]
        del self.boardListsVertical.controls[index]
        self.mainView.update()

    def editListTitle(self, list: BoardList):
        print("edit list title: ", list.header)
        list.header.controls[0] = list.editField
        list.header.controls[1].visible = False
        list.header.controls[2].visible = False

        list.view.update()

    def saveListTitle(self, list: BoardList):
        oldTitle = list.title
        print("oldTitle: ", oldTitle)
        list.title = list.editField.controls[0].value
        print("new editField title: ",
              list.editField.controls[0].value, list.title)
        list.header.controls[0] = Text(value=list.title, style="titleMedium")
        list.header.controls[1].visible = True
        list.header.controls[2].visible = True
        # self.boardListsHash[oldTitle][0].title = list.title
        # self.boardListsHash[oldTitle][1].title = list.title
        # self.boardListsHash[list.title] = self.boardListsHash[oldTitle]
        # del self.boardListsHash[oldTitle]
        # for bl in blTuple:
        #     bl.title = list.title
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
            padding=padding.all(10),
            margin=margin.all(1),
            alignment=alignment.center,
        )

    def createBoardNavDestination(self):
        pass
