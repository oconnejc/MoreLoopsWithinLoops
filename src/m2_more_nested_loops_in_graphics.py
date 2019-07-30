"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Joe OConnell.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------

    rectangle.attach_to(window)
    window.render()
    ogp1x = rectangle.corner_1.x
    ogp1y = rectangle.corner_1.y
    ogp2x = rectangle.corner_2.x
    ogp2y = rectangle.corner_2.y
    width = abs(ogp1x-ogp2x)
    height = abs(ogp1y-ogp2y)
    for k in range(n-1):
        rectangle.corner_1.x = ogp1x + .5 * width * (k+1)
        rectangle.corner_2.x = ogp2x + .5 * width* (k+1)
        rectangle.corner_1.y = ogp1y - height * (k+1)
        rectangle.corner_2.y = ogp2y - height * (k+1)
        rectangle.attach_to(window)
        window.render()
        for i in range(k+1):
            rectangle.corner_1.x = rectangle.corner_1.x - width
            rectangle.corner_2.x = rectangle.corner_2.x - width
            rectangle.attach_to(window)
            window.render()
        window.render()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
