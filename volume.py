from os import popen

def get_volume() -> tuple[float, bool]:
    a = popen("wpctl get-volume @DEFAULT_SINK@ ").read().strip()
    muted = len(a) == 20
    return float(a[7:11]), muted

def get_str() -> str:
    num, muted = get_volume()
    if muted:
        return "  MUTED!  "
    num = round(10 * num)
    if 0 <= num <= 10:
        return "█" * num + " " * (10 - num)
    elif num > 10:
        return "██████████"
    else:
        return "  ERROR!  "
