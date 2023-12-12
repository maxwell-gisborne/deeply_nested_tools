# For working with deeply nested datastructures in python

example from the test.py:

```
  80   │ d = {}
  81   │ d = goset(d, 'charicter/details/name', 'tony')
  82   │
  83   │ assert d == {'charicter': {'details': {'name': 'tony'}}}
  84   │
  85   │ d = goset(d, 'charicter/details/age', 28)
  86   │
  87   │ assert d == {'charicter': {'details': {'name': 'tony', 'age': 28}}}
  88   │
  89   │ assert gomap(d, 'charicter/details/age', lambda x: x+1) == {'charicter': {'details': {'name': 'tony', 'age': 29}}}
```
