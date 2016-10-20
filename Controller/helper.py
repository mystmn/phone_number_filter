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


def sub_search(start='', last='', line=''):
    try:
        s = line.index(start) + len(start)
        e = line.index(last, s) - 2
        return line[s:e]

    except ValueError:
        return ""


def whitespace(x, y=()):
    if y is ():
        return x.replace(" ", "")
    else:
        return y.strip()  # remove from left and right position


def search_file():
    pass


def comment_out_line():
    pass
