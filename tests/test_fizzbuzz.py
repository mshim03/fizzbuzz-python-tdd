import pytest

from fizzbuzz.fizzbuzz import FizzBuzz

# def test_fail():
#     assert pytest.fail("これは失敗するはず")


@pytest.fixture(scope="module")
def fizzbuzz():
    # 準備
    return FizzBuzz()


class TestConvertMethodToStr:
    class TestReturnFizzMultiple3:
        def test_convert_3(self, fizzbuzz):
            # 実行 & 検証
            assert fizzbuzz.convert(3) == "Fizz"

        def test_convert_9(self, fizzbuzz):
            # 実行 & 検証
            assert fizzbuzz.convert(9) == "Fizz"

    class TestReturnBuzzMultiple5:
        def test_convert_5(self, fizzbuzz):
            # 実行 & 検証
            assert fizzbuzz.convert(5) == "Buzz"

        def test_convert_10(self, fizzbuzz):
            # 実行 & 検証
            assert fizzbuzz.convert(10) == "Buzz"

    class TestReturnSameStrOther:
        def test_convert_one(self, fizzbuzz):
            # 実行 & 検証
            assert fizzbuzz.convert(1) == "1"

        # def test_convert_two(self, fizzbuzz):
        #     # 実行 & 検証
        #     assert fizzbuzz.convert(2) == "2"

    class TestReturnFizzBuzzMultiple15:
        def test_convert_15(self, fizzbuzz):
            # 実行 & 検証
            assert fizzbuzz.convert(15) == "FizzBuzz"

        def test_convert_30(self, fizzbuzz):
            # 実行 & 検証
            assert fizzbuzz.convert(30) == "FizzBuzz"


class TestPrintedStr:
    def test_PrintedFizzBuzz(self, fizzbuzz, capsys):
        fizzbuzz.print_fizzbuzz(15)
        captured_pritned = capsys.readouterr()
        assert captured_pritned.out == f"{fizzbuzz.convert(15)}\n"

    def test_PrintedFizz(self, fizzbuzz, capsys):
        fizzbuzz.print_fizzbuzz(3)
        captured_pritned = capsys.readouterr()
        assert captured_pritned.out == f"{fizzbuzz.convert(3)}\n"

    def test_PrintedBuzz(self, fizzbuzz, capsys):
        fizzbuzz.print_fizzbuzz(5)
        captured_pritned = capsys.readouterr()
        assert captured_pritned.out == f"{fizzbuzz.convert(5)}\n"


class TestPrintRange:
    def test_PrintedFizzBuzzRange(self, fizzbuzz, mocker):
        m = mocker.patch("fizzbuzz.fizzbuzz.FizzBuzz.print_fizzbuzz")
        fizzbuzz.print_fizzbuzz_range(5)
        m.assert_has_calls(
            [
                mocker.call(1),
                mocker.call(2),
                mocker.call(3),
                mocker.call(4),
                mocker.call(5),
             ]
        )
        # m.assert_has_calls(
        #     [mocker.call(i) for i in range(1, 101)]
        # )
