import pytest

from spikify import MD5Util


class TestMD5Util:
    @pytest.mark.parametrize(
        "input_str, expected",
        [
            ("", "d41d8cd98f00b204e9800998ecf8427e"),  # 空字符串
            ("hello world", "5eb63bbbe01eeed093cb22bb8f5acdc3"),  # 非空字符串
        ],
    )
    def test_from_str(self, input_str, expected):
        result = MD5Util.from_str(input_str)
        assert result == expected

    @pytest.mark.parametrize(
        "input_dict, expected",
        [
            ({}, "d41d8cd98f00b204e9800998ecf8427e"),  # 空字典
            ({"key": "value"}, "88bac95f31528d13a072c05f2a1cf371"),  # 非空字典
            (
                {"foo": "bar", "hello": "world"},
                "0b061d0ec0590da36e96fe2278ce8544",
            ),  # 多个键值对
        ],
    )
    def test_from_dict(self, input_dict, expected):
        result = MD5Util.from_dict(input_dict)
        assert result == expected
