from ChessPiece import ChessPiece
import sys


class Bing(ChessPiece):

    def get_image_file_name(self):
        if self.selected:
            if self.is_red:
                return "/home/chy/cchess-zero-master/images/RPS.GIF"
            else:
                return "/home/chy/cchess-zero-master/images/BPS.GIF"
        else:
            if self.is_red:
                return "/home/chy/cchess-zero-master/images/RP.GIF"
            else:
                return "/home/chy/cchess-zero-master/images/BP.GIF"

    def get_selected_image(self):
        if self.is_red:
            return "/home/chy/cchess-zero-master/images/RPS.GIF"
        else:
            return "/home/chy/cchess-zero-master/images/BPS.GIF"

    def can_move(self, board, dx, dy):
        if abs(dx) + abs(dy) != 1:
            # print('Too far')
            return False
        if (self.is_north() and dy == -1) or (self.is_south() and dy==1):
            # print('cannot go back')
            return False
        if dy == 0:
            if (self.is_north() and self.y <5) or (self.is_south() and self.y >=5):
                # print('behind river')
                return False
        nx, ny = self.x + dx, self.y + dy
        if nx < 0 or nx > 8 or ny < 0 or ny > 9:
            return False
        if (nx, ny) in board.pieces:
            if board.pieces[nx, ny].is_red == self.is_red:
                # print('blocked by yourself')
                return False
            else:
                pass
                #print 'kill a chessman'
        return True

    def __init__(self, x, y, is_red, direction):
        ChessPiece.__init__(self, x, y, is_red, direction)

    def display(self):
        sys.stdout.write('B')
