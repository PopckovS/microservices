from dataclasses import dataclass, asdict
from typing import List, Optional
from enum import Enum, auto
import json


@dataclass
class RequestMixin:
    @classmethod
    def from_request(cls, request):
        values = request.get("input")
        return cls(**values)

    def to_json(self):
        return json.dumps(asdict(self))


@dataclass
class InsertMainNewsOneDerivedOutput(RequestMixin):
    id: int


@dataclass
class InsertNewsOneOutput(RequestMixin):
    id: int


@dataclass
class Mutation(RequestMixin):
    InsertNewsOne: Optional[InsertNewsOneOutput]


@dataclass
class InsertNewsOneArgs(RequestMixin):
    cat: int
    content: str
    title: str
