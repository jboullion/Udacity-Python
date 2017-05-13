import webbrowser
import time

max_breaks = 2
breaks = 0
break_min = 10
url = 'https://www.youtube.com/watch?v=pDmnV6PWv5Y'
debug_string = "Break {} started on: {}"

while breaks < max_breaks:
    time.sleep(break_time * 60)
    breaks += 1

    print(debug_string.format(breaks, time.ctime()))
    webbrowser.open(url)
