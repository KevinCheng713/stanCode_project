"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constant
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        self.paddle_offset = PADDLE_OFFSET
        self.paddle_width = PADDLE_WIDTH
        self.paddle_height = PADDLE_HEIGHT
        self._dx = 0
        self._dy = 0
        self.death = 0
        self.num_lives = 3
        self.score = 0

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window_width-paddle_width)/2,
                        y=self.window_height - self.paddle_offset - self.paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window_width-self.ball.width)/2, y=(self.window_height-self.ball.height)/2)
        self.initial_position_x = self.ball.x
        self.initial_position_y = self.ball.y

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.launch)
        onmousemoved(self.move_paddle)

        # Draw bricks
        color = ['red', 'orange', 'yellow', 'green', 'blue']
        for i in range(brick_rows):
            bricks_position_y = brick_offset + i * (brick_height + brick_spacing)
            for j in range(brick_cols):
                bricks_position_x = j * (brick_width + brick_spacing)
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                self.bricks.fill_color = color[i//2]
                self.window.add(self.bricks, x=bricks_position_x, y=bricks_position_y)

        # Create a scorecard
        self.score_label = GLabel('Score: ' + str(self.score))
        self.score_label.font = '-30'
        self.score_label.color = 'purple'
        self.window.add(self.score_label, x=0, y=self.window_height)

    def launch(self, m):
        """The onmouseclicked function only works if the ball is in the middle and the initial velocity is zero.
           Click the mouse to launch the ball"""
        if self.ball.x == self.initial_position_x and self.ball.y == self.initial_position_y:
            """  if self.window.get_object_at(m.x, m.y) is not None or \
                    self.window.get_object_at(m.x, m.y) is None: """
            if self._dx == 0 or self._dy == 0:
                self._dx = random.randint(1, MAX_X_SPEED)
                self._dy = INITIAL_Y_SPEED
                if random.random() > 0.5:  # Make the ball doesn't move in the same direction every time
                    self._dx = -self._dx
                self.ball.move(self._dx, self._dy)

    def move_paddle(self, m):  # The mouse controls the movement of the paddle from left to right
        if m.x < self.paddle.width/2:
            self.paddle.x = 0
        elif m.x > self.window_width - self.paddle.width/2:
            self.paddle.x = self.window_width - self.paddle.width
        else:
            self.paddle.x = m.x - self.paddle.width / 2
            self.paddle.y = self.window_height - self.paddle_offset - self.paddle_height

    def get_dx(self):  # Getter
        return self._dx

    def get_dy(self):  # Getter
        return self._dy

    def bounce(self):  # The ball bounces when it hits an obstacle
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window_width:  # If the ball hits the far left or right, it bounces
            self._dx = -self._dx
        if self.ball.y <= 0:  # If the ball hits the ceiling, it bounces
            self._dy = -self._dy
        if (self.ball.y + self.ball.height >= self.paddle.y) and \
                (self.window.get_object_at(self.ball.x + self.ball.width,
                                           self.ball.y + self.ball.height) is self.paddle)\
                and self._dy > 0:
            self._dy = -self._dy
        if self.ball.y <= self.window.height / 2:
            if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
                self._dx = -self._dx
                self._dy = -self._dy
                self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
                self.add_score()
            elif self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height) is not None:
                self._dx = -self._dx
                self._dy = -self._dy
                self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height))
                self.add_score()
            elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y) is not None:
                self._dx = -self._dx
                self._dy = -self._dy
                self.window.remove(self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y))
                self.add_score()
            elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height) is not None:
                self._dx = -self._dx
                self._dy = -self._dy
                self.window.remove(self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height))
                self.add_score()

    def add_score(self):
        # Each time when an obstacle is removed, the score is increased and the text content of GLabel is updated
        self.score += 1
        self.score_label.text = 'Score:', self.score

    def restart(self):  # When the ball disappears from the window, add a new ball in the center of the window
        if self.ball.y >= self.window.height:
            self.death += 1
            if self.death >= self.num_lives:
                failure = GLabel('Game over!', x=self.window_width/4, y=self.window_height/2)
                failure.font = '-40'
                failure.color = 'red'
                self.window.add(failure)
            else:
                self.window.add(self.ball, x=(self.window_width - self.ball.width) / 2,
                                y=(self.window_height - self.ball.height) / 2)
                self._dx = 0
                self._dy = 0

    def win(self):  # Game victory condition
        if self.score >= BRICK_ROWS * BRICK_COLS:
            win = GLabel('You win!', x=self.window_width / 4, y=self.window_height / 2)
            win.font = '-40'
            win.color = 'red'
            self.window.add(win)





