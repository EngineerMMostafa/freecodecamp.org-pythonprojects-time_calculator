def add_time(start, duration, startingday = ''):

    week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    strt_hour = int(start[:start.find(':')])
        
    if 'AM' in start:
        strt_mm = 0
    else :
        strt_mm = 1

    strt_hour = strt_hour + (strt_mm * 12)
    strt_minute = int(start[start.find(':')+1:start.find(' ')])

    strt_day = 0
    if startingday:
        startingday = startingday.lower().capitalize()
        if startingday in week:
            strt_day = week.index(startingday)

    dur_hours = int(duration[:duration.find(':')])
    dur_minutes = int(duration[duration.find(':')+1 :])
    dur_days = 0

    if(dur_hours >= 24):
        dur_days = dur_hours // 24
        dur_hours = dur_hours % 24

    res_hour = strt_hour + dur_hours
    res_minute = strt_minute + dur_minutes

    if res_minute >= 60:
        res_hour += 1
        res_minute = res_minute - 60
    
    res_day = strt_day + dur_days
    
    if res_hour >= 24:
        res_day += 1
        res_hour = res_hour - 24

    if res_hour == 12:
        res_mm = ' PM'
    elif res_hour > 12:
        res_mm = ' PM'
        res_hour = res_hour - 12
    elif res_hour == 0:
        res_hour = 12
        res_mm = ' AM' 
    else:
        res_mm = ' AM'

    new_time = str(res_hour) + ':' + str(res_minute).rjust(2, '0') + res_mm

    if startingday:
        day = res_day
        if day > 6: day = day % 7
        new_time = new_time + ', ' + week[day]

    if strt_day != res_day:
        if res_day - strt_day == 1:
            new_time = new_time + ' (next day)'
        else:
            new_time = new_time + ' (%s days later)'%(res_day - strt_day)

    return new_time