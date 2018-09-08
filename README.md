# from-dict
Convert a nested Python dictionary into a nested Python dataclass

## Usage:

The FromDictMixin should be used as a super/parent for the class you're creating:

```
@dataclass
class MyClass(FromDictMixin):
...
```

When you want to create a Python dictionary (for conversion to JSON or other persistence) use the built-in asdict() function from the dataclasses module. Then pass the dictionary arguments back into the from_dict classmethod.

```
x = MyClass(value1="a"...)
x_as_dict = asdict(x)
y = MyClass.from_dict(**x)
assert x == y
```
