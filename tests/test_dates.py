from datetime import date

import pytest

from regolith.dates import (month_to_str_int,
                            day_to_str_int,
                            find_gaps_overlaps)


@pytest.mark.parametrize(
    "input,expected",
    [
        (1, "01"),
        (10, "10"),
        ("Oct", "10"),
        ("Jan", "01"),
    ],
)
def test_month_to_str(input, expected):
    assert month_to_str_int(input) == expected
import datetime
from regolith.dates import begin_end_date, date_to_float, month_to_int


@pytest.mark.parametrize(
    "input,expected_begin,expected_end",
    [
        ({'begin_day': 15, 'begin_month': 'Oct', 'begin_year': 2019,
          'end_day': 21, 'end_month': 'Nov', 'end_year': 2025},
         datetime.date(2019, 10, 15), datetime.date(2025, 11, 21)),
        ({'begin_month': 'Oct', 'begin_year': 2019,
          'end_month': 'Nov', 'end_year': 2025},
         datetime.date(2019, 10, 1), datetime.date(2025, 11, 30)),
        ({'begin_month': 'Oct', 'begin_year': 2019,
          'end_month': 'Feb', 'end_year': 2025},
         datetime.date(2019, 10, 1), datetime.date(2025, 2, 28)),
    ],
)
def test_begin_end_date(input, expected_begin, expected_end):
    b, e = begin_end_date(input)
    assert b == expected_begin
    assert e == expected_end



@pytest.mark.parametrize(
    "input,expected",
    [
        ('Jan', 1),
        (1, 1),
        ('February', 2)
    ],
)
def test_month_to_int(input, expected):
    assert month_to_int(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ([2019, 1, 15], 2019.0115),
        ([2019, 'May', 0], 2019.05),
        ([2019, 'February', 2], 2019.0202)
    ],
)
def test_date_to_float(input, expected):
    assert date_to_float(input[0], input[1], d=input[2]) == expected

@pytest.mark.parametrize(
    "input,expected",
    [
            (1, "01"),
    (10, "10"),
    ],
)
def test_day_to_str(input, expected):
    assert day_to_str_int(input) == expected


@pytest.mark.parametrize(
    "input,flag,expected",
    [
        ([(date(2020, 1, 1), date(2020, 1, 31)),
         (date(2020, 2, 1), date(2020, 2, 5))], False, True),
        ([(date(2020, 2, 1), date(2020, 2, 5)),
         (date(2020, 1, 1), date(2020, 1, 31))], False, True),
        ([(date(2020, 1, 1), date(2020, 1, 31)),
         (date(2020, 2, 2), date(2020, 2, 5))], False, False),
        ([(date(2020, 1, 1), date(2020, 1, 31)),
         (date(2020, 1, 31), date(2020, 2, 5))], False, False),
        ([(date(2020, 1, 1), date(2020, 1, 31)),
         (date(2020, 1, 31), date(2020, 2, 5))], True, True),
        ([(date(2020, 1, 1), date(2020, 1, 31)),
         (date(2020, 2, 1), date(2020, 2, 5)),
         (date(2020, 2, 6), date(2020, 2, 7))], False, True),
        ([(date(2020, 1, 1), date(2020, 1, 31)),
         (date(2020, 2, 1), date(2020, 2, 5)),
         (date(2020, 2, 7), date(2020, 2, 7))], False, False)
    ],
)
def test_find_gaps_overlaps(input, flag, expected):
    actual = find_gaps_overlaps(input, overlaps_ok=flag)
    assert actual == expected
