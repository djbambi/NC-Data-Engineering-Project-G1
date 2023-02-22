from src.timestamp import create_timestamp
from datetime import datetime
import unittest
from unittest.mock import patch, Mock

# def test_returns_date_and_time_as_a_string():
    # time_mock = Mock()
    # return_value="2023-02-22 11:43:42.214110"
    # with patch(dt=DEFAULT) as mock_i:
    #     mock.dt.now.return_value = datetime(2023, 2, 22, 11, 43)
    
    # with patch("src.timestamp.datetime.now") as m:
    #     m.return_value = Mock(return_value=datetime.datetime(2023, 2, 22, 11, 43))
    #     assert create_timestamp() == "H"
    # assert create_timestamp() == datetime.now().strftime("%Y-%m-%d %H:%M")


class Test(unittest.TestCase):

    @patch('src.timestamp.datetime')
    def test_returns_date_and_time_as_a_string(self, datetime_mock):
        datetime_mock.now = Mock(return_value=datetime(2023, 2, 22, 11, 43))
        
        assert create_timestamp() == "2023-02-22 11:43"