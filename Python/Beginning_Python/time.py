from datetime import datetime

then = datetime(2018, 9, 1, 23, 13)
now = datetime(2018, 10, 7, 21, 51)

duration = now - then
duration_in_s = duration.total_seconds()

days = divmod(duration_in_s, 86400)
hours = divmod(days[1], 3600)
minutes = divmod(hours[1], 60)
seconds = divmod(minutes[1], 1)
result = "Time between dates: {} days, {} hours, {} minutes and {} seconds"

print(
    result.format(
        int(days[0]), int(hours[0]), int(minutes[0]), int(seconds[0])))
