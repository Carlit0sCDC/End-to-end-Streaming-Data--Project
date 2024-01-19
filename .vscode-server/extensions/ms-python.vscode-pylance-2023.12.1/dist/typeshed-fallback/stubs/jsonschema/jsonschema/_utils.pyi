from _typeshed import Incomplete, SupportsKeysAndGetItem
from collections.abc import Generator, Iterable, Iterator, Mapping, MutableMapping, Sized

class URIDict(MutableMapping[str, str]):
    def normalize(self, uri: str) -> str: ...
    store: dict[str, str]
    def __init__(self, __m: SupportsKeysAndGetItem[str, str] | Iterable[tuple[str, str]], **kwargs: str) -> None: ...
    def __getitem__(self, uri: str) -> str: ...
    def __setitem__(self, uri: str, value: str) -> None: ...
    def __delitem__(self, uri: str) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...

class Unset: ...

def format_as_index(container: str, indices) -> str: ...
def find_additional_properties(
    instance: Iterable[Incomplete], schema: Mapping[Incomplete, Incomplete]
) -> Generator[Incomplete, None, None]: ...
def extras_msg(extras: Iterable[Incomplete] | Sized) -> str: ...
def ensure_list(thing) -> list[Incomplete]: ...
def equal(one, two) -> bool: ...
def unbool(element, true=..., false=...): ...
def uniq(container) -> bool: ...
def find_evaluated_item_indexes_by_schema(validator, instance, schema) -> list[Incomplete]: ...
def find_evaluated_property_keys_by_schema(validator, instance, schema) -> list[Incomplete]: ...
