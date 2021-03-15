def add_time(start, duration, startingday = ''):
  # Function to calculate and add duration to start time
  # accepts start time, and duration as required parameters
  # accepts optional parameter starting day



    # create a list of week days capitalized
    week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    # Extract hours from start time
    strt_hour = int(start[:start.find(':')])
    # define a variable indicate AM or PM to convert 12 hours clock format to 24 hours format
    if 'AM' in start:
        strt_mm = 0
    else :
        strt_mm = 1
    strt_hour = strt_hour + (strt_mm * 12)

    # Extract minutes from start time
    strt_minute = int(start[start.find(':')+1:start.find(' ')])

    # Initialize starting day
    strt_day = 0
    if startingday:       # if starting day in input
        startingday = startingday.lower().capitalize()
        if startingday in week:
            strt_day = week.index(startingday)

    # Extract hours from duration
    dur_hours = int(duration[:duration.find(':')])
    # Extract minutes from duration
    dur_minutes = int(duration[duration.find(':')+1 :])
    # Initialize duration days and calculate it
    dur_days = 0
    if(dur_hours >= 24):
        dur_days = dur_hours // 24
        dur_hours = dur_hours % 24
    

    # Compute resultant time
    # calculate resultant hours
    res_hour = strt_hour + dur_hours
    # calculate resultant minutes
    res_minute = strt_minute + dur_minutes

    # Approximate result minutes if higher than 60 and update resultant hours
    if res_minute >= 60:
        res_hour += 1
        res_minute = res_minute - 60
    # calculate resultant days
    res_day = strt_day + dur_days

    # Approximate result hours if higher than 24 and update result days
    if res_hour >= 24:
        res_day += 1
        res_hour = res_hour - 24

    # Indicate result time is AM or PM then update result hours in 12 hours format
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

    # Concatenate new_time in required format
    new_time = str(res_hour) + ':' + str(res_minute).rjust(2, '0') + res_mm

    # Add result Day if starting day in input.
    if startingday:
        day = res_day
        if day > 6: day = day % 7
        new_time = new_time + ', ' + week[day]

    # Concatenate number of days to new_time
    if strt_day != res_day:
        if res_day - strt_day == 1:
            new_time = new_time + ' (next day)'
        else:
            new_time = new_time + ' (%s days later)'%(res_day - strt_day)

    return new_time
