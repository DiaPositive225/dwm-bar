from psutil import sensors_battery

def get_str() -> str:
    bat = sensors_battery()
    percent = round(bat.percent / 10)
    return "█" * percent + " " * (10 - percent)
