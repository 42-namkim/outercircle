'''
Your lib imports must be explicit,
for example you must "import numpy as np".
Importing "from pandas import *" is not allowed,
and you will get 0 on the exercise.

1. import 모듈  // 모듈.함수 로 모듈 내 함수에 접근 가능
2. import 모듈 as 이름
3. from 모듈 import 함수명  // 함수 호출 시 모듈 이름 없이 곧바로 모듈 안 함수 호출 가능
4. from 모듈 import *
'''

'''
Date and time objects may be categorized as “aware” or “naive” depending on whether or not they include timezone information.

With sufficient knowledge of applicable algorithmic and political time adjustments, such as time zone and daylight saving time information, an aware object can locate itself relative to other aware objects. An aware object represents a specific moment in time that is not open to interpretation. 1

A naive object does not contain enough information to unambiguously locate itself relative to other date/time objects. Whether a naive object represents Coordinated Universal Time (UTC), local time, or time in some other timezone is purely up to the program, just like it is up to the program whether a particular number represents metres, miles, or mass. Naive objects are easy to understand and to work with, at the cost of ignoring some aspects of reality.
'''

#Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
#Oct 21 2022$

import datetime

datetime = datetime.datetime
ft_now = datetime.now()
ft_posix = datetime.fromtimestamp(0, tz=None)
ft_curr_timestamp = ft_now.timestamp()


#format %e?
#lstrip
# ValueError: cannot switch from automatic field numbering to manual field specification
# 0.day <- get value
print("Seconds since " \
        + '{0:%B} {0.day} {0:%Y: }'.format(ft_posix) \
        # + '{0:%B} {1} {0:%Y:}'.format(ft_posix, ft_posix.day) \
        + '{0:,.4f}'.format(ft_curr_timestamp)
        + " or " \
        + format(ft_curr_timestamp, ".2E") \
        + " in scientific notation")
print(format(ft_now, "%b %d %Y"))