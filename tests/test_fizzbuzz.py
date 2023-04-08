from fizzbuzz import fizzbuzz

# def test_fail():
#     assert pytest.fail("これは失敗するはず")


def test_convert_one():
    # 実行 & 検証
    assert fizzbuzz.convert(1) == "1"


def test_convert_two():
    # 実行 & 検証
    assert fizzbuzz.convert(2) == "2"

def test_convert_three():
    # 実行 & 検証
    assert fizzbuzz.convert(3) == "Fizz"

# def test_convert_nums_to_str():
#     assert fizzbuzz
