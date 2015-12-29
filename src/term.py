#!/usr/bin/env python3
import sys
import curses

class Screen(object):
    
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def getch(self):
        return self.stdscr.getch

    def addstr(self, y, x, phrase):
        stdscr.addstr(y,x,phrase)

