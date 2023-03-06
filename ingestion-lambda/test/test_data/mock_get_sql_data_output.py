import datetime
from decimal import Decimal

test_data = {'counterparty': [['counterparty_id', 'counterparty_legal_name', 'legal_address_id', 'commercial_contact', 'delivery_contact', 'created_at', 'last_updated'], [1, 'Fahey and Sons', 15, 'Micheal Toy', 'Mrs. Lucy Runolfsdottir', datetime.datetime(2022, 11, 3, 14, 20, 51, 563000), datetime.datetime(2022, 11, 3, 14, 20, 51, 563000)], [2, 'Leannon, Predovic and Morar', 28, 'Melba Sanford', 'Jean Hane III', datetime.datetime(2022, 11, 3, 14, 20, 51, 563000), datetime.datetime(2022, 11, 3, 14, 20, 51, 563000)], [3, 'Armstrong Inc', 2, 'Jane Wiza', 'Myra Kovacek', datetime.datetime(2022, 11, 3, 14, 20, 51, 563000), datetime.datetime(2022, 11, 3, 14, 20, 51, 563000)]], 'currency': [['currency_id', 'currency_code', 'created_at', 'last_updated'], [1, 'GBP', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [2, 'USD', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [3, 'EUR', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)]], 'department': [['department_id', 'department_name', 'location', 'manager', 'created_at', 'last_updated'], [1, 'Sales', 'Manchester', 'Richard Roma', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [2, 'Purchasing', 'Manchester', 'Naomi Lapaglia', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [3, 'Production', 'Leeds', 'Chester Ming', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)]], 'full_department_table': [[1, 'Sales', 'Manchester', 'Richard Roma', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [2, 'Purchasing', 'Manchester', 'Naomi Lapaglia', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [3, 'Production', 'Leeds', 'Chester Ming', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [4, 'Dispatch', 'Leds', 'Mark Hanna', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [5, 'Finance', 'Manchester', 'Jordan Belfort', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [6, 'Facilities', 'Manchester', 'Shelley Levene', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [7, 'Communications', 'Leeds', 'Ann Blake', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [8, 'HR', 'Leeds', 'James Link', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)]], 'design': [['design_id', 'created_at', 'design_name', 'file_location', 'file_name', 'last_updated'], [1, datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), 'Wooden', '/home/user/dir', 'wooden-20201128-jdvi.json', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [8, datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), 'Wooden', '/usr', 'wooden-20220717-npgz.json', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [9, datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), 'Concrete', '/etc', 'concrete-20211012-auw9.json', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)]], 'payment': [['payment_id', 'created_at', 'last_updated', 'transaction_id', 'counterparty_id', 'payment_amount', 'currency_id', 'payment_type_id', 'paid', 'payment_date', 'company_ac_number', 'counterparty_ac_number'], [2, datetime.datetime(2022, 11, 3, 14, 20, 52, 187000), datetime.datetime(2022, 11, 3, 14, 20, 52, 187000), 2, 15, Decimal('552548.62'), 2, 3, False, '2022-11-04', 67305075, 31622269], [3, datetime.datetime(2022, 11, 3, 14, 20, 52, 186000), datetime.datetime(2022, 11, 3, 14, 20, 52, 186000), 3, 18, Decimal('205952.22'), 3, 1, False, '2022-11-03', 81718079, 47839086], [5, datetime.datetime(2022, 11, 3, 14, 20, 52, 187000), datetime.datetime(2022, 11, 3, 14, 20, 52, 187000), 5, 17, Decimal('57067.20'), 2, 3, False, '2022-11-06', 66213052, 91659548]], 'transaction': [['transaction_id', 'transaction_type', 'sales_order_id', 'purchase_order_id', 'created_at', 'last_updated'], [1, 'PURCHASE', None, 2, datetime.datetime(2022, 11, 3, 14, 20, 52, 186000), datetime.datetime(2022, 11, 3, 14, 20, 52, 186000)], [2, 'PURCHASE', None, 3, datetime.datetime(2022, 11, 3, 14, 20, 52, 187000), datetime.datetime(2022, 11, 3, 14, 20, 52, 187000)], [3, 'SALE', 1, None, datetime.datetime(2022, 11, 3, 14, 20, 52, 186000), datetime.datetime(2022, 11, 3, 14, 20, 52, 186000)]], 'staff': [['staff_id', 'first_name', 'last_name', 'department_id', 'email_address', 'created_at', 'last_updated'], [1, 'Jeremie', 'Franey', 2, 'jeremie.franey@terrifictotes.com', datetime.datetime(2022, 11, 3, 14, 20, 51, 563000), datetime.datetime(2022, 11, 3, 14, 20, 51, 563000)], [2, 'Deron', 'Beier', 6, 'deron.beier@terrifictotes.com', datetime.datetime(2022, 11, 3, 14, 20, 51, 563000), datetime.datetime(2022, 11, 3, 14, 20, 51, 563000)], [3, 'Jeanette', 'Erdman', 6, 'jeanette.erdman@terrifictotes.com', datetime.datetime(2022, 11, 3, 14, 20, 51, 563000), datetime.datetime(2022, 11, 3, 14, 20, 51, 563000)]], 'sales_order': [['sales_order_id', 'created_at', 'last_updated', 'design_id', 'staff_id', 'counterparty_id', 'units_sold', 'unit_price', 'currency_id', 'agreed_delivery_date', 'agreed_payment_date', 'agreed_delivery_location_id'], [1, datetime.datetime(2022, 11, 3, 14, 20, 52, 186000), datetime.datetime(2022, 11, 3, 14, 20, 52, 186000), 9, 16, 18, 84754, Decimal('2.43'), 3, '2022-11-10', '2022-11-03', 4], [2, datetime.datetime(2022, 11, 3, 14, 20, 52, 186000), datetime.datetime(2022, 11, 3, 14, 20, 52, 186000), 3, 19, 8, 42972, Decimal('3.94'), 2, '2022-11-07', '2022-11-08', 8], [3, datetime.datetime(2022, 11, 3, 14, 20, 52, 188000), datetime.datetime(2022, 11, 3, 14, 20, 52, 188000), 4, 10, 4, 65839, Decimal('2.91'), 3, '2022-11-06', '2022-11-07', 19]], 'address': [['address_id', 'address_line_1', 'address_line_2', 'district', 'city', 'postal_code', 'country', 'phone', 'created_at', 'last_updated'], [1, '6826 Herzog Via', None, 'Avon', 'New Patienceburgh', '28441', 'Turkey', '1803 637401', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [2, '179 Alexie Cliffs', None, None, 'Aliso Viejo', '99305-7380', 'San Marino', '9621 880720', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [3, '148 Sincere Fort', None, None, 'Lake Charles', '89360', 'Samoa', '0730 783349', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)]], 'full_address_table': [[1, '6826 Herzog Via', None, 'Avon', 'New Patienceburgh', '28441', 'Turkey', '1803 637401', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [2, '179 Alexie Cliffs', None, None, 'Aliso Viejo', '99305-7380', 'San Marino', '9621 880720', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [3, '148 Sincere Fort', None, None, 'Lake Charles', '89360', 'Samoa', '0730 783349', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [4, '6102 Rogahn Skyway', None, 'Bedfordshire', 'Olsonside', '47518', 'Republic of Korea', '1239 706295', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [5, '34177 Upton Track', None, None, 'Fort Shadburgh', '55993-8850', 'Bosnia and Herzegovina', '0081 009772', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [6, '846 Kailey Island', None, None, 'Kendraburgh', '08841', 'Zimbabwe', '0447 798320', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [7, '75653 Ernestine Ways', None, 'Buckinghamshire', 'North Deshaun', '02813', 'Faroe Islands', '1373 796260', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [8, '0579 Durgan Common', None, None, 'Suffolk', '56693-0660', 'United Kingdom', '8935 157571', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [9, '644 Edward Garden', None, 'Borders', 'New Tyra', '30825-5672', 'Australia', '0768 748652', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [10, '49967 Kaylah Flat', 'Tremaine Circles', 'Bedfordshire', 'Beaulahcester', '89470', "Democratic People's Republic of Korea", '4949 998070', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [11, '249 Bernier Mission', None, 'Buckinghamshire', 'Corpus Christi', '85111-9300', 'Japan', '0222 525870', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [12, '6461 Ernesto Expressway', None, 'Berkshire', 'Pricetown', '37167-0340', 'Tajikistan', '4757 757948', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [13, '80828 Arch Dale', 'Torphy Turnpike', None, 'Shanahanview', '60728-5019', 'Bouvet Island (Bouvetoya)', '8806 209655', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [14, '84824 Bryce Common', 'Grady Turnpike', None, 'Maggiofurt', '50899-1522', 'Iraq', '3316 955887', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [15, '605 Haskell Trafficway', 'Axel Freeway', None, 'East Bobbie', '88253-4257', 'Heard Island and McDonald Islands', '9687 937447', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [16, '511 Orin Extension', 'Cielo Radial', 'Buckinghamshire', 'South Wyatt', '04524-5341', 'Iceland', '2372 180716', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [17, '962 Koch Drives', None, None, 'Hackensack', '95316-4738', 'Indonesia', '5507 549583', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [18, '58805 Sibyl Cliff', 'Leuschke Glens', 'Bedfordshire', 'Lake Arne', '63808', 'Kiribati', '0168 407254', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [19, '0283 Cole Corner', 'Izabella Ways', 'Buckinghamshire', 'West Briellecester', '01138', 'Sierra Leone', '1753 158314', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [20, '22073 Klein Landing', None, None, 'Pueblo', '91445', 'Republic of Korea', '4003 678621', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [21, '389 Georgette Ridge', None, 'Cambridgeshire', 'Fresno', '91510-3655', 'Bolivia', '8697 474676', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [22, '364 Goodwin Streets', None, None, 'Sayreville', '85544-4254', 'Svalbard & Jan Mayen Islands', '0847 468066', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [23, '822 Providenci Spring', None, 'Berkshire', 'Derekport', '25541', 'Papua New Guinea', '4111 801405', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [24, '8434 Daren Freeway', None, None, 'New Torrance', '17110', 'Antigua and Barbuda', '5582 055380', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [25, '253 Ullrich Inlet', 'Macey Wall', 'Borders', 'East Arvel', '35397-9952', 'Sudan', '0021 366201', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [26, '522 Pacocha Branch', None, 'Bedfordshire', 'Napa', '77211-4519', 'American Samoa', '5794 359212', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [27, '7212 Breitenberg View', 'Nora Bridge', 'Buckinghamshire', 'Oakland Park', '77499', 'Guam', '2949 665163', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [28, '079 Horacio Landing', None, None, 'Utica', '93045', 'Austria', '7772 084705', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [29, '37736 Heathcote Lock', 'Noemy Pines', None, 'Bartellview', '42400-5199', 'Congo', '1684 702261', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [30, '0336 Ruthe Heights', None, 'Buckinghamshire', 'Lake Myrlfurt', '94545-4284', 'Falkland Islands (Malvinas)', '1083 286132', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)]], 'purchase_order': [['purchase_order_id', 'created_at', 'last_updated', 'staff_id', 'counterparty_id', 'item_code', 'item_quantity', 'item_unit_price', 'currency_id', 'agreed_delivery_date', 'agreed_payment_date', 'agreed_delivery_location_id'], [1, datetime.datetime(2022, 11, 3, 14, 20, 52, 187000), datetime.datetime(2022, 11, 3, 14, 20, 52, 187000), 12, 11, 'ZDOI5EA', 371, Decimal('361.39'), 2, '2022-11-09', '2022-11-07', 6], [2, datetime.datetime(2022, 11, 3, 14, 20, 52, 186000), datetime.datetime(2022, 11, 3, 14, 20, 52, 186000), 20, 17, 'QLZLEXR', 286, Decimal('199.04'), 2, '2022-11-04', '2022-11-07', 8], [3, datetime.datetime(2022, 11, 3, 14, 20, 52, 187000), datetime.datetime(2022, 11, 3, 14, 20, 52, 187000), 12, 15, 'AN3D85L', 839, Decimal('658.58'), 2, '2022-11-05', '2022-11-04', 16]], 'payment_type': [['payment_type_id', 'payment_type_name', 'created_at', 'last_updated'], [1, 'SALES_RECEIPT', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [2, 'SALES_REFUND', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)], [3, 'PURCHASE_PAYMENT', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)]]}

single_test_data = {'counterparty': [['counterparty_id', 'counterparty_legal_name', 'legal_address_id', 'commercial_contact', 'delivery_contact', 'created_at', 'last_updated'], [1, 'Fahey and Sons', 15, 'Micheal Toy', 'Mrs. Lucy Runolfsdottir', datetime.datetime(2022, 11, 3, 14, 20, 51, 563000), datetime.datetime(2022, 11, 3, 14, 20, 51, 563000)], [2, 'Leannon, Predovic and Morar', 28, 'Melba Sanford', 'Jean Hane III', datetime.datetime(2022, 11, 3, 14, 20, 51, 563000), datetime.datetime(2022, 11, 3, 14, 20, 51, 563000)], [3, 'Armstrong Inc', 2, 'Jane Wiza', 'Myra Kovacek', datetime.datetime(2022, 11, 3, 14, 20, 51, 563000), datetime.datetime(2022, 11, 3, 14, 20, 51, 563000)]]}