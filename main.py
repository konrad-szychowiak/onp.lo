""" onp.lo - All Rights Reserved. """

import utils.test


def main():
    """
    Application awaints for input…
    To stop reading input please type END or click Enter [Return] again after the last line.
    """

    # reading data
    while True:
        postfix = input('$ ').split()

        # user interruption / ending input
        if postfix in [[], ['END']]:
            break

        postfix = utils.test.init(postfix)

        print(f"| {postfix}\n")
        # for i in range(len(postfix)-1, -1, -1): #odczytywanie wyrazow postfixa od konca
        #     pass

    print("| %s" % (utils.test.END))


print(main.__doc__)
main()
