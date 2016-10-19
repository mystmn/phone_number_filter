from __future__ import print_function
from Controller.main import FeedList

#  What file are we looking at?
f = 'Need File Path'

each_line = FeedList().start(f)

for each in each_line:
    print(FeedList().read_file('<sms', '/\"', 'address=\"', 'date', each), end='')
