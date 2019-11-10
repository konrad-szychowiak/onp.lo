""" onp.lo - All Rights Reserved. """

import onpl.read as reader


def main():
    """onp.lo
    | Translating postfix to infix notation
    | for first order predicate calculus.

    To end the program type EXIT or press Enter [Return] again after the last line.
    """

    # reading data
    while True:
        postfix = input('$ ').split()

        # user interruption / ending input
        if postfix in [[], ['EXIT'], ['END']]:
            break

        postfix = reader.get(postfix)

        print(f"| {postfix}\n")
        # for i in range(len(postfix)-1, -1, -1): #odczytywanie wyrazow postfixa od konca
        #     pass

    reader.end()


print(main.__doc__)
try:
    main()
except KeyboardInterrupt:
    reader.end(True)
except EOFError:
    reader.end(True)
