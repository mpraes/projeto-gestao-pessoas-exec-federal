from app.extract.extract_as_csv import extract_from_ods
import pandas as pd

def test_extract_as_csv_prints_dataframe(mocker):
    mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    mocker.patch('pandas.read_excel', return_value=mock_df)
    mock_print = mocker.patch('builtins.print')

    extract_from_ods("fake_link.ods")
    mock_print.assert_called_once_with(mock_df)
