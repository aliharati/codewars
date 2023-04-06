# Write a function, which takes a non-negative integer (seconds) 
# as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.




def make_readable(seconds):
    hours = int(seconds / 3600)
    minutes = int((seconds % 3600) / 60)
    seconds_left = int((seconds % 3600) % 60)
    
    if hours < 10:
        hours = '0' + str(hours)
    if minutes < 10:
        minutes = '0' + str(minutes)
    if seconds_left < 10:
        seconds_left = '0' + str(seconds_left)

    
    return '{}:{}:{}'.format(hours if hours != 0 else '00',
                             minutes if minutes != 0 else '00',
                             seconds_left if seconds_left != 0 else '00')