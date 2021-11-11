from enum import Enum


class DAO:
    @staticmethod
    def _asdict(obj):
        if isinstance(obj, dict):
            return {key: DAO._asdict(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [DAO._asdict(element) for element in obj]
        elif isinstance(obj, tuple):
            return tuple([DAO._asdict(element) for element in obj])
        elif isinstance(obj, (int, float, str, bool)):
            return obj
        elif isinstance(obj, Enum):
            return obj.value
        elif isinstance(obj, DAO):
            return obj.asdict()
        else:
            raise ValueError('Unsupported type {}.'.format(type(obj)))

    def asdict(self):
        return {key: DAO._asdict(value) for key, value in self.__dict__.items() if value is not None}

    def __repr__(self):
        _repr = '{}('.format(self.__class__.__name__)
        for key, value in self.__dict__.items():
            _repr += '{}={!r}, '.format(key, value)
        _repr = '{})'.format(_repr[:-2])

        return _repr
