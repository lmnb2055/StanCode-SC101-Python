"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 90     # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout',):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle

        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.paddle.color = 'black'
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius, x=(window_width-ball_radius*2)/2, y=(window_height-ball_radius*2)/2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.ball.color = 'black'
        self.window.add(self.ball)
        # Original
        self.origin_x = (window_width-ball_radius*2) / 2
        self.origin_y = (window_height-ball_radius*2) / 2
        # count
        self.count = 0
        self.count_bricks = 0
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmousemoved(self.moving)
        onmouseclicked(self.ball_moving)
        # Draw bricks
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                color = ['red', 'red', 'orange', 'orange', 'yellow', 'yellow', 'green', 'green', 'blue', 'blue']
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                self.bricks.fill_color = color[j]
                self.bricks.color = color[j]
                self.window.add(self.bricks, x=i*(BRICK_WIDTH+BRICK_SPACING),
                                y=BRICK_OFFSET+j*(BRICK_HEIGHT+brick_spacing))
        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))
        self.score_label.font = '-30'
        self.window.add(self.score_label, x=0, y=self.window.height)

    def moving(self, mouse):
        if mouse.x < PADDLE_WIDTH / 2:
            self.paddle.x = 0
        elif mouse.x > self.window.width-PADDLE_WIDTH/2:
            self.paddle.x = self.window.width-PADDLE_WIDTH
        else:
            self.paddle.x = mouse.x - PADDLE_WIDTH/2

    def ball_moving(self, mouse):
        if self.ball.x == self.origin_x and self.ball.y == self.origin_y:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = - self.__dx

    def get_vx(self):
        return self.__dx

    def set_new_vx(self, new_vx):  # setter都可以
        self.__dx = new_vx

    def get_vy(self):
        return self.__dy

    def set_new_vy(self, new_vy):  # setter都可以
        self.__dy = new_vy

    def move(self):
        self.ball.move(self.get_vx(), self.get_vy())
        if self.ball.x <= 0 or self.ball.x + self.ball.width > self.window.width:
            self.set_new_vx(-self.get_vx())
        if self.ball.y <= 0:
            self.set_new_vy(-self.get_vy())
        # if self.ball.y + self.ball.height > self.window.height:
        #     self.window.remove(self.ball)
        #     self.ball = GOval(BALL_RADIUS, BALL_RADIUS, x=(self.window.width - BALL_RADIUS) / 2,
        #                       y=(self.window.height - BALL_RADIUS) / 2)
        #     self.ball.filled = True
        #     self.ball.fill_color = 'black'
        #     self.ball.color = 'black'
        #     self.window.add(self.ball)

    def collision(self):
        for i in range(2):
            for j in range(2):
                ball_object = self.window.get_object_at(self.ball.x+i*BALL_RADIUS*2, self.ball.y+j*BALL_RADIUS*2)
                if ball_object is not None:
                    if ball_object is self.paddle and self.__dy > 0:
                        self.__dy = - self.__dy
                    elif ball_object is self.score_label:
                        pass
                    else:  # 為什麼這裡用if ball_object is self.bricks 會出錯？
                        self.window.remove(ball_object)
                        self.score += 1
                        self.score_label.text = 'Score: ' + str(self.score)
                        self.set_new_vy(-self.get_vy())
                        self.count_bricks += 1
                    if self.count_bricks == 100:
                        self.window.remove(self.ball)
                        self.window.remove(self.paddle)
                        self.window.remove(self.score_label)
                        win = GLabel('WIN')
                        win.font = '-150'
                        self.window.add(win, x=(self.window.width-win.width)/2,
                                        y=(self.window.height-win.height)/2+win.height)
                        return False
                return True
        return None
        # if self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y + BALL_RADIUS * 2) is not None:
        #     self.set_new_vy(-self.get_vy())
        # elif self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS * 2) is not None:
        #     self.set_new_vy(-self.get_vy())
        # elif self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y) is not None:
        #     self.set_new_vy(-self.get_vy())
        # elif self.window.get_object_at(self.ball.x, self.ball.y) is not None:
        #     self.set_new_vy(-self.get_vy())
        # else:
        #     return None

    def origin(self):
        self.ball = GOval(BALL_RADIUS, BALL_RADIUS, x=(self.window.width-BALL_RADIUS)/2,
                          y=(self.window.height-BALL_RADIUS)/2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.ball.color = 'black'
        self.window.add(self.ball)

    def again(self):
        if self.ball.y > self.window.height:
            if self.count == 2:
                self.__dx = 0
                self.__dy = 0
                self.window.remove(self.paddle)
                game_over = GLabel('GAME OVER')
                game_over.font = '-80'
                self.window.add(game_over, x=(self.window.width - game_over.width) / 2,
                                y=(self.window.height - game_over.height) / 2 + game_over.height)
                return True
            else:
                self.__dx = 0
                self.__dy = 0
                self.window.add(self.ball, self.origin_x, self.origin_y)
                self.count += 1









