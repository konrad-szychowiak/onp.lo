import onplo.read as reader


def main():
    """onp.lo
    | Translating postfix to infix notation
    | for first order predicate calculus.

    To end the program type EXIT or press Enter [Return] again after the last line.
    """

    # reading data
    while True:

        try:
            postfix = input('$ ')

            # user interruption / ending input
            if postfix in ['', 'EXIT', 'END']:
                break

            postfix = reader.get(postfix)
            print(f"| {postfix}\n")

        except (KeyboardInterrupt, EOFError):
            print("\n", end="")
            break

        except (IndexError, ValueError) as Error:
            print(f"| \033[1;31mERROR\033[0m\t{Error}\n")

    print("| \033[1;30mEXIT\033[0m")


if __name__ == '__main__':
    print(main.__doc__)
    main()
