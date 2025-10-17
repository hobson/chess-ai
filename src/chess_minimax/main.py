from .Board import *
from . import graphics
import sys

DEBUG = '--debug' in sys.argv[1:]


def main(debug=DEBUG):
    print(f'chess-minimax BUT BETTER! running main(debug={debug})')
    keep_playing = True

    board = Board(game_mode=0, ai=True, depth=1, log=True or debug, debug=debug)  # game_mode == 0: whites down / 1: blacks down

    while keep_playing:
        graphics.initialize()
        board.place_pieces()
        graphics.draw_background(board)
        keep_playing = graphics.start(board)


if __name__ == '__main__':
    main(debug=DEBUG)
