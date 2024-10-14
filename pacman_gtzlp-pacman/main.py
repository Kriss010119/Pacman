from scenes.game import main_game
from records import main_records
import pyray
from raylib import colors


class Settings:
    WIDTH = 900
    HEIGHT = 900


def main():
    pyray.init_window(Settings.WIDTH, Settings.HEIGHT, "GTZLP_PACKMAN")
    pyray.set_target_fps(120)  # FPS
    font = pyray.load_font_ex('Arial', 68, None, 0)

    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.clear_background(colors.BLACK)

        if pyray.gui_button(pyray.Rectangle(Settings.WIDTH//2.3, Settings.HEIGHT//4, 100, 50), 'Play'):
            main_game()
        if pyray.gui_button(pyray.Rectangle(Settings.WIDTH//2.3, Settings.HEIGHT//4*1.5, 100, 50), 'Records'):
            main_records()
        if pyray.gui_button(pyray.Rectangle(Settings.WIDTH//2.3, Settings.HEIGHT//4*2, 100, 50), 'Exit'):
            pyray.end_drawing()
            pyray.close_window()

        pyray.end_drawing()
    pyray.close_window()



if __name__ == '__main__':
    main()
