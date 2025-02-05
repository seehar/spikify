import string

import pytest

from spikify.util.string_util import StringUtil


class TestStringUtil:
    @pytest.mark.parametrize("length", [0, 1, 5, 10, 20])
    def test_create_random_alphanumeric(self, length: int):
        """
        测试生成指定长度的随机字母数字字符串
        """
        result = StringUtil.create_random_alphanumeric(length)
        assert len(result) == length, f"Expected length {length}, but got {len(result)}"
        assert all(
            c in string.ascii_letters + string.digits for c in result
        ), "String contains invalid characters"

    @pytest.mark.parametrize("length", [0, 1, 5, 10, 20])
    def test_create_random_letters(self, length: int):
        """
        测试生成指定长度的随机字母字符串（仅包含大小写字母）
        """
        result = StringUtil.create_random_letters(length)
        assert len(result) == length, f"Expected length {length}, but got {len(result)}"
        assert all(
            c in string.ascii_letters for c in result
        ), "String contains invalid characters"

    @pytest.mark.parametrize("length", [0, 1, 5, 10, 20])
    def test_create_random_lowercase_letters(self, length: int):
        """
        测试生成指定长度的随机小写字母字符串
        """
        result = StringUtil.create_random_lowercase_letters(length)
        assert len(result) == length, f"Expected length {length}, but got {len(result)}"
        assert all(
            c in string.ascii_lowercase for c in result
        ), "String contains invalid characters"

    @pytest.mark.parametrize("length", [0, 1, 5, 10, 20])
    def test_create_random_uppercase_letters(self, length: int):
        """
        测试生成指定长度的随机大写字母字符串
        """
        result = StringUtil.create_random_uppercase_letters(length)
        assert len(result) == length, f"Expected length {length}, but got {len(result)}"
        assert all(
            c in string.ascii_uppercase for c in result
        ), "String contains invalid characters"
