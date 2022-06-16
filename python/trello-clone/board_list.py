from flet import (
    Column,
    Row,
    Switch,
    Checkbox,
    Text,
    FloatingActionButton,
    Container,
    TextButton,
    TextField,
    Card,
    icons,
    border_radius,
    colors,
    padding,
    margin
)


class BoardList:
    def __init__(self, board, title: str):
        self.board = board
        self.title = title
        self.cardInput = TextField(label="new card name", width=200)
        self.cardList = Column([
            self.cardInput,
            TextButton("add card", icon=icons.ADD, on_click=self.addCard)
        ])
        #self.view = self.buildList()
        self.view = Column([
            Text(value=self.title, style="titleMedium"),
            Container(
                content=self.cardList,
                border_radius=border_radius.all(15),
                bgcolor=colors.WHITE24,
                padding=padding.all(20),
            )
        ])

    def addCard(self, e):
        self.cardList.controls.append(Checkbox(label=self.cardInput.value))
        self.cardInput.value = ""
        self.view.update()

    def buildList(self):
        return Container(
            content=Column(controls=self.cardList, expand=True),
            border_radius=border_radius.all(15),
            bgcolor=colors.WHITE24,
            padding=padding.all(20),
            margin=margin.all(10),
        )
