import curses

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Retro Text Editor - Green on Black")
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)