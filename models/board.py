class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]
    


    def draw_board(self, board):
        """
        Draw the board of a Tic-Tac-Toe game.
        This function takes a 2D list representing the Tic-Tac-Toe board and prints it in a formatted way.
        Empty cells are represented by spaces, and cells occupied by players are represented by 'X' or 'O'.
        Args:
            board (list of list of str): A 2D list representing the Tic-Tac-Toe board. Each element should be 'X', 'O', or an empty string.
        Returns:
            None
        """

        def regular_board(n1, n2, board):
            for i in range(n1):
                for j in range(n2):
                    if board[i][j] != 'X' and board[i][j] != 'O':
                        board[i][j] = ' '
            return board
    
        if not board:
            return
        n1 = len(board)
        n2 = len(board[0])
        sign1 = " ---"
        sign2 = " | "
        board = regular_board(n1, n2, board)
        for i in range(n1):
            print(" "+sign1 * n2)
            print("".join([sign2+x for x in board[i]])+sign2)
        print(" "+sign1 * n2)
        return 


    def update_board(self, row: int, col: int, symbol: str) -> bool:
        """
        Update the game board based on location selected by player

        Args:
            row (int): row index of board
            col (int): column index of board
            symbol (str): symbol used by player
        """
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self, board) -> str:
        """
        Check the winner of the current board

        Returns:
            str: The winning symbol ('X' or 'O') if there is a winner, else an empty string
        """
        def sameLine(sign1, sign2, sign3):
            return (sign1 == 'X' or sign1 == 'O') and sign1 == sign2 and sign2 == sign3
        
        for i in range(3):
            if sameLine(board[i][0], board[i][1], board[i][2]):
                return board[i][0]
            if sameLine(board[0][i], board[1][i], board[2][i]):
                return board[0][i]
        if sameLine(board[0][0], board[1][1], board[2][2]):
            return board[0][0]
        if sameLine(board[0][2], board[1][1], board[2][0]):
            return board[0][2]
        return None




    def is_full(self) -> bool:
        """
        Check if the current board is full or not

        Returns:
            bool: Boolean outcome indicating whether the board is full
        """
        return all(cell != " " for row in self.grid for cell in row)
