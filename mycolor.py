RESET = "\033[0m"

class Color:
    def basic(self, color_name):
        # Basic colors
        colors = {
            'RED': "\033[31m",
            'GREEN': "\033[32m",
            'YELLOW': "\033[33m",
            'BLUE': "\033[34m",
            'MAGENTA': "\033[35m",
            'CYAN': "\033[36m",
            'WHITE': "\033[37m"
        }
        # Retorn a the color or lauch a mistake if it's not valid
        return colors.get(color_name.upper(), ValueError("Unrecognized color"))
    
    def print(self, color_code, text):
        return print(f"{color_code}{text}{RESET}")

    def color256(self, text, color_code, bg_code=None):
        color = f"\033[38;5;{color_code}m"  # Color text
        if bg_code is not None:
            color += f"\033[48;5;{bg_code}m"  # Color background
        return f"{color}{text}{RESET}"
    