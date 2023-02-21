from src.ingest import *

def test_returns_a_list():    
    assert type(ingest()) == list


def test_returns_dictionary_with_tablenames_as_keyes():
    output = ingest()
    
    table_names = []
    for i in output:        
        table_names.append(list(i)[0])

    expected_table_names = ['counterparty', 'currency', 'department', 'design', 'payment', 'transaction', 'staff', 'sales_order', 'address', 'purchase_order', 'payment_type']

    for name in expected_table_names:
        assert name in table_names

    assert len(table_names) == 11

def test_value_of_each_table_name_key_is_a_list_of_table_data():
    output = ingest()    
    
    table_names = ['counterparty', 'currency', 'department', 'design', 'payment', 'transaction', 'staff', 'sales_order', 'address', 'purchase_order', 'payment_type']   

    for index, name in enumerate(table_names):
        assert type(output[index][name]) == list

def test_table_data_is_correct():
    output = ingest()   
     
    for row in output[0]['counterparty']:
        assert len(row) == 7

    for row in output[2]['department']:
        assert len(row) == 6

    for row in output[10]['payment_type']:
        assert len(row) == 4


    
 