from deeply_nested_tools import goget, goset, gomap

deeply_nested_data = {
    'level1': {
        'level2': {
            'level3': {
                'level4': {
                    'level5': {
                        'level6': {
                            'level7': {
                                'level8': {
                                    'level9': {
                                        'level10': {
                                            'name': 'John Doe',
                                            'age': 30,
                                            'details': {
                                                'address': {
                                                    'city': 'Anytown',
                                                    'zipcode': '12345',
                                                    'coordinates': (12.345, -45.678)
                                                },
                                                'contact': {
                                                    'email': 'john.doe@example.com',
                                                    'phone_numbers': ['123-456-7890', '987-654-3210']
                                                },
                                                'attributes': {
                                                    'height': 175.5,
                                                    'weight': 70.2,
                                                    'hobbies': {
                                                        'sports': {
                                                            'indoor': {
                                                                'table_tennis': ['racket', 'ball']
                                                            }
                                                        }
                                                    }
                                                }
                                            },
                                            'grades': {
                                                'math': {'midterm': 85, 'final': 92},
                                                'science': {'midterm': 78, 'final': 88}
                                            },
                                            'friends': [
                                                {'name': 'Alice', 'age': 28},
                                                {'name': 'Bob', 'age': 32, 'interests': {'movies': ['action', 'comedy'], 'music': {'rock': 'classic'}}}
                                            ],
                                            'pets': {
                                                'dogs': {'breed': 'Labrador', 'names': {'male': 'Buddy', 'female': 'Daisy'}},
                                                'cats': {'breed': 'Siamese', 'names': {'male': 'Whiskers', 'female': 'Mittens'}}
                                            },
                                            'favorite_numbers': {1, 7, 42, 3.14},
                                            'notes': """
                                                This is a multiline string providing additional notes.
                                                It can include line breaks and special characters.
                                            """
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

interesting_address='level1/level2/level3/level4/level5/level6/level7/level8/level9/level10'
contents = goget(deeply_nested_data,interesting_address)

assert goget(contents,'details/address/zipcode') == '12345'

assert goget(contents, 'pets/cats/names') == {'male': 'Whiskers', 'female': 'Mittens'}

assert goget(contents, 'pets/cats/names/afd') == None

assert goset(contents, 'family/dad/name','Tony')['family'] == {'dad': {'name': 'Tony'}}

assert goget(contents, 'family') == None

d = {}
d = goset(d, 'charicter/details/name', 'tony')

assert d == {'charicter': {'details': {'name': 'tony'}}}

d = goset(d, 'charicter/details/age', 28)

assert d == {'charicter': {'details': {'name': 'tony', 'age': 28}}}

assert gomap(d, 'charicter/details/age', lambda x: x+1) == {'charicter': {'details': {'name': 'tony', 'age': 29}}}

