from Core.BrowserHelpers import BrowserHelpers
import re


class App(BrowserHelpers):
    def convert_color_to_hex(self, rgb_color):
        try:
            rgb_color = re.search(r'\(.*\)', rgb_color).group(0).replace(' ', '').lstrip('(').rstrip(')')
            [red, green, blue, alpha] = [int(x) for x in rgb_color.split(',')]
            hex_color = '#{:02x}{:02x}{:02x}'.format(red, green, blue)
            return hex_color
        except Exception as err:
            self.test_step_failed(err.__class__.__name__, err, err.__traceback__.tb_frame.f_back.f_lineno)
