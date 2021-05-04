"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# Constant
FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add animation loop here!
    while True:
        pause(FRAME_RATE)
        graphics.bounce()
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        graphics.restart()
        graphics.win()
        if graphics.score >= 100:  # 之後把100改成磚塊行列數乘積
            break
        if graphics.death >= NUM_LIVES:
            break


if __name__ == '__main__':
    main()
