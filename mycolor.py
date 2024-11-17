class Color:
    RESET = "\033[0m"

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
        # Return the color or raise an error if it's not valid
        return colors.get(color_name.upper(), ValueError("Unrecognized color"))
    
    def print(self, color_code, text, bold=False, underline=False):
        # Apply bold and underline if specified
        style = ""
        if bold:
            style += "\033[1m"  # Bold
        if underline:
            style += "\033[4m"  # Underline
        
        # Print the colored and styled text
        return print(f"{style}{color_code}{text}{self.RESET}")

    def color256(self, text, color_code, bg_code=None, bold=False, underline=False):
        # Apply styles
        style = ""
        if bold:
            style += "\033[1m"  # Bold
        if underline:
            style += "\033[4m"  # Underline

        # Apply the color
        color = f"\033[38;5;{color_code}m"  # Text color
        if bg_code is not None:
            color += f"\033[48;5;{bg_code}m"  # Background color

        # Return the styled text
        return f"{style}{color}{text}{self.RESET}"
