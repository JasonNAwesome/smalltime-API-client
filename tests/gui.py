#!/usr/bin/env python3
import curses, sys

# output
def param_get(_output_string):
    stdscr.erase()
    stdscr.border(0)
    stdscr.addstr(2,2,_output_string)
    stdscr.hline(int(y_length/2),0,'#',x_length)

stdscr = curses.initscr()

yx_tuple = stdscr.getmaxyx()
y_length = yx_tuple[0]
x_length = yx_tuple[1]

# color
curses.start_color()
WHITE = curses.COLOR_WHITE
BLUE = curses.COLOR_BLUE
curses.init_pair(1, WHITE, BLUE)
curses.curs_set(0)
stdscr.attron(curses.color_pair(1))

# wait
stdscr.getch()


stdscr.clear
stdscr.border(0)
stdscr.addstr(3,3,"Choose a choice:")
stdscr.addstr(5,5,"1) Row & Col")
stdscr.addstr(6,5,"2) None")
stdscr.refresh()

n = stdscr.getch()

if n == ord('1'):
    phrase = "Row:" + str(yx_tuple[0]) + " Col:" + str(yx_tuple[1])
    param_get(phrase)
elif n == ord('2'):
    param_get("Ok.")

stdscr.getch()

curses.endwin()
sys.exit()
