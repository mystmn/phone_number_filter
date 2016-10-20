from __future__ import print_function  # allows end=''
from pathlib import Path
from Controller import helper as coh
import fileinput


class FeedList(object):

    @staticmethod
    def start(x):
        if not Path(x).is_file():
            return False
        #  Back up the original file
        return fileinput.FileInput(x, inplace=True, backup='.bak')

    @staticmethod
    def read_file(start_div, end_div, sub_one, sub_two, line):
        list_numbers = [
            '+16146666666',
            '+16147777777',
        ]

        #  Find the starting position number of our html
        #  example: <sms or <div
        first_pos = line.find(start_div)

        #  Find the closing position number
        #  example: </> or </div>
        sec_pos = line.find(end_div)

        #  Confirm our character exist in this line
        if start_div in line:

            #  Isolated the range to a broad positioning
            range_in_line = line[first_pos:sec_pos]

            #  Narrow down the range within the broad
            #  example: <broad>
            #               <narrow></narrow>
            #           </broad>
            sub_range = coh.sub_search(sub_one, sub_two, range_in_line)

            #  Find phone number and change to a universal format
            #  example: 614-614-2699 & 16146142699 to +16146142699
            format_number = coh.scrubbed(sub_range)

            #  Replace the cleaned phone number in our broad range line
            fresh_clean = range_in_line.replace(sub_range, format_number)

            # XML files hate str(--)
            fc = fresh_clean.replace('--', '')

            #  Does the number match our white list?
            if format_number in list_numbers or not format_number:

                #  Phone number confirmed, return line
                return "{}{}".format("\n", fc)

            else:
                #  This line has a black listed number, comment out <!-- HTML -->
                return "{}<!-- {} -->{}".format("\n", fc, "\n")

        # This line doesn't have the ranged html that we're search for
        return line
