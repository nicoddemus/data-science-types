from typing import List, Tuple, Type, Union, overload, Optional, Dict, TypeVar, Iterator, Generic
from typing_extensions import Literal
import numpy as _np

from .indexing import _LocIndexer, _iLocIndexer
from .frame import DataFrame
from .indexes import Index
from .strings import StringMethods

_str = str  # needed because Series has a property called "str"...

_DType = TypeVar("_DType", bool, int, float, object)
_ListLike = Union[_np.ndarray, List[_DType], Dict[_str, _np.ndarray]]
# dtypes for numpy
_DTypeNp = TypeVar(
    "_DTypeNp",
    _np.bool_,
    _np.int8,
    _np.int16,
    _np.int32,
    _np.int64,
    _np.float32,
    _np.float64,
    _np.str_,
)

class Series(Generic[_DType]):
    def __init__(
        self,
        data: Optional[
            Union[_ListLike[_DType], Series[_DType], Dict[int, _DType], Dict[str, _DType]]
        ],
        index: Union[_str, int, Series] = ...,
    ): ...
    # magic methods
    def __and__(self, other: Series) -> Series: ...
    def __eq__(self, other: object) -> Series: ...  # type: ignore
    def __ge__(self, other: float) -> Series[bool]: ...
    def __gt__(self, other: float) -> Series[bool]: ...
    def __le__(self, other: float) -> Series[bool]: ...
    def __lt__(self, other: float) -> Series[bool]: ...
    def __ne__(self, other: object) -> Series: ...  # type: ignore
    def __mul__(self, other: float) -> Series[float]: ...
    @overload
    def __getitem__(self, idx: Union[List[_str], Index[int], Series, slice]) -> Series: ...
    @overload
    def __getitem__(self, idx: int) -> float: ...
    def __invert__(self: Series[bool]) -> Series[bool]: ...
    def __iter__(self) -> Iterator[_DType]: ...
    def __truediv__(self, other: object) -> Series: ...
    #
    # properties
    @property
    def iloc(self) -> _iLocIndexer: ...
    @property
    def index(self) -> Index: ...
    @property
    def item(self) -> _DType: ...
    @property
    def loc(self) -> _LocIndexer: ...
    @property
    def shape(self) -> Tuple[int, ...]: ...
    @property
    def str(self) -> StringMethods: ...
    @property
    def values(self) -> _np.ndarray: ...
    #
    # methods
    def all(self, axis: int = ..., bool_only: bool = ...) -> bool: ...
    def corr(
        self, other: Series, method: Literal["pearson", "kendall", "spearman"] = ...
    ) -> float: ...
    def count(self) -> int: ...
    def isnull(self) -> Series: ...
    def max(self) -> float: ...
    def mean(self) -> float: ...
    def median(self) -> float: ...
    def min(self) -> float: ...
    def mode(self) -> Series: ...
    def notnull(self) -> Series: ...
    def nunique(self) -> int: ...
    def replace(self, to_replace: int, value: int, inplace: bool) -> None: ...
    def std(self) -> float: ...
    def sum(self) -> float: ...
    def to_dict(self) -> Dict[Union[int, _str], _DType]: ...
    def to_frame(self, name: Optional[_str]) -> DataFrame: ...
    @overload
    def to_numpy(self: Series[bool]) -> _np.ndarray[_np.bool_]: ...
    @overload
    def to_numpy(self: Series[int]) -> _np.ndarray[_np.int64]: ...
    @overload
    def to_numpy(self: Series[float]) -> _np.ndarray[_np.float64]: ...
    @overload
    def to_numpy(self: Series[object]) -> _np.ndarray: ...
    @overload
    def to_numpy(self, dtype: Type[_DTypeNp]) -> _np.ndarray[_DTypeNp]: ...
    def unique(self) -> _np.ndarray: ...
    def update(self, other: Series) -> None: ...
    def value_counts(self, normalize: bool = False) -> Series: ...
