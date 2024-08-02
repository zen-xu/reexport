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


_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")
_T6 = TypeVar("_T6")
_T7 = TypeVar("_T7")
_T8 = TypeVar("_T8")
_T9 = TypeVar("_T9")


_As1 = TypeVar("_As1")
_As2 = TypeVar("_As2")
_As3 = TypeVar("_As3")
_As4 = TypeVar("_As4")
_As5 = TypeVar("_As5")
_As6 = TypeVar("_As6")
_As7 = TypeVar("_As7")
_As8 = TypeVar("_As8")
_As9 = TypeVar("_As9")


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
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
) -> Callable[
    Concatenate[
        _T1,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
    __t2: type[_T2],
) -> Callable[
    Concatenate[
        _T1,
        _T2,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
) -> Callable[
    Concatenate[
        _T1,
        _T2,
        _T3,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
) -> Callable[
    Concatenate[
        _T1,
        _T2,
        _T3,
        _T4,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
    __t5: type[_T5],
) -> Callable[
    Concatenate[
        _T1,
        _T2,
        _T3,
        _T4,
        _T5,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
    __t5: type[_T5],
    __t6: type[_T6],
) -> Callable[
    Concatenate[
        _T1,
        _T2,
        _T3,
        _T4,
        _T5,
        _T6,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
    __t5: type[_T5],
    __t6: type[_T6],
    __t7: type[_T7],
) -> Callable[
    Concatenate[
        _T1,
        _T2,
        _T3,
        _T4,
        _T5,
        _T6,
        _T7,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
    __t5: type[_T5],
    __t6: type[_T6],
    __t7: type[_T7],
    __t8: type[_T8],
) -> Callable[
    Concatenate[
        _T1,
        _T2,
        _T3,
        _T4,
        _T5,
        _T6,
        _T7,
        _T8,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
    __t5: type[_T5],
    __t6: type[_T6],
    __t7: type[_T7],
    __t8: type[_T8],
    __t9: type[_T9],
) -> Callable[
    Concatenate[
        _T1,
        _T2,
        _T3,
        _T4,
        _T5,
        _T6,
        _T7,
        _T8,
        _T9,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
    *,
    kind: Literal["add"],
) -> Callable[
    Concatenate[
        _T1,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
    __t2: type[_T2],
    *,
    kind: Literal["add"],
) -> Callable[
    Concatenate[
        _T1,
        _T2,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    *,
    kind: Literal["add"],
) -> Callable[
    Concatenate[
        _T1,
        _T2,
        _T3,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
    *,
    kind: Literal["add"],
) -> Callable[
    Concatenate[
        _T1,
        _T2,
        _T3,
        _T4,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
    __t5: type[_T5],
    *,
    kind: Literal["add"],
) -> Callable[
    Concatenate[
        _T1,
        _T2,
        _T3,
        _T4,
        _T5,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
    __t5: type[_T5],
    __t6: type[_T6],
    *,
    kind: Literal["add"],
) -> Callable[
    Concatenate[
        _T1,
        _T2,
        _T3,
        _T4,
        _T5,
        _T6,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
    __t5: type[_T5],
    __t6: type[_T6],
    __t7: type[_T7],
    *,
    kind: Literal["add"],
) -> Callable[
    Concatenate[
        _T1,
        _T2,
        _T3,
        _T4,
        _T5,
        _T6,
        _T7,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
    __t5: type[_T5],
    __t6: type[_T6],
    __t7: type[_T7],
    __t8: type[_T8],
    *,
    kind: Literal["add"],
) -> Callable[
    Concatenate[
        _T1,
        _T2,
        _T3,
        _T4,
        _T5,
        _T6,
        _T7,
        _T8,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[_FP, _FR],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
    __t5: type[_T5],
    __t6: type[_T6],
    __t7: type[_T7],
    __t8: type[_T8],
    __t9: type[_T9],
    *,
    kind: Literal["add"],
) -> Callable[
    Concatenate[
        _T1,
        _T2,
        _T3,
        _T4,
        _T5,
        _T6,
        _T7,
        _T8,
        _T9,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_T1],
    *,
    kind: Literal["remove"],
) -> Callable[
    _FP,
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _T2,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_T1],
    __t2: type[_T2],
    *,
    kind: Literal["remove"],
) -> Callable[
    _FP,
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _T2,
            _T3,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    *,
    kind: Literal["remove"],
) -> Callable[
    _FP,
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _T2,
            _T3,
            _T4,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
    *,
    kind: Literal["remove"],
) -> Callable[
    _FP,
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _T2,
            _T3,
            _T4,
            _T5,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
    __t5: type[_T5],
    *,
    kind: Literal["remove"],
) -> Callable[
    _FP,
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _T2,
            _T3,
            _T4,
            _T5,
            _T6,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
    __t5: type[_T5],
    __t6: type[_T6],
    *,
    kind: Literal["remove"],
) -> Callable[
    _FP,
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _T2,
            _T3,
            _T4,
            _T5,
            _T6,
            _T7,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
    __t5: type[_T5],
    __t6: type[_T6],
    __t7: type[_T7],
    *,
    kind: Literal["remove"],
) -> Callable[
    _FP,
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _T2,
            _T3,
            _T4,
            _T5,
            _T6,
            _T7,
            _T8,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
    __t5: type[_T5],
    __t6: type[_T6],
    __t7: type[_T7],
    __t8: type[_T8],
    *,
    kind: Literal["remove"],
) -> Callable[
    _FP,
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _T2,
            _T3,
            _T4,
            _T5,
            _T6,
            _T7,
            _T8,
            _T9,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_T1],
    __t2: type[_T2],
    __t3: type[_T3],
    __t4: type[_T4],
    __t5: type[_T5],
    __t6: type[_T6],
    __t7: type[_T7],
    __t8: type[_T8],
    __t9: type[_T9],
    *,
    kind: Literal["remove"],
) -> Callable[
    _FP,
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_As1],
    *,
    kind: Literal["transform"],
) -> Callable[
    Concatenate[
        _As1,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _T2,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_As1],
    __t2: type[_As2],
    *,
    kind: Literal["transform"],
) -> Callable[
    Concatenate[
        _As1,
        _As2,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _T2,
            _T3,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_As1],
    __t2: type[_As2],
    __t3: type[_As3],
    *,
    kind: Literal["transform"],
) -> Callable[
    Concatenate[
        _As1,
        _As2,
        _As3,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _T2,
            _T3,
            _T4,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_As1],
    __t2: type[_As2],
    __t3: type[_As3],
    __t4: type[_As4],
    *,
    kind: Literal["transform"],
) -> Callable[
    Concatenate[
        _As1,
        _As2,
        _As3,
        _As4,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _T2,
            _T3,
            _T4,
            _T5,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_As1],
    __t2: type[_As2],
    __t3: type[_As3],
    __t4: type[_As4],
    __t5: type[_As5],
    *,
    kind: Literal["transform"],
) -> Callable[
    Concatenate[
        _As1,
        _As2,
        _As3,
        _As4,
        _As5,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _T2,
            _T3,
            _T4,
            _T5,
            _T6,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_As1],
    __t2: type[_As2],
    __t3: type[_As3],
    __t4: type[_As4],
    __t5: type[_As5],
    __t6: type[_As6],
    *,
    kind: Literal["transform"],
) -> Callable[
    Concatenate[
        _As1,
        _As2,
        _As3,
        _As4,
        _As5,
        _As6,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _T2,
            _T3,
            _T4,
            _T5,
            _T6,
            _T7,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_As1],
    __t2: type[_As2],
    __t3: type[_As3],
    __t4: type[_As4],
    __t5: type[_As5],
    __t6: type[_As6],
    __t7: type[_As7],
    *,
    kind: Literal["transform"],
) -> Callable[
    Concatenate[
        _As1,
        _As2,
        _As3,
        _As4,
        _As5,
        _As6,
        _As7,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _T2,
            _T3,
            _T4,
            _T5,
            _T6,
            _T7,
            _T8,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_As1],
    __t2: type[_As2],
    __t3: type[_As3],
    __t4: type[_As4],
    __t5: type[_As5],
    __t6: type[_As6],
    __t7: type[_As7],
    __t8: type[_As8],
    *,
    kind: Literal["transform"],
) -> Callable[
    Concatenate[
        _As1,
        _As2,
        _As3,
        _As4,
        _As5,
        _As6,
        _As7,
        _As8,
        _FP,
    ],
    _FR,
]: ...


@overload
def concatenate(
    __func: Callable[
        Concatenate[
            _T1,
            _T2,
            _T3,
            _T4,
            _T5,
            _T6,
            _T7,
            _T8,
            _T9,
            _FP,
        ],
        _FR,
    ],
    __t1: type[_As1],
    __t2: type[_As2],
    __t3: type[_As3],
    __t4: type[_As4],
    __t5: type[_As5],
    __t6: type[_As6],
    __t7: type[_As7],
    __t8: type[_As8],
    __t9: type[_As9],
    *,
    kind: Literal["transform"],
) -> Callable[
    Concatenate[
        _As1,
        _As2,
        _As3,
        _As4,
        _As5,
        _As6,
        _As7,
        _As8,
        _As9,
        _FP,
    ],
    _FR,
]: ...


def concatenate(__func: Callable, *concatenate, kind="add"):
    "adds, removes or transforms parameters of a callable."
    return __func  # type: ignore[return-type]
