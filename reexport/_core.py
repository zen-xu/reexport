from __future__ import annotations

import sys

from typing import Any
from typing import Callable
from typing import TypeVar
from typing import overload


if sys.version_info < (3, 10):
    from typing_extensions import Concatenate
    from typing_extensions import Literal
    from typing_extensions import ParamSpec
else:
    from typing import Concatenate
    from typing import Literal
    from typing import ParamSpec


_FP = ParamSpec("_FP")  # From parameters
_FR = TypeVar("_FR")  # From return
_TR = TypeVar("_TR")  # To return
_As = TypeVar("_As")

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")
_T6 = TypeVar("_T6")
_T7 = TypeVar("_T7")
_T8 = TypeVar("_T8")
_T9 = TypeVar("_T9")


@overload
def clone_params_from(
    __clone_func: Callable[_FP, _FR],
) -> Callable[[Callable[..., Any]], Callable[_FP, _FR]]: ...


@overload
def clone_params_from(
    __clone_func: Callable[_FP, _FR], *, keep_return: Literal[True]
) -> Callable[[Callable[..., Any]], Callable[_FP, _FR]]: ...


@overload
def clone_params_from(
    __clone_func: Callable[_FP, _FR], *, keep_return: Literal[False]
) -> Callable[[Callable[..., _TR]], Callable[_FP, _TR]]: ...


def clone_params_from(__clone_func: Callable, *, keep_return: bool = True) -> Callable:
    def decorator(func):
        return func

    return decorator


@overload
def concatenate(
    *, add: tuple[type[_T1]]
) -> Callable[
    [Callable[_FP, _FR]],
    Callable[
        Concatenate[_T1, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    *, add: tuple[type[_T1], type[_T2]]
) -> Callable[
    [Callable[_FP, _FR]],
    Callable[
        Concatenate[_T1, _T2, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    *, add: tuple[type[_T1], type[_T2], type[_T3]]
) -> Callable[
    [Callable[_FP, _FR]],
    Callable[
        Concatenate[_T1, _T2, _T3, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    *, add: tuple[type[_T1], type[_T2], type[_T3], type[_T4]]
) -> Callable[
    [Callable[_FP, _FR]],
    Callable[
        Concatenate[_T1, _T2, _T3, _T4, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    *, add: tuple[type[_T1], type[_T2], type[_T3], type[_T4], type[_T5]]
) -> Callable[
    [Callable[_FP, _FR]],
    Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    *, add: tuple[type[_T1], type[_T2], type[_T3], type[_T4], type[_T5], type[_T6]]
) -> Callable[
    [Callable[_FP, _FR]],
    Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    *,
    add: tuple[
        type[_T1], type[_T2], type[_T3], type[_T4], type[_T5], type[_T6], type[_T7]
    ],
) -> Callable[
    [Callable[_FP, _FR]],
    Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    *,
    add: tuple[
        type[_T1],
        type[_T2],
        type[_T3],
        type[_T4],
        type[_T5],
        type[_T6],
        type[_T7],
        type[_T8],
    ],
) -> Callable[
    [Callable[_FP, _FR]],
    Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    *,
    add: tuple[
        type[_T1],
        type[_T2],
        type[_T3],
        type[_T4],
        type[_T5],
        type[_T6],
        type[_T7],
        type[_T8],
        type[_T9],
    ],
) -> Callable[
    [Callable[_FP, _FR]],
    Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    *,
    add: tuple[type[_T1]],
) -> Callable[
    Concatenate[_T1, _FP],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    *,
    add: tuple[type[_T1], type[_T2]],
) -> Callable[
    Concatenate[_T1, _T2, _FP],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    *,
    add: tuple[type[_T1], type[_T2], type[_T3]],
) -> Callable[
    Concatenate[_T1, _T2, _T3, _FP],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    *,
    add: tuple[type[_T1], type[_T2], type[_T3], type[_T4]],
) -> Callable[
    Concatenate[_T1, _T2, _T3, _T4, _FP],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    *,
    add: tuple[type[_T1], type[_T2], type[_T3], type[_T4], type[_T5]],
) -> Callable[
    Concatenate[_T1, _T2, _T3, _T4, _T5, _FP],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    *,
    add: tuple[type[_T1], type[_T2], type[_T3], type[_T4], type[_T5], type[_T6]],
) -> Callable[
    Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _FP],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    *,
    add: tuple[
        type[_T1], type[_T2], type[_T3], type[_T4], type[_T5], type[_T6], type[_T7]
    ],
) -> Callable[
    Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _FP],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    *,
    add: tuple[
        type[_T1],
        type[_T2],
        type[_T3],
        type[_T4],
        type[_T5],
        type[_T6],
        type[_T7],
        type[_T8],
    ],
) -> Callable[
    Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _FP],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    *,
    add: tuple[
        type[_T1],
        type[_T2],
        type[_T3],
        type[_T4],
        type[_T5],
        type[_T6],
        type[_T7],
        type[_T8],
        type[_T9],
    ],
) -> Callable[
    Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _FP],
    _FR,
]: ...


@overload
def concatenate(
    *,
    remove: Literal[1],
) -> Callable[
    [
        Callable[
            Concatenate[Any, _FP],
            _FR,
        ]
    ],
    Callable[_FP, _FR],
]: ...


@overload
def concatenate(
    *,
    remove: Literal[2],
) -> Callable[
    [
        Callable[
            Concatenate[Any, Any, _FP],
            _FR,
        ]
    ],
    Callable[_FP, _FR],
]: ...


@overload
def concatenate(
    *,
    remove: Literal[3],
) -> Callable[
    [
        Callable[
            Concatenate[Any, Any, Any, _FP],
            _FR,
        ]
    ],
    Callable[_FP, _FR],
]: ...


@overload
def concatenate(
    *,
    remove: Literal[4],
) -> Callable[
    [
        Callable[
            Concatenate[Any, Any, Any, Any, _FP],
            _FR,
        ]
    ],
    Callable[_FP, _FR],
]: ...


@overload
def concatenate(
    *,
    remove: Literal[5],
) -> Callable[
    [
        Callable[
            Concatenate[Any, Any, Any, Any, Any, _FP],
            _FR,
        ]
    ],
    Callable[_FP, _FR],
]: ...


@overload
def concatenate(
    *,
    remove: Literal[6],
) -> Callable[
    [
        Callable[
            Concatenate[Any, Any, Any, Any, Any, Any, _FP],
            _FR,
        ]
    ],
    Callable[_FP, _FR],
]: ...


@overload
def concatenate(
    *,
    remove: Literal[7],
) -> Callable[
    [
        Callable[
            Concatenate[Any, Any, Any, Any, Any, Any, Any, _FP],
            _FR,
        ]
    ],
    Callable[_FP, _FR],
]: ...


@overload
def concatenate(
    *,
    remove: Literal[8],
) -> Callable[
    [
        Callable[
            Concatenate[Any, Any, Any, Any, Any, Any, Any, Any, _FP],
            _FR,
        ]
    ],
    Callable[_FP, _FR],
]: ...


@overload
def concatenate(
    *,
    remove: Literal[9],
) -> Callable[
    [
        Callable[
            Concatenate[Any, Any, Any, Any, Any, Any, Any, Any, Any, _FP],
            _FR,
        ]
    ],
    Callable[_FP, _FR],
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _FP],
        _FR,
    ],
    *,
    remove: Literal[1],
) -> Callable[_FP, _FR]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _T2, _FP],
        _FR,
    ],
    *,
    remove: Literal[2],
) -> Callable[_FP, _FR]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _T2, _T3, _FP],
        _FR,
    ],
    *,
    remove: Literal[3],
) -> Callable[_FP, _FR]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _T2, _T3, _T4, _FP],
        _FR,
    ],
    *,
    remove: Literal[4],
) -> Callable[_FP, _FR]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _FP],
        _FR,
    ],
    *,
    remove: Literal[5],
) -> Callable[_FP, _FR]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _FP],
        _FR,
    ],
    *,
    remove: Literal[6],
) -> Callable[_FP, _FR]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _FP],
        _FR,
    ],
    *,
    remove: Literal[7],
) -> Callable[_FP, _FR]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _FP],
        _FR,
    ],
    *,
    remove: Literal[8],
) -> Callable[_FP, _FR]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _FP],
        _FR,
    ],
    *,
    remove: Literal[9],
) -> Callable[_FP, _FR]: ...


@overload
def concatenate(
    *,
    transform: tuple[Literal[1], type[_As]],
) -> Callable[
    [
        Callable[
            Concatenate[Any, _FP],
            _FR,
        ]
    ],
    Callable[
        Concatenate[_As, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    *,
    transform: tuple[Literal[2], type[_As]],
) -> Callable[
    [
        Callable[
            Concatenate[_T1, Any, _FP],
            _FR,
        ]
    ],
    Callable[
        Concatenate[_T1, _As, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    *,
    transform: tuple[Literal[3], type[_As]],
) -> Callable[
    [
        Callable[
            Concatenate[_T1, _T2, Any, _FP],
            _FR,
        ]
    ],
    Callable[
        Concatenate[_T1, _T2, _As, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    *,
    transform: tuple[Literal[4], type[_As]],
) -> Callable[
    [
        Callable[
            Concatenate[_T1, _T2, _T3, Any, _FP],
            _FR,
        ]
    ],
    Callable[
        Concatenate[_T1, _T2, _T3, _As, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    *,
    transform: tuple[Literal[5], type[_As]],
) -> Callable[
    [
        Callable[
            Concatenate[_T1, _T2, _T3, _T4, Any, _FP],
            _FR,
        ]
    ],
    Callable[
        Concatenate[_T1, _T2, _T3, _T4, _As, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    *,
    transform: tuple[Literal[6], type[_As]],
) -> Callable[
    [
        Callable[
            Concatenate[_T1, _T2, _T3, _T4, _T5, Any, _FP],
            _FR,
        ]
    ],
    Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _As, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    *,
    transform: tuple[Literal[7], type[_As]],
) -> Callable[
    [
        Callable[
            Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, Any, _FP],
            _FR,
        ]
    ],
    Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _As, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    *,
    transform: tuple[Literal[8], type[_As]],
) -> Callable[
    [
        Callable[
            Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, Any, _FP],
            _FR,
        ]
    ],
    Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _As, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    *,
    transform: tuple[Literal[9], type[_As]],
) -> Callable[
    [
        Callable[
            Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, Any, _FP],
            _FR,
        ]
    ],
    Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _As, _FP],
        _FR,
    ],
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _FP],
        _FR,
    ],
    *,
    transform: tuple[Literal[1], type[_As]],
) -> Callable[
    Concatenate[_As, _FP],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _T2, _FP],
        _FR,
    ],
    *,
    transform: tuple[Literal[2], type[_As]],
) -> Callable[
    Concatenate[_T1, _As, _FP],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _T2, _T3, _FP],
        _FR,
    ],
    *,
    transform: tuple[Literal[3], type[_As]],
) -> Callable[
    Concatenate[_T1, _T2, _As, _FP],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _T2, _T3, _T4, _FP],
        _FR,
    ],
    *,
    transform: tuple[Literal[4], type[_As]],
) -> Callable[
    Concatenate[_T1, _T2, _T3, _As, _FP],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _FP],
        _FR,
    ],
    *,
    transform: tuple[Literal[5], type[_As]],
) -> Callable[
    Concatenate[_T1, _T2, _T3, _T4, _As, _FP],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _FP],
        _FR,
    ],
    *,
    transform: tuple[Literal[6], type[_As]],
) -> Callable[
    Concatenate[_T1, _T2, _T3, _T4, _T5, _As, _FP],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _FP],
        _FR,
    ],
    *,
    transform: tuple[Literal[7], type[_As]],
) -> Callable[
    Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _As, _FP],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _FP],
        _FR,
    ],
    *,
    transform: tuple[Literal[8], type[_As]],
) -> Callable[
    Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _As, _FP],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _FP],
        _FR,
    ],
    *,
    transform: tuple[Literal[9], type[_As]],
) -> Callable[
    Concatenate[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _As, _FP],
    _FR,
]: ...


def concatenate(
    __func: Callable | None = None, *, add=None, remove=None, transform=None
) -> Callable:
    "adds, removes or transforms parameters of a callable."

    if __func:
        return __func

    def wrapper(func):
        return func

    return wrapper
