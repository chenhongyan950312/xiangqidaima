
from ChessPiece import ChessPiece


class Pao(ChessPiece):

    def get_image_file_name(self):
        if self.selected:
            if self.is_red:
                return "/home/chy/cchess-zero-master/images/RCS.GIF"
            else:
                return "/home/chy/cchess-zero-master/images/BCS.GIF"
        else:
            if self.is_red:
                return "/home/chy/cchess-zero-master/images/RC.GIF"
            else:
                return "/home/chy/cchess-zero-master/images/BC.GIF"

    def get_selected_image(self):
        if self.is_red:
            return "/home/chy/cchess-zero-master/images/RCS.GIF"
        else:
            return "/home/chy/cchess-zero-master/images/BCS.GIF"

    def can_move(self, board, dx, dy):
        if dx != 0 and dy != 0:
            #print 'no diag'
            return False
        nx, ny = self.x + dx, self.y + dy
        if nx < 0 or nx > 8 or ny < 0 or ny > 9:
            return False
        if (nx, ny) in board.pieces:
            if board.pieces[nx, ny].is_red == self.is_red:
                #print 'blocked by yourself'
                return False
        cnt = self.count_pieces(board, self.x, self.y, dx, dy)
        # print 'Pao cnt',cnt
        if (nx, ny) not in board.pieces:
            if cnt!= 0:
                #print 'blocked'
                return False
        else:
            if cnt != 1:
                #print 'cannot kill'
                return False
        return True

    def __init__(self, x, y, is_red, direction):
        ChessPiece.__init__(self, x, y, is_red, direction)

