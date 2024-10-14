import pyray
from raylib import colors
from scenes.game import main_game

class Settings:
    WIDTH = 300
    HEIGHT = 300

def main_records():
    pyray.init_window(Settings.WIDTH, Settings.HEIGHT, "Records")
    pyray.set_target_fps(120)  # FPS
    font = pyray.load_font_ex('Arial', 68, None, 0)

    image = pyray.load_image('image/kubki.png')
    texture = pyray.load_texture_from_image(image)
    pyray.unload_image(image)
    f = open('records.txt', 'r')
    max_score = f.readline()
    f.close()

    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.clear_background(colors.BLACK)
        pyray.draw_text('Max score: ', 30, 70, 43, colors.WHITE)
        pyray.draw_rectangle(100, 10, 100, 50, colors.BLACK)
        pyray.draw_texture(texture, 100, 10, colors.WHITE)
        pyray.draw_text(max_score, 135, 135, 43, colors.WHITE)

        if pyray.gui_button(pyray.Rectangle(100,220, 100, 40), 'Play'):
            pyray.close_window()
            main_game()

        pyray.end_drawing()
    pyray.close_window()


if __name__ == '__main__':
    main_records()
