import pytest
from API.impulses import BaseImpulse, Datapoint, DatapointSeries, TimeSeriesImpulse, ConstantImpulse

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

def test_time_series_impulse_init(datapoint_series):
    series = DatapointSeries(datapoint_series)
    time_start = 1
    time_end = 3
    impulse = TimeSeriesImpulse(series, time_start, time_end)
    
    assert impulse.series == series
    assert impulse.time_start == time_start
    assert impulse.time_end == time_end

def test_time_series_impulse_from_series(datapoint_series):
    series = DatapointSeries(datapoint_series)
    impulse = TimeSeriesImpulse.from_series(series)
    
    assert impulse.series == series
    assert impulse.time_start == series.time_at(0)
    assert impulse.time_end == series.time_at(-1)

def test_base_impulse_empty_series():
    impulse = BaseImpulse([])
    sum_impulse = impulse.sum()
    count_impulse = impulse.count()
    
    assert len(sum_impulse.series) == 0
    assert len(count_impulse.series) == 0

def test_base_impulse_invalid_datapoint():
    with pytest.raises(TypeError):
        BaseImpulse([Datapoint(unix_time=1, value="invalid")])

def test_constant_impulse_invalid_value():
    with pytest.raises(TypeError):
        ConstantImpulse("invalid")

def test_time_series_impulse_invalid_time_range(datapoint_series):
    series = DatapointSeries(datapoint_series)
    with pytest.raises(ValueError):
        TimeSeriesImpulse(series, time_start=3, time_end=1)

def test_time_series_impulse_empty_series():
    series = DatapointSeries([])
    with pytest.raises(ValueError):
        TimeSeriesImpulse(series, time_start=1, time_end=3)

def test_creating_base_impulse_from_wrong_type():
    with pytest.raises(TypeError):
        BaseImpulse("invalid")
    with pytest.raises(TypeError):
        BaseImpulse(5)
    with pytest.raises(TypeError):
        BaseImpulse([5.0, 10.0])
    with pytest.raises(TypeError):
        BaseImpulse([Datapoint(unix_time=1, value=10.0), 5.0])    