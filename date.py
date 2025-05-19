import datetime

def get_str() -> str:
    d = datetime.datetime.now()
    return f"{d.day:02}.{d.month:02}.{d.year} | {d.hour:02}:{d.minute:02}:{d.second:02}"

