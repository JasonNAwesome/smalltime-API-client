#!/usr/bin/env python3
import curses, sys

def param_get(_output_string):
    stdscr.erase()
    stdscr.border(0)
    stdscr.addstr(2,2,_output_string)

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.start_color()
WHITE = curses.COLOR_WHITE
BLUE = curses.COLOR_BLUE
curses.init_pair(1, WHITE, BLUE)
curses.curs_set(0)
stdscr.attron(curses.color_pair(1))
stdscr.getch()


stdscr.clear
stdscr.border(0)
stdscr.addstr(3,3,"Choose a choice:")
stdscr.addstr(5,5,"1) RA RA RA")
stdscr.addstr(6,5,"2) Prooal and alks")
stdscr.refresh()

n = stdscr.getch()

if n == ord('1'):
    param_get("Wow you said RA")
elif n == ord('2'):
    param_get("Yes")

stdscr.getch()

curses.endwin()
sys.exit()
