import random
import string


class StringUtil:
    """
    字符串工具类
    """

    @staticmethod
    def create_random_alphanumeric(length: int) -> str:
        """
        生成指定长度的随机字母数字字符串

        :param length: 需要生成字符串的长度
        :return: 生成的字符串
        """
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def create_random_letters(length: int) -> str:
        """
        生成指定长度的随机字母字符串（仅包含大小写字母）

        :param length: 需要生成字符串的长度
        :return: 生成的字符串
        """
        return "".join(random.choices(string.ascii_letters, k=length))

    @staticmethod
    def create_random_lowercase_letters(length: int) -> str:
        """
        生成指定长度的随机小写字母字符串

        :param length: 需要生成字符串的长度
        :return: 生成的字符串
        """
        return "".join(random.choices(string.ascii_lowercase, k=length))

    @staticmethod
    def create_random_uppercase_letters(length: int) -> str:
        """
        生成指定长度的随机大写字母字符串

        :param length: 需要生成字符串的长度
        :return: 生成的字符串
        """
        return "".join(random.choices(string.ascii_uppercase, k=length))
