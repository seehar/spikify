import hashlib
import json


class MD5Util:
    """
    md5 工具类
    """

    @staticmethod
    def from_str(string: str) -> str:
        """
        生成给定字符串的MD5哈希值

        :param string: 原始字符串
        :return: 字符串的MD5哈希值
        """
        hash_object = hashlib.md5(string.encode())
        return hash_object.hexdigest()

    @staticmethod
    def from_dict(dict_data: dict) -> str:
        """
        生成给定字典的MD5哈希值

        :param dict_data: 字典类型数据
        :return: MD5哈希值
        """
        if not dict_data:
            return MD5Util.from_str("")

        dict_str = json.dumps(dict_data, sort_keys=True)
        return MD5Util.from_str(dict_str)
