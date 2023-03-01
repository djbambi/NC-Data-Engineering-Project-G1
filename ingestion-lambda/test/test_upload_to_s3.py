from upload_to_s3 import upload_to_s3
from test_data.mock_get_sql_data_output import test_data, single_test_data
from unittest.mock import patch, Mock
import pytest

test_time = "2022-10-15 14:26"
test_bucket = "my_s3_bucket"


@patch("upload_to_s3.client")
def test_returns_count_of_files_uploaded(*args):
    assert upload_to_s3(single_test_data, test_time, test_bucket) == 1
    assert upload_to_s3(test_data, test_time, test_bucket) == 13


def raises_exception():
    raise Exception()


mock = Mock()
mock.put_object.side_effect = raises_exception


@patch("upload_to_s3.client", return_value=mock)
def test_raises_connection_error(*args):
    with pytest.raises(Exception) as e:
        upload_to_s3(single_test_data, test_time, test_bucket)

    assert type(e.value) == ConnectionError
    assert "Could not upload CSV files to ingestion bucket." in str(e.value)
