from itertools import zip_longest
import pprint


class Unreachable(Exception):
    pass


class InvalidPath(Exception):
    pass


def key_in(item, key):
    match item:
        case dict():
            return key in item
        case list() | tuple():
            return int(key) in range(0, len(item))
    raise Unreachable(item, key)


def update(data, name, value):
    match data:
        case dict():
            return data | {name: value}
        case list() | tuple():
            new_data = [item for item in data]
            index = int(name)
            if index < 0:
                index = len(new_data)+index
            new_data[index] = value
            return type(data)(new_data)
    raise Unreachable(data, name, value)


def _get(data, key):
    match data:
        case dict():
            return data.get(key)
        case list() | tuple():
            return data[int(key)]


def validate_path(path):
    if type(path) in {list, tuple}:
        return path
    if type(path) == str:
        return tuple(p for p in path.split('/') if p != '')
    raise InvalidPath(path)


def gowalk(data, path):
    path = validate_path(path)

    if len(path) == 0:
        return data
    for i, p in enumerate(path):
        yield data
        if not key_in(data, p):
            yield None
            return
        else:
            data = _get(data, p)
            if type(data) in {list, tuple, dict}:
                continue
            if not i == len(path)-1:
                raise Exception('Path Terminated Early', path)
    yield data


def goget(data, path):
    result = list(gowalk(data, path))
    if result:
        return result[-1]


def goset(data, path, value):
    path = validate_path(path)
    n_s = list(zip_longest(path, gowalk(data, path)))
    for n, s in reversed(n_s):
        if n is None:
            continue
        if s is None:
            value = {n: value}
        else:
            value = update(s, n, value)
    return value


def gomap(data, path, foo):
    value = goget(data, path)
    if value is None:
        return None
    result = foo(value)
    return goset(data, path, result)


class Gower:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Gower({pprint.pformat(self.data)})'

    def get(self, path):
        result = goget(self.data, path)
        if type(result) in {list, dict, tuple}:
            return Gower(result)
        return result

    def set(self, path, value):
        return Gower(goset(self.data, path, value))

    def map(self, path, foo):
        return Gower(gomap(self.data, path, foo))
