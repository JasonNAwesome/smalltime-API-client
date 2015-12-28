#!/usr/bin/env python3
import curses

screen = curses.initscr()

screen.clear
screen.border(0)
screen.addstr(3,3,"Choose a choice:")
screen.addstr(5,5,"A) RA RA RA")
screen.addstr(6,5,"B) Prooal and alks")
screen.refresh()

n = screen.getch()

curses.endwin()
