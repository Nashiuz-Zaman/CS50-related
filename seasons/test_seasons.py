from seasons import validate_date

def test_validate_date():
    assert validate_date('1991-08-10') == ['1991', '08', '10']
    assert validate_date('2000-08-10') == ['2000', '08', '10']
    assert validate_date('1991-8-10') == None
