"""
File: draw_line
Name:Sidney
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
window = GWindow()
click = 0
x = 0
y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global click, x, y
    if click % 2 == 0:
        pen = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        x = mouse.x  # the original position x
        y = mouse.y  # the original position y
        pen.color = 'black'
        window.add(pen)
        click += 1   # to check how many times my mouse click

    else:
        point = window.get_object_at(x, y)
        window.remove(point)  # remove the black point
        draw_line = GLine(x, y, mouse.x, mouse.y)
        window.add(draw_line)
        click += 1







if __name__ == "__main__":
    main()
