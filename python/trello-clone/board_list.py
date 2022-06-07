from board import Board


class BoardList:
    def __init__(self, app, board: Board, title: str):
        self.app = app
        self.board = board
        self.title = title
        self.cardList = []

    def addCard(self, card):
        self.cardList.append(card)
