from __future__ import annotations
from dataclasses import dataclass
from typing import Final, List, Tuple


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


class DatapointSeries:
    """
    A class to represent a series of Datapoint objects.
    """

    def __init__(self, series: List[Datapoint]):
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
    
    def to_list(self) -> List[Datapoint]:
        """
        Convert the DatapointSeries to a list.
        """
        return self.series

    def __len__(self) -> int:
        return len(self.series)

    def __getitem__(self, idx: int) -> Datapoint:
        return self.series[idx]

    def __iter__(self):
        return iter(self.series)

    def __str__(self):
        return f"DatapointSeries({self.series})"

    def __repr__(self):
        return str(self)


@dataclass
class BaseImpulse(DatapointSeries):
    """
    Abstract class for an impulse.
    """
    def __init__(self, series: List[Datapoint]):
        super().__init__(series)

    def sum(self) -> BaseImpulse:
        """Get the BaseImpulse object containing the cumulative sum of the impulse.

        Returns:
            BaseImpulse: The cumulative sum of the impulse.
        """
        current_sum = 0.0
        sum_impulse: BaseImpulse = BaseImpulse([])

        for datapoint in self.series:
            current_sum += datapoint.value
            sum_impulse.series.append(Datapoint(datapoint.unix_time, current_sum))

        return sum_impulse

    def count(self) -> BaseImpulse:
        """
        Get a BaseImpulse object containing the count of the impulse.

        Returns:
            BaseImpulse: The count of the impulse.
        """
        return BaseImpulse(
            [Datapoint(dp.unix_time, float(value) + 1) for value, dp in enumerate(self.series)]
        )

class ConstantImpulse(BaseImpulse):
    """
    A class representing a constant impulse.
    """
    def __init__(self, value: float):
        self.value: Final[float] = value
