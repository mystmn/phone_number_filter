from __future__ import print_function
from Controller.main import FeedList

#  What file are we looking at?
f = ''

each_line = FeedList().start(f)

if not each_line:
    print("The requested file {} doesn't exist".format(f))

for each in each_line:
    print(FeedList().read_file('<sms', '/\"', 'address=\"', 'date', each), end='')
