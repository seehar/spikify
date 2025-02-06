### StringUtil

#### 简介

`StringUtil` 是一个用于生成随机字符串的工具类，提供了多种方法来生成不同类型的随机字符串。它使用 Python 内置的 `random` 和
`string` 模块来实现这些功能。

#### 安装依赖

`StringUtil` 依赖于 Python 标准库中的 `random` 和 `string` 模块，因此无需额外安装依赖包。

#### 使用示例

以下是一些简单的使用示例，展示了如何使用 `StringUtil` 类生成不同类型的随机字符串：

```python
from spikify.util.string_util import StringUtil

# 生成指定长度的随机字母数字字符串
random_alphanumeric = StringUtil.create_random_alphanumeric(10)
print(f"随机字母数字字符串: {random_alphanumeric}")

# 生成指定长度的随机字母字符串（仅包含大小写字母）
random_letters = StringUtil.create_random_letters(8)
print(f"随机字母字符串: {random_letters}")

# 生成指定长度的随机小写字母字符串
random_lowercase = StringUtil.create_random_lowercase_letters(6)
print(f"随机小写字母字符串: {random_lowercase}")

# 生成指定长度的随机大写字母字符串
random_uppercase = StringUtil.create_random_uppercase_letters(4)
print(f"随机大写字母字符串: {random_uppercase}")
```

#### 方法说明

##### `create_random_alphanumeric`

- **描述**: 生成指定长度的随机字母数字字符串。
- **参数**:

| 参数名      | 类型    | 默认值 | 描述         |
|----------|-------|-----|------------|
| `length` | `int` | 必填  | 需要生成字符串的长度 |

- **返回值**: 包含大小写字母和数字的随机字符串。

##### `create_random_letters`

- **描述**: 生成指定长度的随机字母字符串（仅包含大小写字母）。
- **参数**:

| 参数名      | 类型    | 默认值 | 描述         |
|----------|-------|-----|------------|
| `length` | `int` | 必填  | 需要生成字符串的长度 |

- **返回值**: 包含大小写字母的随机字符串。

##### `create_random_lowercase_letters`

- **描述**: 生成指定长度的随机小写字母字符串。
- **参数**:

| 参数名      | 类型    | 默认值 | 描述         |
|----------|-------|-----|------------|
| `length` | `int` | 必填  | 需要生成字符串的长度 |

- **返回值**: 包含小写字母的随机字符串。

##### `create_random_uppercase_letters`

- **描述**: 生成指定长度的随机大写字母字符串。
- **参数**:

| 参数名      | 类型    | 默认值 | 描述         |
|----------|-------|-----|------------|
| `length` | `int` | 必填  | 需要生成字符串的长度 |

- **返回值**: 包含大写字母的随机字符串。

#### 示例输出

假设你运行了上述示例代码，输出可能如下所示：

```plaintext
随机字母数字字符串: aB3dE9XzP1
随机字母字符串: ZxYwVbNm
随机小写字母字符串: abcdef
随机大写字母字符串: ABCD
```

#### 注意事项

##### 字符集

| 方法                                | 字符集描述        | 示例字符集                                  |
|-----------------------------------|--------------|----------------------------------------|
| `create_random_alphanumeric`      | 包含所有大小写字母和数字 | `string.ascii_letters + string.digits` |
| `create_random_letters`           | 包含所有大小写字母    | `string.ascii_letters`                 |
| `create_random_lowercase_letters` | 包含所有小写字母     | `string.ascii_lowercase`               |
| `create_random_uppercase_letters` | 包含所有大写字母     | `string.ascii_uppercase`               |

- **随机性**:
    - 生成的字符串是基于伪随机数生成器的，因此在不同的运行环境中可能会得到不同的结果。
    - 如果需要更强的随机性，可以考虑使用更安全的随机数生成器，例如 `secrets` 模块。

#### 扩展功能

如果你需要生成其他类型的随机字符串或自定义字符集，可以考虑扩展 `StringUtil` 类，添加新的静态方法来处理这些需求。例如，可以添加一个方法来生成包含特殊字符的随机字符串。

希望这份文档能帮助你更好地理解和使用 `StringUtil`。如果有任何问题或建议，请随时联系开发团队。