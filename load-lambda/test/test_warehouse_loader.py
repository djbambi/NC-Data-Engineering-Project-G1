from src.warehouse_loader import get_warehouse_connection
import pytest
from unittest.mock import Mock, patch
import pg8000.native as pg

mock_event = {
    "Records":[{"s3":{
        "bucket":{"name":"test_bucket"},
        "object":{"key":"test_file"}
    }}]
}
mock_host_name='host'
mock_password='password'
@patch.object(pg, 'Connection', return_value={})
def test_passes_creds_to_server(*args):
    get_warehouse_connection(mock_event, mock_host_name,mock_password)
    assert pg.Connection.call_args.kwargs['host']==mock_host_name
    assert pg.Connection.call_args.kwargs['password']==mock_password

mock_connection=Mock()
mock_connection.user=b'project_team_1'
mock_connection.password=1234
@patch.object(pg, 'Connection', return_value=mock_connection)
def test_returns_connection_when_called(*args):
    bucket_name, file_name, conn = get_warehouse_connection(mock_event, mock_host_name,mock_password) 
    assert conn.user==b'project_team_1'
    assert conn.password==1234

@patch.object(pg, 'Connection', return_value=mock_connection)
def test_returns_right_bucket_attributes(*args):
    bucket_name, file_name, conn = get_warehouse_connection(mock_event, mock_host_name,mock_password)
    assert bucket_name == 'test_bucket'
    assert file_name == 'test_file'