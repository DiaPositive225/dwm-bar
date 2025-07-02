from psutil import sensors_battery

reset = "\x1b[0m"
inverse = "\x1b[7m"

def get_str() -> str:
    bat = sensors_battery()
    percent = round(bat.percent / 10)
    return "█" * percent + " " * (10 - percent)
    # return inverse + " " * percent + reset + " " * (10 - percent)
