import pandas as pd
from pull_stock_data import filter_first_day_month


def test_filter_first_day_month():
    dates = pd.date_range('2024-01-01', '2024-03-31', freq='D')
    df = pd.DataFrame({'close': range(len(dates))}, index=dates)
    result = filter_first_day_month(df)
    assert len(result) == 3
    assert result.index[0] == pd.Timestamp('2024-01-01')
    assert result.index[1] == pd.Timestamp('2024-02-01')
    assert result.index[2] == pd.Timestamp('2024-03-01')
