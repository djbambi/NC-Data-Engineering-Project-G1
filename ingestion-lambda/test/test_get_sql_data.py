from get_sql_data import get_sql_data
from test_data.mock_queries import all_tables_query, all_data_query, column_names_query, partial_column_names_query, partial_data_query
from unittest.mock import patch, Mock
import pg8000.native as pg

test_time = '2020-02-28 08:00:13.016000'


mock_connection = Mock()
mock_connection.call_count = 0


def return_data_query(*args, time=test_time):
    mock_connection.call_count += 1

    if mock_connection.call_count <= 1:
        mock_connection.columns = column_names_query[0]
        return all_tables_query
    else:   
        mock_connection.columns = column_names_query[mock_connection.call_count - 2]
        return all_data_query[mock_connection.call_count - 2]


mock_connection.run.side_effect = return_data_query


@patch.object(pg, "Connection", return_value=mock_connection)
def test_dictionary_has_correct_keys(*args):

    result = get_sql_data(test_time) 
    mock_connection.call_count = 0

    assert "Table1" in result
    assert "design" in result
    assert "transaction" in result
    assert "purchase_order" in result
    assert "payment_type" in result


@patch.object(pg, "Connection", return_value=mock_connection)
def test_tables_have_correct_length(*args):

    result = get_sql_data(test_time) 
    mock_connection.call_count = 0

    assert len(result["Table1"]) == 4
    assert len(result["transaction"]) == 4
    assert len(result["payment_type"]) == 4


@patch.object(pg, "Connection", return_value=mock_connection)
def test_tables_have_correct_contents(*args):

    result = get_sql_data(test_time) 
    mock_connection.call_count = 0

    assert "delivery_contact" in result["Table1"][0]
    assert "Fahey and Sons" in result["Table1"][1]
    assert "Myra Kovacek" in result["Table1"][3]

    assert "payment_type_name" in result["payment_type"][0]
    assert 1 in result["payment_type"][1]
    assert "PURCHASE_PAYMENT" in result["payment_type"][3]


@patch.object(pg, "Connection", return_value=mock_connection)
def test_returns_full_tables(*args):

    result = get_sql_data(test_time) 
    mock_connection.call_count = 0

    assert "full_address_table" in result
    assert "full_department_table" in result


@patch.object(pg, "Connection", return_value=mock_connection)
def test_full_tables_should_contain_complete_table(*args):
    result = get_sql_data(test_time) 
    mock_connection.call_count = 0

    assert len(result["full_address_table"]) == 31
    assert len(result["full_department_table"]) == 9


@patch.object(pg, "Connection", return_value=mock_connection)
def test_full_tables_have_correct_values(*args):
    result = get_sql_data(test_time)
    mock_connection.call_count = 0

    assert "test_address_id" in result["full_address_table"][0]
    assert "test_last_updated" in result["full_address_table"][0]
    assert "test_department_id" in result["full_department_table"][0]
    assert "test_last_updated" in result["full_department_table"][0]


mock_updates = Mock()
mock_updates.call_count = 0


def return_partial_query(*args, time=test_time):
    mock_updates.call_count += 1

    if mock_updates.call_count <= 1:
        mock_updates.columns = partial_column_names_query[0]
        return all_tables_query
    else:   
        mock_updates.columns = partial_column_names_query[mock_updates.call_count - 2]
        return partial_data_query[mock_updates.call_count - 2]


mock_updates.run.side_effect = return_partial_query


@patch.object(pg, "Connection", return_value=mock_updates)
def test_ignores_empty_tables(*args):
    result = get_sql_data(test_time)
    mock_updates.call_count = 0

    assert "Table1" not in result
    assert "Table2" in result
    assert "department" in result
    assert "full_department_table" in result
    assert "design" not in result
    assert "address" not in result
    assert "full_address_table" not in result
    assert "purchase_order" in result
    assert "payment_type" in result
