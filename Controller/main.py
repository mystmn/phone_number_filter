from __future__ import print_function  # allows end=''
import os, fileinput


class FeedList(object):

    @staticmethod
    def start(x):
        #  Back up the original file
        return fileinput.FileInput(x, inplace=True, backup='.bak')

    def read_file(self, start_div, end_div, sub_one, sub_two, line):
        list_numbers = [
            '+19999999999',  # Mom
            '+17777777777',
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
            sub_range = self.sub_search(sub_one, sub_two, range_in_line)

            #  Find phone number and change to a universal format
            #  example: 614-614-2699 & 16146142699 to +16146142699
            format_number = self.scrubbed(sub_range)

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
        else:
            return line

    @staticmethod
    def scrubbed(var, sym="+"):
        #  address="614-216-2423" address="+1 614-273-4873"

        nn = list(var.replace('-', "").replace(' ', ''))

        if len(nn) != 0:
            if nn[0] is not sym:
                nn.insert(0, sym)

            if nn[1] is not "1":
                nn.insert(1, "1")

            return ''.join(nn)

        return var

    @staticmethod
    def sub_search(start='', last='', line=''):

        try:
            s = line.index(start) + len(start)
            e = line.index(last, s) - 2
            return line[s:e]

        except ValueError:
            return ""

    @staticmethod
    def whitespace(x, y=()):
        if y is ():
            return x.replace(" ", "")
        else:
            return y.strip()  # remove from left and right position

    @staticmethod
    def reset():
        os.system('clear')

    def search_file(self, path=''):
        pass

    def comment_out_line(self):
        pass
