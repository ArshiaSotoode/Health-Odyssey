from project import validate_name, calculate_BMI, give_percentage


def test_validate_name():
    assert validate_name(input="Arshia ali") == False
    assert validate_name(input="Arshia") == True
    assert validate_name(input="arshia") == True
    assert validate_name(input="Ars2hia99") == False
    assert validate_name(input="Ar") == False
    assert validate_name(input="Bita") == True


def test_calculate_BMI():
    assert calculate_BMI(weight=105, height=180) == 32.41
    assert calculate_BMI(weight=82, height=179) == 25.59
    assert calculate_BMI(weight=67, height=180) == 20.68


def test_give_percentage():
    assert give_percentage(elapsed=100, total=1000) == 10
    assert give_percentage(elapsed=1, total=1000) == 0.1
    assert give_percentage(elapsed=3, total=22) == 13.64
