# 简介及安装

> `Spikify` 是一个旨在帮助开发者快速提升开发效率的 `Python` 工具包。其名称来源于“Spike”，意味着在短时间内集中特性，迅速解决问题。`Spikify` 提供了一系列实用工具和函数，帮助开发者在日常开发中减少重复劳动，专注于核心逻辑的实现。

## 安装

=== "pip"
    ```bash
    # 安装全部功能
    pip install spikify[all]

    # 安装单模块功能
    pip install spikify[log]

    # 安装多模块功能
    pip install spikify[log,...]
    ```

=== "poetry"
    ```bash
    # 安装全部功能
    poetry add spikify[all]

    # 安装单模块功能
    poetry add spikify[log]

    # 安装多模块功能
    poetry add spikify[log,...]
    ```

## 主要特性

* 实用工具函数：提供了一系列常用的工具函数，如数据处理、字符串操作、文件读写等。
* 性能优化：内置了性能分析工具和装饰器，帮助开发者快速定位性能瓶颈。
* 代码简化：通过提供简洁的 `API`，减少样板代码，提升开发效率。
* 模块化设计：每个功能模块都经过精心设计，易于扩展和定制。
