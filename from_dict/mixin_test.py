from dataclasses import dataclass, asdict, field
from typing import Dict, List
from .from_dict import FromDictMixin

@dataclass
class B(FromDictMixin):
    value: str

@dataclass
class A(FromDictMixin):
    internal: Dict[str, B] = field(default_factory=dict)

@dataclass
class C(FromDictMixin):
    outer: List[A]


def test_simple():
    b = B(value="hello, world!")
    assert b == B.from_dict(**asdict(b))


b = B(value="hello, world!")

a = A()
a.internal["greeting"] = b

print(asdict(a))
print(asdict(b))

c = A.from_dict(**asdict(a))





