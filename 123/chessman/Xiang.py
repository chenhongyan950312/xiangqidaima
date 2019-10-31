from ChessPiece import ChessPiece


class Xiang(ChessPiece):

    def get_image_file_name(self):
        if self.selected:
            if self.is_red:
                return "/home/chy/cchess-zero-master/images/RBS.GIF"
            else:
                return "/home/chy/cchess-zero-master/images/BBS.GIF"
        else:
            if self.is_red:
                return "/home/chy/cchess-zero-master/images/RB.GIF"
            else:
                return "/home/chy/cchess-zero-master/images/BB.GIF"

    def get_selected_image(self):
        if self.is_red:
            return "/home/chy/cchess-zero-master/images/RBS.GIF"
        else:
            return "/home/chy/cchess-zero-master/images/BBS.GIF"

    def can_move(self, board, dx, dy):
        x,y = self.x, self.y
        nx, ny = x + dx, y + dy
        if nx < 0 or nx > 8 or ny < 0 or ny > 9:
            return False
        if (nx, ny) in board.pieces:
            if board.pieces[nx, ny].is_red == self.is_red:
                #print 'blocked by yourself'
                return False
        if (self.is_north() and ny > 4) or (self.is_south() and ny <5):
            #print 'no river cross'
            return False

        if abs(dx)!=2 or abs(dy)!=2:
            #print 'not normal'
            return False
        sx, sy = dx/abs(dx), dy/abs(dy)
        if (x+sx, y+sy) in board.pieces:
            #print 'blocked'
            return False
        return True

    def __init__(self, x, y, is_red, direction):
        ChessPiece.__init__(self, x, y, is_red, direction)

