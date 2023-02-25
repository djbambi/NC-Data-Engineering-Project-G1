from src.timestamp import create_timestamp, retrieve_timestamp, upload_timestamp
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


class Test(unittest.TestCase):

    # @patch('src.timestamp.datetime')
    # def test_create_timestamp_returns_date_and_time_as_a_string(self, datetime_mock):
    #     datetime_mock.now = Mock(return_value=datetime(2023, 2, 22, 11, 43))
        
    #     assert create_timestamp() == "2023-02-22 11:43"


    @patch('src.timestamp.client')
    def test_retrieve_timestamp_reads_latest_timestamp_from_s3(self, boto3_mock):
        boto3_mock.get_object = Mock(return_value=mocked_response)
        
        assert retrieve_timestamp()[1:17] == "2023-02-22 11:51"


# def test_upload_timestamp_uploads_to_s3():
#     assert upload_timestamp("2023-02-22 12:51") == None