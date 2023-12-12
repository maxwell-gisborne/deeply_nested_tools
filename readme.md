# For working with deeply nested datastructures in python

## Functions included

to get the value at ``data['path']['to']['data'][2]``
``` python
goget(data, 'path/to/data/2') 
```

to create a new structure with some part modified
``` python
new_data = goset(data, 'path/to/data/value', 'new-value')
```
now ``data`` and ``new_data`` will differ at the value given by the path.

Paths can be the dash seperated strings as shown, or a list or tuple of its parts.
If one part of the path refers to a list, then the value is converted into an ``int`` befor lookup.

There is also a `map` version
``` python
new_data2 = gomap(data, '/games/scores/highscor', lambda x: x+1) 
```

There is also a convinience class to allow
```
Gower(data).set('/fisrt/value', 1).set('/second/value')
```

## example from the test.py:

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
