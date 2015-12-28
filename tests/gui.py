#!/usr/bin/env python3
import curses, sys

screen = curses.initscr()
curses.start_color()


screen.clear
screen.border(0)
screen.addstr(3,3,"Choose a choice:")
screen.addstr(5,5,"1) RA RA RA")
screen.addstr(6,5,"2) Prooal and alks")
screen.refresh()

n = screen.getch()

if n == ord('1'):
    screen.clear
    screen.refresh()
    screen.border(0)
    screen.addstr(2,2,"Wow you said RA")
elif n == ord('2'):
    screen.clear
    screen.refresh()
    screen.border(0)
    screen.addstr(2,2,"Yes.")

screen.getch()

curses.endwin()
