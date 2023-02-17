from src.get_updated_data import *
from test_data.test_data_base_tables import *
from unittest.mock import Mock, patch

test_items  = [test_names, test_counterparty, test_currency, test_department, test_design, test_payment, test_transaction, test_staff, test_sales_order, test_address, test_purchase_order, test_payment_type]

mock_response = Mock()

# counter = 0

def return_patch_data(*args):    
    patched_data  = test_items[0]
    # counter = counter + 1

    return patched_data

mock_response.side_effect = return_patch_data
time = '2023-02-15 08:00:13.016000'

def test_returns_a_list(): 
    time = '2023-02-15 08:00:13.016000'  
    assert type(get_updated_data(time)) == list  

def test_returns_dictionary_with_tablenames_as_keyes():
    time = '2023-02-15 08:00:13.016000'
    output = get_updated_data(time)
    
    table_names = []
    for i in output:        
        table_names.append(list(i)[0])

    expected_table_names = ['counterparty', 'currency', 'department', 'design', 'payment', 'transaction', 'staff', 'sales_order', 'address', 'purchase_order', 'payment_type']

    for name in expected_table_names:
        assert name in table_names

    assert len(table_names) == 11

def test_value_of_each_table_name_key_is_a_list_of_table_data():
    time = '2023-02-15 08:00:13.016000'
    output = get_updated_data(time)    
    
    table_names = ['counterparty', 'currency', 'department', 'design', 'payment', 'transaction', 'staff', 'sales_order', 'address', 'purchase_order', 'payment_type']    

    for index, name in enumerate(table_names):
        assert type(output[index][name]) == list

def test_table_data_is_correct():
    time = '2023-02-15 08:00:13.016000'
    output = get_updated_data(time)      
     
    for row in output[0]['counterparty']:
        assert len(row) == 7

    for row in output[2]['department']:
        assert len(row) == 6

    for row in output[10]['payment_type']:
        assert len(row) == 4

    
