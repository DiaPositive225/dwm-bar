# from os import popen
import subprocess
from Xlib import Xatom
import pulsectl

def get_volume() -> tuple[float, bool]:
    a = subprocess.Popen("/sbin/wpctl get-volume @DEFAULT_SINK@ ", shell=True, stdout=subprocess.PIPE, text=True)
    a.wait()
    a = a.stdout.readline().strip()
    muted = len(a) == 20
    return float(a[7:11]), muted
# def get_volume() -> tuple[float, bool]:
#     try: 
#         pulse = pulsectl.Pulse()
#         sink = pulse.sink_default_get()
#         v = sink.volume.values
#         res = ((v[0]+v[1])/2, sink.mute == 1)
#         return res
#     except pulsectl.PulseError:
#         return (0,False)
#
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
