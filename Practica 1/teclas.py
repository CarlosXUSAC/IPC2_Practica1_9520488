import curses

def select_option(options):
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    selected_index = 0

    while True:
        stdscr.clear()

        # Imprimir las opciones
        for i, option in enumerate(options):
            if i == selected_index:
                stdscr.addstr(i, 0, f"> {option}", curses.A_BOLD)
            else:
                stdscr.addstr(i, 0, f"  {option}")

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_DOWN:
            selected_index = min(selected_index + 1, len(options) - 1)
        elif key == curses.KEY_UP:
            selected_index = max(selected_index - 1, 0)
        elif key == 10:  # Tecla Enter
            curses.endwin()
            return options[selected_index]

if __name__ == "__main__":
    options = ["Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5"]

    selected_option = select_option(options)
    print(f"Has seleccionado: {selected_option}")
