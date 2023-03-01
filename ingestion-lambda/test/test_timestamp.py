from timestamp import create_timestamp, retrieve_timestamp
from datetime import datetime
import unittest
from unittest.mock import patch, Mock
import json
from botocore.response import StreamingBody
import io

body_json = '2023-02-22 11:51'

body_encoded = json.dumps(body_json).encode('utf-8')

body = StreamingBody(
    io.BytesIO(body_encoded),
    len(body_encoded)
)

mocked_response = {
    'Body': body
}
mocked_list_response = {
    'Contents': "contents"
}
mocked_list_error_response = {
}


class Test(unittest.TestCase):

    @patch('timestamp.datetime')
    def test_create_timestamp_returns_date_and_time_as_a_string(
            self, datetime_mock):
        datetime_mock.now = Mock(return_value=datetime(2023, 2, 22, 11, 43))

        assert create_timestamp() == "2023-02-22 11:43"

    @patch('timestamp.client')
    def test_retrieve_timestamp_reads_latest_timestamp_from_s3(
            self, boto3_mock):
        boto3_mock.get_object = Mock(return_value=mocked_response)
        boto3_mock.list_objects = Mock(return_value=mocked_list_response)

        assert retrieve_timestamp().strip('"') == "2023-02-22 11:51"

    @patch('timestamp.client')
    def test_retrieve_timestamp_returns_default_if_invalid_response(
            self, boto3_mock):
        boto3_mock.list_objects = Mock(return_value=mocked_list_error_response)

        assert retrieve_timestamp() == "2020-01-01 00:00"
