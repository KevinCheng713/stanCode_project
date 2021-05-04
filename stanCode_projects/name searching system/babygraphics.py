"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_coordinate = int(width // len(YEARS)) * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for i in range(len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(width=CANVAS_WIDTH-2 * GRAPH_MARGIN_SIZE, year_index=i), 0,
                           GRAPH_MARGIN_SIZE + get_x_coordinate(width=CANVAS_WIDTH-2 * GRAPH_MARGIN_SIZE, year_index=i), CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(width=CANVAS_WIDTH-2 * GRAPH_MARGIN_SIZE, year_index=i) + TEXT_DX,
                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE + TEXT_DX, text=str(YEARS[i]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        for j in range(len(YEARS)-1):
            year = YEARS[j]
            year_next = YEARS[j+1]

            if str(year) in name_data[name]:
                rank = name_data[name][str(year)]
                rank = int(rank)
            else:
                rank = 1001
            if str(year_next) in name_data[name]:
                rank_next = name_data[name][str(year_next)]
                rank_next = int(rank_next)
            else:
                rank_next = 1001

            """
            Divided into four groups based on whether they fall within the ranking 1,000th 
            this year and in the next decade
            """
            if name in name_data:
                if rank <= 1000 and rank_next <= 1000:
                    canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(width=CANVAS_WIDTH-2 * GRAPH_MARGIN_SIZE, year_index=j),
                                       GRAPH_MARGIN_SIZE + rank * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000,
                                       GRAPH_MARGIN_SIZE + get_x_coordinate(width=CANVAS_WIDTH-2 * GRAPH_MARGIN_SIZE, year_index=j+1),
                                       GRAPH_MARGIN_SIZE + rank_next * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000,
                                       width=LINE_WIDTH, fill=COLORS[i % len(COLORS)])
                    canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(width=CANVAS_WIDTH-2 * GRAPH_MARGIN_SIZE, year_index=j) + TEXT_DX,
                                       GRAPH_MARGIN_SIZE + rank * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000,
                                       text=name + ' ' + str(rank), anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])

                elif rank <= 1000 and rank_next > 1000:
                    canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(width=CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, year_index=j),
                                       GRAPH_MARGIN_SIZE + rank * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000,
                                       GRAPH_MARGIN_SIZE + get_x_coordinate(width=CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, year_index=j + 1),
                                       GRAPH_MARGIN_SIZE + rank_next * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000,
                                       width=LINE_WIDTH, fill=COLORS[i % len(COLORS)])
                    canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(width=CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, year_index=j) + TEXT_DX,
                                       GRAPH_MARGIN_SIZE + rank * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000,
                                       text=name + ' ' + str(rank), anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])

                elif rank > 1000 and rank_next <= 1000:
                    canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(width=CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, year_index=j),
                                       GRAPH_MARGIN_SIZE + rank * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000,
                                       GRAPH_MARGIN_SIZE + get_x_coordinate(width=CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, year_index=j + 1),
                                       GRAPH_MARGIN_SIZE + rank_next * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000,
                                       width=LINE_WIDTH, fill=COLORS[i % len(COLORS)])
                    canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(width=CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, year_index=j) + TEXT_DX,
                                       GRAPH_MARGIN_SIZE + rank * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000,
                                       text=name + ' *', anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])

                elif rank > 1000 and rank_next > 1000:
                    canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(width=CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, year_index=j),
                                       GRAPH_MARGIN_SIZE + rank * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000,
                                       GRAPH_MARGIN_SIZE + get_x_coordinate(width=CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, year_index=j + 1),
                                       GRAPH_MARGIN_SIZE + rank_next * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000,
                                       width=LINE_WIDTH, fill=COLORS[i % len(COLORS)])
                    canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(width=CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, year_index=j) + TEXT_DX,
                                       GRAPH_MARGIN_SIZE + rank * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000,
                                       text=name + ' *', anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])

        """
        Add the babynames-2010 ranking text
        """
        if str(YEARS[-1]) in name_data[name]:
            rank = int(name_data[name][str(YEARS[-1])])
            canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(width=CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, year_index=len(YEARS)-1) + TEXT_DX,
                               GRAPH_MARGIN_SIZE + rank * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000,
                               text=name + ' ' + str(rank), anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
        else:
            rank = 1001
            canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(width=CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, year_index=len(YEARS)-1) + TEXT_DX,
                               GRAPH_MARGIN_SIZE + rank * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000,
                               text=name + ' *', anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])


        # main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
