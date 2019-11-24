# onp.lo package

> Python 3.x package for translating reverse polish notation (AKA postfix notation)
> into infix notation (AKA the normal one)..

## Usage

Our converter function is delivered by `onplo.read` module:

```py
# your_python_file.py
import onplo.read

onplo.read.get('X X p/1 X p/1 ¬ AND EXISTS NOT')
#              ^ string in reverse polish notation
#
# => '(NOT (EXISTS X ((p(X) AND ¬ p(X)))))'
```

### Install

> Make sure you have `python` 3.6+ and `pip` installed

```sh
# check versions
python3 --version   # expected: 3.6+
pip3 --version

## from project's main directory
# we suggest you open virtualenv in the directory
virtualenv venv
source venv/bin/activate

# install dependencies
pip3 install -r requirements.txt
pip3 install -e .
```

### Configuration

In `config.json` you can find

- lists of tokens that are identified by `onplo.type`
  as valid **operators** (including quantifiers), and
- regular expressions which are used to validate tokens as **predicates**, **functions**, **constants** and **variables**

It should look like this:

Following tokens are processed, whilst considered valid.

| token                                       | namespace                      |
| ------------------------------------------- | ------------------------------ |
| **variable**                                | `[A-Z]`                        |
| **constant**                                | `[a-e]`                        |
| **function** (w/ arity)                     | `[f-o]`                        |
| **predicate** (w/ arity)                    | `[p-z]`                        |
| **negacja** (single argument operator)      | `NOT`, `~`, `¬`                |
| **conjunction**                             | `AND`, `&`, `∧`                |
| **disjunction**                             | `OR`, <code>&vert;</code>, `∨` |
| **implication**                             | `IMPLIES`, `→`                 |
| **if, and only if**                         | `IFF`, `↔`                     |
| **exclusive** disjunction                   | `XOR`, `⊕`                     |
| **quantifiers** (universal and existential) | `FORALL`, `∀`, `EXISTS`, `∃`   |

Module `onplo.config` provides acess to the above config data
as python lists and strings (respectively).

`onplo.conf.quantifier` will provide quantifiers,
`onplo.conf.predicate`—predicates,
etc.

### Testing

```sh
# required dependencies
pip3 install -r requirements.txt
pip3 install -e .

# running test suites
pytest
```
