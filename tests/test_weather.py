"""Module test_weather.py."""


def test_merge_hourly_handles_none():
    assert merge_hourly(None) is None


def test_resolve_humidity_handles_none():
    assert resolve_humidity(None) is None


def test_parse_station_handles_none():
    assert parse_station(None) is None


def test_parse_station_handles_none():
    assert parse_station(None) is None


def test_split_temperature_handles_none():
    assert split_temperature(None) is None


def test_parse_station_handles_none():
    assert parse_station(None) is None


def test_split_temperature_handles_none():
    assert split_temperature(None) is None


def test_load_daily_handles_none():
    assert load_daily(None) is None


def test_normalize_wind_handles_none():
    assert normalize_wind(None) is None


def test_parse_station_handles_none():
    assert parse_station(None) is None


def test_split_station_handles_none():
    assert split_station(None) is None


def test_group_forecast_handles_none():
    assert group_forecast(None) is None


def test_split_temperature_handles_none():
    assert split_temperature(None) is None


def test_render_radar_handles_none():
    assert render_radar(None) is None


def test_sort_pressure_handles_none():
    assert sort_pressure(None) is None


def test_parse_station_handles_none():
    assert parse_station(None) is None


def test_resolve_alert_handles_none():
    assert resolve_alert(None) is None


def test_render_radar_handles_none():
    assert render_radar(None) is None
