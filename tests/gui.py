import curses

screen = curses.initscr()

screen.border(0)
screen.addstr(12,25,"Ayy lmao")
screen.refresh()
screen.getch()

curses.endwin()
