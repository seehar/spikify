### MD5Util

#### 简介
`MD5Util` 是一个用于生成 MD5 哈希值的工具类，支持从字符串和字典生成哈希值。它使用 Python 内置的 `hashlib` 库来计算 MD5 哈希，并且对于字典类型的数据，通过 `json.dumps` 方法将其序列化为字符串后再进行哈希计算。

#### 安装依赖
`MD5Util` 依赖于 Python 标准库中的 `hashlib` 和 `json` 模块，因此无需额外安装依赖包。

#### 使用示例
以下是一些简单的使用示例，展示了如何使用 `MD5Util` 类生成 MD5 哈希值：

```python
from spikify.util.md5_util import MD5Util

# 从字符串生成 MD5 哈希值
string = "Hello, World!"
md5_hash_str = MD5Util.from_str(string)
print(f"字符串 '{string}' 的 MD5 哈希值: {md5_hash_str}")

# 从字典生成 MD5 哈希值
dict_data = {"name": "Alice", "age": 30, "city": "New York"}
md5_hash_dict = MD5Util.from_dict(dict_data)
print(f"字典 {dict_data} 的 MD5 哈希值: {md5_hash_dict}")
```


#### 方法说明

##### `from_str`
- **描述**: 生成给定字符串的 MD5 哈希值。
- **参数**:
  - `string`: 需要生成 MD5 哈希值的原始字符串。
- **返回值**: 字符串的 MD5 哈希值（十六进制表示的字符串）。

##### `from_dict`
- **描述**: 生成给定字典的 MD5 哈希值。
- **参数**:
  - `dict_data`: 需要生成 MD5 哈希值的字典数据。
- **返回值**: 字典数据的 MD5 哈希值（十六进制表示的字符串）。
- **注意事项**: 
  - 如果字典为空，则返回空字符串的 MD5 哈希值。
  - 字典会被转换为 JSON 字符串（按键排序），以确保生成的哈希值是确定性的。

#### 示例输出
假设你运行了上述示例代码，输出可能如下所示：
```plaintext
字符串 'Hello, World!' 的 MD5 哈希值: 65a8e27d8879283831b664bd8b7f0ad4
字典 {'name': 'Alice', 'age': 30, 'city': 'New York'} 的 MD5 哈希值: 8cb4c3c6f8a7e5e4d7adeb5e8c5e4d8f
```


#### 注意事项
- **字符编码**: `from_str` 方法中，字符串会使用 UTF-8 编码后进行哈希计算。
- **字典顺序**: `from_dict` 方法中，字典会按键排序后转换为 JSON 字符串，以确保生成的哈希值是唯一的。
- **空字典处理**: 如果传入的字典为空，`from_dict` 方法会返回空字符串的 MD5 哈希值。

#### 扩展功能
如果你需要对其他类型的数据生成 MD5 哈希值，可以考虑扩展 `MD5Util` 类，添加新的静态方法来处理这些数据类型。例如，可以添加一个方法来处理列表或元组类型的输入。

希望这份文档能帮助你更好地理解和使用 `MD5Util`。如果有任何问题或建议，请随时联系开发团队。