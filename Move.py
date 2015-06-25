from Piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King

class Move(object):
    """Contains all the move methods"""
    def __init__(self):
        pass

    def set_new_game(self):
        """
        Initializes pieces for a new chess game.
        Uses two for loops and if/else statements to set the pieces.
        """
        board = []
        A, B, C, D, E, F, G, H = range(8), range(8), range(8), range(8), range(8), range(8), range(8), range(8) # Feels unpythonic but can't do A = B = C = ... = range(8) since lists are mutable
        board.extend([A, B, C, D, E, F, G, H])

        for row in xrange(8):
            for col in xrange(8):
                if col == 1:
                    board[row][col] = Pawn(False, 'White')

                elif col == 6:
                    board[row][col] = Pawn(False, 'Black')

                elif col in range(2,7):
                    board[row][col] = Piece()

                elif col == 0:
                    if row == 0 or row == 7:
                        board[row][col] = Rook(False, 'White')

                    elif row == 1 or row == 6:
                        board[row][col] = Knight(False, 'White')

                    elif row == 2 or row == 5:
                        board[row][col] = Bishop(False, 'White')

                    elif row == 3:
                        board[row][col] = Queen(False, 'White')

                    else:
                        board[row][col] = King(False, 'White')

                else:
                    if row == 0 or row == 7:
                        board[row][col] = Rook(False, 'Black')

                    elif row == 1 or row == 6:
                        board[row][col] = Knight(False, 'Black')

                    elif row == 2 or row == 5:
                        board[row][col] = Bishop(False, 'Black')

                    elif row == 3:
                        board[row][col] = Queen(False, 'Black')

                    else:
                        board[row][col] = King(False, 'Black')

        return board

    def move(self):
        """Consolidates move methods"""
        wanted = self.get_move()
        self.apply_move(wanted[0], wanted[1])

    def get_move(self):
        """
        Prompts user for desired move. Only using numerical coordinates for now.
        Stores from and to coordinates in tuples. Returns a tuple of these tuples."
        Input is basic now, eg. 12 is parsed as (1, 2)
        """
        piece_from = tuple(i for i in raw_input("From?"))
        piece_to = tuple(i for i in raw_input("To?"))

        print "Moving from {0} to {1}".format(piece_from, piece_to)
        piece_from, piece_to = self.anum_to_cart(piece_from, piece_to)

        legal = self.main_board[piece_from[0]][piece_from[1]].move_set(piece_from,self.main_board)
        for i in legal:   # List of legal moves for testing
            print self.cart_to_anum(i),

        return (piece_from, piece_to)

    def apply_move(self, piece_from, piece_to):
        """Rudimentary move function for now"""
        self.main_board[piece_to[0]][piece_to[1]] = self.main_board[piece_from[0]][piece_from[1]]  # Moves piece
        self.main_board[piece_from[0]][piece_from[1]] = Piece()  # Makes old location empty

    def anum_to_cart(self, piece_from, piece_to):
        """
        Converts board coordinate input--eg. 'A5' to cartesian coordinates.
        Takes the two movement tuples, converts, then returns a single tuple
        """
        atoi = {
            'A' : 0,
            'B' : 1,
            'C' : 2,
            'D' : 3,
            'E' : 4,
            'F' : 5,
            'G' : 6,
            'H' : 7
        }

        piece_from = (atoi[piece_from[0]], int(piece_from[1]) - 1)  # -1 since counting starts from 0 not 1
        piece_to = (atoi[piece_to[0]], int(piece_to[1]) - 1)

        return (piece_from, piece_to)

    def cart_to_anum(self, piece):
        """Converts from array coordinates to board coordinates for testing purposes"""
        itoa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        piece = (itoa[piece[0]], piece[1] + 1)
        return piece
