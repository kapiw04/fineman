import pytest
from API.impulses import BaseImpulse, Datapoint, ConstantImpulse

@pytest.fixture
def datapoint_series():
    return [
        Datapoint(unix_time=1, value=10.0),
        Datapoint(unix_time=2, value=20.0),
        Datapoint(unix_time=3, value=30.0)
    ]

def test_base_impulse_sum(datapoint_series):
    impulse = BaseImpulse(datapoint_series)
    sum_impulse = impulse.sum()
    
    expected_series = [
        Datapoint(unix_time=1, value=10.0),
        Datapoint(unix_time=2, value=30.0),
        Datapoint(unix_time=3, value=60.0)
    ]
    
    assert len(sum_impulse.series) == len(expected_series)
    for i, expected in enumerate(expected_series):
        assert sum_impulse.series[i].unix_time == expected.unix_time
        assert sum_impulse.series[i].value == expected.value

def test_base_impulse_count(datapoint_series):
    impulse = BaseImpulse(datapoint_series)
    count_impulse = impulse.count()
    
    expected_series = [
        Datapoint(unix_time=1, value=1.0),
        Datapoint(unix_time=2, value=2.0),
        Datapoint(unix_time=3, value=3.0)
    ]
    
    assert len(count_impulse.series) == len(expected_series)
    for i, expected in enumerate(expected_series):
        assert count_impulse.series[i].unix_time == expected.unix_time
        assert count_impulse.series[i].value == expected.value
        assert isinstance(count_impulse.series[i].value, float)

def test_base_impulse_init(datapoint_series):
    impulse = BaseImpulse(datapoint_series)
    
    assert len(impulse.series) == len(datapoint_series)
    for i, datapoint in enumerate(datapoint_series):
        assert impulse.series[i].unix_time == datapoint.unix_time
        assert impulse.series[i].value == datapoint.value

@pytest.mark.parametrize("value", [5.0])
def test_constant_impulse_init(value):
    impulse = ConstantImpulse(value)
    assert impulse.value == value

def test_base_impulse_empty_series():
    impulse = BaseImpulse([])
    sum_impulse = impulse.sum()
    count_impulse = impulse.count()
    
    assert len(sum_impulse.series) == 0
    assert len(count_impulse.series) == 0
