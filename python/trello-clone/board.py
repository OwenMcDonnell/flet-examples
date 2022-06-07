from board_list import BoardList


class Board:
    def __init__(self, app, identifier: str):
        self.app = app
        self.identifier = identifier
        self.boardList: list[BoardList] = []

    def addList(self, list: BoardList):
        self.boardList.append(list)

    def removeList(self, list: BoardList):
        self.boardList.remove(list)

    def moveBoard(self, list: BoardList, displacement: int):
        i = self.boardList.index(list)
        listToMove = self.boardList.pop(i)
        self.boardList.insert(i + displacement, list)

    def createBoardNavDestination(self):
        pass
