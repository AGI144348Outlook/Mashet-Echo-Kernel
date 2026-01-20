from dataclasses import dataclass


@dataclass(frozen=True)
class ScalarCarrier:
    state: str = "undefined"


@dataclass(frozen=True)
class VectorCarrier:
    slots: tuple


@dataclass(frozen=True)
class MatrixCarrier:
    rows: tuple


@dataclass(frozen=True)
class Point:
    identifier: str


@dataclass(frozen=True)
class DimensionSlot:
    assigned: bool = False
