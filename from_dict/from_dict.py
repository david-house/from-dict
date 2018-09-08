from dataclasses import fields, dataclass, is_dataclass, Field
from typing import List, _GenericAlias, Type


class FromDictMixin:

    @classmethod
    def container_type(cls, field):
        if isinstance(field.type, _GenericAlias):
            return field.type.__origin__
        else:
            return None

    @classmethod
    def from_dict(cls, **kwargs):
        new_kwargs = dict()
        init_fields = [field for field in fields(cls) if field.init]

        for field in init_fields:
            if field.name in kwargs:

                value = None

                if is_dataclass(field.type):
                    value = field.type.from_dict(**kwargs[field.name])

                elif cls.container_type(field) in [list, tuple, set]:
                    iterable_class = field.type.__args__[0]
                    if is_dataclass(iterable_class):
                        value = cls.container_type(field)([iterable_class.from_dict(**x) for x in kwargs[field.name]])
                    else:
                        value = [x for x in kwargs[field.name]]

                elif cls.container_type(field) is dict:
                    key_type, value_type = field.type.__args__[0], field.type.__args__[1]

                    if key_type is str and is_dataclass(value_type):
                        value = dict()
                        for k, v in kwargs[field.name].items():
                            value[k] = value_type.from_dict(**v)
                else:
                    value = kwargs[field.name]

                new_kwargs[field.name] = value

        return cls(**new_kwargs)
