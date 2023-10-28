def format_duration(seconds):
    patterns = {5: "{}, {}, {}, {} and {}",
                4: "{}, {}, {} and {}",
                3: "{}, {} and {}",
                2: "{} and {}",
                1: "{}",
                0: "now"}

    def format(n: int, time: str):
        if n:
            if n == 1:
                return f"{n} {time}"
            return f"{n} {time}s"
        return ""

    years = format(seconds // 31_536_000, "year")
    days = format(seconds % 31_536_000 // 86_400, "day")
    hours = format(seconds % 86_400 // 3600, "hour")
    minutes = format(seconds % 3600 // 60, "minite")
    seconds = format(seconds % 60, "second")

    not_zero = tuple(filter(lambda x: x != '', (years, days, hours, minutes, seconds)))

    return patterns[len(not_zero)].format(*not_zero)