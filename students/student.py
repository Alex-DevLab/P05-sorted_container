from dataclasses import dataclass, field


@dataclass(unsafe_hash=True, order=True)
class Student:
    id: int
    name: str = field(compare=False)
    score: int = field(compare=False)
