""" onp.lo - All Rights Reserved. """

from sys import stdin, stderr

import utils.test


def main():
    """
    Application awaints for input…
    To stop reading input please type END or click Enter [Return] again after the last line.
    """

    # reading data
    for postfix in stdin:
        postfix = postfix.strip().split()

        # user interruption / ending input
        if postfix in [[], ['END']]:
            break

        postfix = utils.test.init(postfix)

        print(f"|> {postfix}\n", file=stderr)
        # for i in range(len(postfix)-1, -1, -1): #odczytywanie wyrazow postfixa od konca
        #     pass


print(main.__doc__)
main()
