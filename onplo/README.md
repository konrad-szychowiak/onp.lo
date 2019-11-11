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
