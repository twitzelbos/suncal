import datetime as dt

from suncal.main import suncal

# Test main of module --------------------------------------------------------------------------------------------------
suncal(
    calendar_title="Sonne",
    from_date=dt.date(2021, 4, 22),
    to_date=dt.date(2021, 4, 23),
    event="sunrise",
    timezone="Europe/Berlin",
    longitude=13.23,
    latitude=52.32,
    return_val="api",
)
