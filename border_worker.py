import typing as typ

from terminaltables import AsciiTable


class Board:
    @classmethod
    def str_board(cls, board: typ.List[typ.List[int]]) -> str:
        def board_element(cell: int) -> str:
            if cell == 0:
                return '   '
            if cell == -1:
                return ' X '
            if cell == 1:
                return ' O '

        board = [[board_element(cell) for cell in row] for row in board]
        table = AsciiTable(board)
        table.inner_row_border = True
        return table.table

    @classmethod
    def init_board(cls, board_size: int) -> typ.List[typ.List[int]]:
        return [[0 for _ in range(board_size)] for _ in range(board_size)]

    @classmethod
    def check_winner(cls, board: typ.List[typ.List[int]]) -> int:
        board_size = len(board)

        if board[0][0] and all(el == board[0][0] for el in [board[i][i] for i in range(board_size)]):
            return board[0][0]
        if board[-1][0] and all(el == board[-1][0] for el in [board[i][-1 - i] for i in range(board_size)]):
            return board[board_size - 1][0]

        for row in board:
            if row[0] and all(el == row[0] for el in row):
                return row[0]
        for i in range(board_size):
            col = [board[j][i] for j in range(board_size)]
            if col[0] and all(el == col[0] for el in col):
                return col[0]
        return 0