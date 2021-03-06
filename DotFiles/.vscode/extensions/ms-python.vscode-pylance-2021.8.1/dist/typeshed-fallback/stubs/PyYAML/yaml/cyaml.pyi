from _typeshed import SupportsRead
from typing import IO, Any, Mapping, Sequence, Text, Union

from yaml.constructor import BaseConstructor, Constructor, SafeConstructor
from yaml.representer import BaseRepresenter, Representer, SafeRepresenter
from yaml.resolver import BaseResolver, Resolver
from yaml.serializer import Serializer

_Readable = SupportsRead[Union[Text, bytes]]

class CParser:
    def __init__(self, stream: str | bytes | _Readable) -> None: ...

class CBaseLoader(CParser, BaseConstructor, BaseResolver):
    def __init__(self, stream: str | bytes | _Readable) -> None: ...

class CLoader(CParser, SafeConstructor, Resolver):
    def __init__(self, stream: str | bytes | _Readable) -> None: ...

class CSafeLoader(CParser, SafeConstructor, Resolver):
    def __init__(self, stream: str | bytes | _Readable) -> None: ...

class CDangerLoader(CParser, Constructor, Resolver): ...  # undocumented

class CEmitter(object):
    def __init__(
        self,
        stream: IO[Any],
        canonical: Any | None = ...,
        indent: int | None = ...,
        width: int | None = ...,
        allow_unicode: Any | None = ...,
        line_break: str | None = ...,
        encoding: Text | None = ...,
        explicit_start: Any | None = ...,
        explicit_end: Any | None = ...,
        version: Sequence[int] | None = ...,
        tags: Mapping[Text, Text] | None = ...,
    ) -> None: ...

class CBaseDumper(CEmitter, BaseRepresenter, BaseResolver):
    def __init__(
        self,
        stream: IO[Any],
        default_style: str | None = ...,
        default_flow_style: bool | None = ...,
        canonical: Any | None = ...,
        indent: int | None = ...,
        width: int | None = ...,
        allow_unicode: Any | None = ...,
        line_break: str | None = ...,
        encoding: Text | None = ...,
        explicit_start: Any | None = ...,
        explicit_end: Any | None = ...,
        version: Sequence[int] | None = ...,
        tags: Mapping[Text, Text] | None = ...,
    ) -> None: ...

class CDumper(CEmitter, SafeRepresenter, Resolver): ...

CSafeDumper = CDumper

class CDangerDumper(CEmitter, Serializer, Representer, Resolver): ...  # undocumented
