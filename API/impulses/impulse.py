from __future__ import annotations
import abc
from dataclasses import dataclass
from typing import Callable, Final, Iterable, Tuple, List

@dataclass
class Datapoint:
    """
    Structure which stores a single value in a timepoint
    """
    unix_time: int
    value: float

    def is_not_after(self, other: Datapoint) -> bool:
        """
        Determine if the current Datapoint is not after another Datapoint.

        Args:
            other (Datapoint): The Datapoint to compare against.

        Returns:
            bool: True if the current Datapoint's unix_time is less than or equal to the other Datapoint's unix_time, False otherwise.
        """
        return self.unix_time <= other.unix_time

    def to_tuple(self) -> Tuple[int, float]:
        """
        Convert the impulse data to a tuple.

        Returns:
            Tuple[int, float]: A tuple containing the unix time as an integer and the value as a float.
        """
        return (self.unix_time, self.value)

    def __str__(self):
        return f"Datapoint({self.unix_time}, {self.value})"
    
    def __repr__(self):
        return str(self)

class DatapointSeries(Iterable[Datapoint]):
    """
    A class to represent a series of Datapoint objects.
    """
    def __init__(self, series: Iterable[Datapoint]):
        self.series = series

    def time_at(self, idx: int) -> int:
        """
        Get the unix time at a specific index.
        """
        return self.series[idx].unix_time
    
    def value_at(self, idx: int) -> float:
        """
        Get the value at a specific index.
        """
        return self.series[idx].value
 
@dataclass
# Maybe we should just name it 'Impulse'
class EvaluatedImpulse(abc.ABC):
    """
    Abstract class for an impulse.
    """
    value: float

    @classmethod
    def with_value_from_series(cls, series: DatapointSeries, operator: Callable[[List[float]], float]) -> float:
        """
        Computes a value from a series of datapoints using a specified operator.

        Args:
            series (DatapointSeries): A series of datapoints from which values are extracted.
            operator (Callable[[List[float]], float]): A function that takes a list of floats and returns a single float.

        Returns:
            float: The result of applying the operator to the list of datapoint values.

        Example:
            >>> series = DatapointSeries([Datapoint(1, 1.0), Datapoint(2, 2.0), Datapoint(3, 3.0)])
            >>> EvaluatedImpulse.with_value_from_series(series, sum)
        """
        return cls(operator([datapoint.value for datapoint in series.series]))

class ConstantImpulse(EvaluatedImpulse):
    """
    A class representing a constant impulse.
    """
    def __init__(self, value: float):
        self.value: Final[float] = value

class TimeSeriesImpulse(EvaluatedImpulse):
    """
    A class representing a time series impulse.
    """
    def __init__(self, series: DatapointSeries, time_start: int, time_end: int):
        self.series = series
        self.time_start = time_start
        self.time_end = time_end
    
    def get_mean(self) -> float:
        return self.get_sum() / len(self.series)
    
    def get_sum(self) -> float:
        return sum([datapoint.value for datapoint in self.series])

    @classmethod
    def from_series(cls, series: DatapointSeries):
        """
        Create a TimeSeriesImpulse from a series of datapoints.
        """
        return cls(series, series.time_at(0), series.time_at(-1))