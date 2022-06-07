from flet import (
    Column,
    Row,
    FloatingActionButton,
    Card,
    icons
)


class BoardList:
    def __init__(self, page, title: str):
        self.page = page
        self.title = title
        self.cardList = []
        self.view = Column(controls=[FloatingActionButton(
            icon=icons.ADD, text="add card", on_click=self.addCard)])

    def addCard(self, card):
        self.cardList.append(card)
        self.page.update()
