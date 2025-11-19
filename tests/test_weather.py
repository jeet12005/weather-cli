"""Module test_weather.py."""


def test_merge_hourly_handles_none():
    assert merge_hourly(None) is None
