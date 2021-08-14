from _typeshed import Self
from types import ModuleType
from typing import Any

class _TempModule:
    mod_name: str = ...
    module: ModuleType = ...
    def __init__(self, mod_name: str) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args: Any) -> None: ...

class _ModifiedArgv0:
    value: Any = ...
    def __init__(self, value: Any) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args: Any) -> None: ...

def run_module(
    mod_name: str, init_globals: dict[str, Any] | None = ..., run_name: str | None = ..., alter_sys: bool = ...
) -> dict[str, Any]: ...
def run_path(path_name: str, init_globals: dict[str, Any] | None = ..., run_name: str | None = ...) -> dict[str, Any]: ...
