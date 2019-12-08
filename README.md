# onp.lo

[![Build Status][travis]](https://travis-ci.com/konrad-szychowiak/onp.lo)
[![Netlify Status][netlify]](https://app.netlify.com/sites/suspicious-davinci-935db7/deploys)

> Python package and showcase application for converting
> reverse polish notation into standard infix notation.
>
> onp.lo stands for _Odwrotna Notacja Polska, Logika Obliczeniowa_
> (polish for: _Reverse Polish Notation, Logical Calculus_)

## Instalation

You can install `onplo` as a python package, if you wish.
It is not required for a showcase application to work, though.
(But you will need it to run tests. Consult [this file][readme] beforehand.)

```sh
## Assuming you use unix/linux to get, test and run onplo
# check versions and install dependencies if you need to
python3 --version   # expected: 3.6+
pip3 --version

## from project's main directory
# we suggest opening virtualenv in the directory
virtualenv venv
source venv/bin/activate

# install dependencies
pip3 install -r requirements.txt

# install the package in editable mode
pip3 install -e .
```

> **note:** `setup.py` is used only for generating and instaling `onplo`
> python package and is not an element of the presented solution itself

## Usage

**onp.lo** provides conversion of input (strings or arrays/lists)
from postfix to infix notation
using recursive algorithm provided by `onplo`'s api.

### Showcase application

```sh
# run showcase app
python3 main.py
```

- Showcase app expects infinite number of lines—after <code>\$&nbsp;</code>.
- Processed output (infix notation) will be given after <code>|&nbsp;</code>
  in new line.
- Inputs can be finished using `END`, `EXIT`, `ctrl+D` or `ctrl+C` in the input, or leaving a blank line.
  - Application will inform about exiting with `| EXIT` line.
  - If during execution any errors occurred (ex. invalid tokens) `| ERROR` will be printed.

### Input/Output Examples

```
$ a p/1
| p(a)

$ Z p/1 EXISTS
| (EXISTS Z p(Z))

$ X X a f/2 p/1 ∃ Y Y Z f/1 p/2 FORALL → FORALL
| (FORALL Z ((∃ X p(f(X, a))) → (FORALL Y p(Y, f(Z)))))

$ Y X X b c q/3 Z Y f/1 p/2 ~ & EXISTS FORALL EXISTS
| (EXISTS Z (FORALL Y (EXISTS X (q(X, b, c) & (~ p(Z, f(Y)))))))

$ invalid_token EXISTS
| ERROR       Forbidden token found whilst analysing given formula :
              'invalid_token' in position 0

$ EXIT
| EXIT
```

> For those provided examples we have prepared tests.
> Please refer to `onplo` package's inner [README]
> and python [test files](./tests/api_test.py).

### Under-the-hood

If you need docs over usage of code we've written,
head straight to `onplo` package [README]
and [CONTRIBUTING] guide (soon)—you will find in-depth explenations
about features and modules of `onplo`.

You can also visit [website] w/ docs published via Netlify.

## Changes

See [CHANGELOG] for full list of changes and updates.

## Authors

See [AUTHORS] for full list of contributors.

## License

This software is distributed under **Mozilla Public License 2.0**.
See [LICENSE] for full license text.

<!-- links -->

[travis]: https://travis-ci.com/konrad-szychowiak/onp.lo.svg?token=t4TxLZpjW4GqaJpJnsTe&branch=develop
[netlify]: https://img.shields.io/netlify/7155677d-8a01-4613-ba7a-b42ad987710a?label=docs&logo=netlify&logoColor=white
[website]: https://suspicious-davinci-935db7.netlify.com/
[authors]: ./AUTHORS.md
[readme]: ./onplo/README.md
[license]: ./LICENSE
[changelog]: ./CHANGELOG.md
[contributing]: ./CONTRIBUTING.md
