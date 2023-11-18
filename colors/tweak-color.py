"""
tweak-color.py

This script provides functionality to adjust the hue, saturation, and brightness of a given hex color code.
It allows the user to input a hex color and then choose to modify its hue, saturation, or brightness by specified amounts.
The script uses the HSV color model for these adjustments and then converts the result back to a hex color code.
"""

import colorsys

def adjust_hsv(hex_color, hue_shift=0, saturation_change=0, brightness_change=0):
    """
    Adjusts the hue, saturation, and brightness of a hex color.
    """
    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    hsv_color = colorsys.rgb_to_hsv(rgb_color[0]/255, rgb_color[1]/255, rgb_color[2]/255)

    new_hue = (hsv_color[0] + hue_shift / 360) % 1
    new_saturation = max(0, min(1, hsv_color[1] + saturation_change / 100))
    new_brightness = max(0, min(1, hsv_color[2] + brightness_change / 100))

    new_rgb = colorsys.hsv_to_rgb(new_hue, new_saturation, new_brightness)
    return "{:02x}{:02x}{:02x}".format(int(new_rgb[0]*255), int(new_rgb[1]*255), int(new_rgb[2]*255))

def get_mode_input():
    """
    Handles the input for selecting the mode of adjustment.
    """
    modes = {'h': 'hue', 's': 'saturation', 'b': 'brightness', 'r': 'reset', 'e': 'exit'}
    while True:
        mode = input("Enter mode: hue (h), saturation (s), brightness (b), reset (r), or exit (e): ").lower()
        if mode in modes:
            return mode
        print("Invalid mode. Please enter a valid mode.")

def get_adjustment_input(mode):
    """
    Handles the input for the adjustment value based on the mode.
    """
    prompt = {
        'h': "Enter hue shift value (degrees, 0-360): ",
        's': "Enter saturation change percentage (-100 to 100): ",
        'b': "Enter brightness change percentage (-100 to 100): "
    }
    while True:
        try:
            adjustment = float(input(prompt[mode]))
            if (mode == 'h' and 0 <= adjustment <= 360) or (mode in ['s', 'b'] and -100 <= adjustment <= 100):
                return adjustment
            print("Invalid value. Please enter a number in the valid range.")
        except ValueError:
            print("Invalid value. Please enter a valid number.")

def main():
    while True:
        mode = get_mode_input()
        if mode == 'r': continue
        if mode == 'e': break

        adjustment = get_adjustment_input(mode) if mode != 'r' else 0

        while True:
            hex_color = input("Enter a hex color code (or 'e' to exit, 'r' to reset): ").strip().lstrip('#')
            if hex_color.lower() in ['e', 'r']: 
                if hex_color.lower() == 'e': return
                break

            try:
                adjustments = {'h': {'hue_shift': adjustment}, 's': {'saturation_change': adjustment}, 'b': {'brightness_change': adjustment}}
                new_hex_color = adjust_hsv(hex_color, **adjustments.get(mode, {}))
                print("New Hex Color Code: " + new_hex_color.upper())
            except ValueError:
                print("Invalid hex color code. Please enter a valid hex color code.")

if __name__ == "__main__":
    main()
