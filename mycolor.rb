class Color
    RESET = "\033[0m"
  
    def basic(color_name)
      # Basic colors
      colors = {
        'RED' => "\033[31m",
        'GREEN' => "\033[32m",
        'YELLOW' => "\033[33m",
        'BLUE' => "\033[34m",
        'MAGENTA' => "\033[35m",
        'CYAN' => "\033[36m",
        'WHITE' => "\033[37m"
      }
      # Return the color or raise an error if it's not valid
      colors.fetch(color_name.upcase, raise("Unrecognized color"))
    end
  
    def print(color_code, text, bold: false, underline: false)
      # Apply bold and underline if specified
      style = ""
      style += "\033[1m" if bold  # Bold
      style += "\033[4m" if underline  # Underline
      
      # Print the colored and styled text
      puts "#{style}#{color_code}#{text}#{RESET}"
    end
  
    def color256(text, color_code, bg_code = nil, bold: false, underline: false)
      # Apply styles
      style = ""
      style += "\033[1m" if bold  # Bold
      style += "\033[4m" if underline  # Underline
  
      # Apply the color
      color = "\033[38;5;#{color_code}m"  # Text color
      color += "\033[48;5;#{bg_code}m" if bg_code  # Background color
  
      # Return the styled text
      "#{style}#{color}#{text}#{RESET}"
    end
end