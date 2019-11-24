# onp.lo contributor guide

## Why so complicated?

When you look up the `onplo/` directory you will find the package's source code…
in many different files. Why is that?

We have taken two main goals (aside making the code work):

1.  The source code must be **easy to edit**

    Whilst using version control, multiple contributors edit multiple lines
    of code. We love the possibility of changing small,
    interchangeable files without any threat of unintended conflicts.

2.  The application must be extremely **easy to expand**

    Either when expectations change, or we need to add more functionality
    to `onplo` we can easily find and expand e.g. set of operators—it's
    just one line in config file.

We believe that small files are better
for getting your head around the project.
One issue, though, is that you need to find what is where
for it work as intended. This is why we present the following
guide on `onplo`'s modules.

## Understanding modules

> **note:** there is a separate README in `onplo/`
> where we cover instalation, usage, configuration
> and testing of the package for you.

1.  **`onplo/config.json`**

    In this file, you will find JSON object with sets of valid
    _quantifiers_ and
    operators (_single_-argument and _double_-argument).

1.  **`onplo/conf.py`** (as `onplo.conf`)

    This module reads configuration form `config.json`
    (using absolute path to the file—it's required by python to work)
    and exports it as python lists.

1.  **`onplo/type.py`** (as `onplo.type`)

    Here are functions which check if given tokens (as strings)
    match respective categories.

    For some `onplo.conf` lists are used, and for some—regular expressions.
    We implemented those simple regexes to make the matching functions
    easier to understand in a compact way.

1.  **`onplo/wrap.py`** (as `onplo.wrap`)

    Before we see the main converting function
    we could have a look at the wrapper functions.

    Those functions take exact number of required arguments
    for respective categories and return formatted strings.
    Nothing fancy, but clean and reusable.

1.  **`onplo/read.py`** (as `onplo.read`)

    This is where the real things happen. You will find here
    2 functions: one for `list`s, and the other for `str`ings.

    `analyse` runs itself as long as there is whole formula generated
    (or error raised).
