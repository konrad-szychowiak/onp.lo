# onp.lo package

> Python 3.x package for translating reversed polish notation (AKA postfix notation)
> into infix notation (AKA the normal one)..

## 🚧 Testing

We have one test suite ready to run from the main project directory:

```sh
$ python3 main.test.py
# Unit tests for provided input/output examples.
```

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
