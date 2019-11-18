# onp.lo package

> Python 3.x package for translating reversed polish notation (AKA postfix notation)
> into infix notation (AKA the normal one)..

## Usage

Our converter function is delivered by `onplo.read` module:

```py
# your_python_file.py
import onplo.read

onplo.read.get('X X p/1 X p/1 ¬ AND EXISTS NOT')
#              ^ string in reversed polish notation
#
# => '(NOT (EXISTS X ((p(X) AND ¬ p(X)))))'
```

## Configuration

In `config.json` you can find

- lists of tokens that are identified by `onplo.type`
  as valid **operators** (including quantifiers), and
- regular expressions which are used to validate tokens as **predicates**, **functions**, **constants** and **variables**

It should look like this:

```js
// config.json
{
  "quantifier":
    /* quantifiers list */,
  "single":
    /* single-argument operators list */,
  "double":
    /* double-argument operators list */,

  "predicate":
    /* predicate-validating regex */,
  "function":
    /* function-validating regex */,
  "constant":
    /* constant-validating regex */,
  "variable":
    /* variable-validating regex */,
}
```

Module `onplo.config` provides acess to the above config data
as python lists and strings (respectively).

`onplo.conf.quantifier` will provide quantifiers,
`onplo.conf.predicate`—predicates,
etc.

## 🚧 Testing

```sh
# Test suites are ready to run using:
$ pytest
```

# API Reference

## `read` module

Module `onplo.read` provides 2 functions for converting postfix to infix notation:

```py
# DEFINITIONS
def get(form: str) -> str:
    """General parser function"""

def analyse(data: list) -> str:
    """Funcion processes and prints tokens from imput with corresponding types."""

# SAMPLE USAGE
onplo.read.get("X p/1")
# => 'p(X)'

onplo.read.analyse(['Y', 'q/1'])
# => 'q(Y)'
```

## `type` module

Module `onplo.type` provides lexing
functions—they check if the given token is of desired category.

```py
# onplo/type.py
# you should expect to see functions of the following pattern:

def token_category_name(token):
    return token in conf.token_category_name
```

## `wrap` module

Module `onplo.type` provides wrapping
functions—they check return formatted string with all
required arguments

```py
# onplo/type.py
# you should expect to see functions of the following pattern:

def token_category_name(*args):
    return f"correctly formatted string for given token_category_name"
```
