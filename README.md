# modrinth_api_wrapper

![modrinth-api-wrapper](https://socialify.git.ci/mcmod-info-mirror/modrinth-api-wrapper/image?description=1&font=Inter&forks=1&issues=1&language=1&name=1&owner=1&pattern=Overlapping+Hexagons&stargazers=1&theme=Dark)

`modrinth_api_wrapper` 是一个用于与 Modrinth API 交互的 Python 包。它提供了方便的客户端类和方法来访问 Modrinth 的各种 API 端点。

## 安装

你可以使用 `pip` 来安装这个包：

```sh
pip install modrinth_api_wrapper
```

## 使用示例

以下是一些使用 modrinth_api_wrapper 的示例代码，展示了如何与 Modrinth API 进行交互。

### 初始化客户端

首先，你需要初始化一个 Client 对象来与 API 进行交互：

```python
from modrinth_api_wrapper import Client

client = Client()
```

### 搜索项目

你可以通过关键字搜索 Modrinth 上的项目：

```python
client.search_project(query="sodium")
```

### 获取项目信息

通过项目 ID 或 slug 获取项目的详细信息：

```python
client.get_project(project_id="AANobbMI")

# 或者通过 slug 获取
client.get_project(project_id="fabric-api")
```

### 批量获取项目信息

你可以通过多个项目 ID 或 slug 批量获取项目信息：

```python
client.get_projects(ids=["AANobbMI", "P7dR8mSH"])

# 或者通过 slug 获取
client.get_projects(ids=["fabric-api", "sodium"])
```

### 获取项目的版本信息

通过项目 ID 获取项目的所有版本：

```python
client.list_project_versions(project_id="AANobbMI")
```

### 获取特定版本信息

通过版本 ID 获取特定版本的详细信息：

```python
client.get_version(version_id="3auffiOJ")
```

### 批量获取版本信息

通过多个版本 ID 批量获取版本信息：

```python
client.get_versions(version_ids=["3auffiOJ", "mnEhtGuH"])
```

### 通过哈希值获取版本信息

你可以通过文件的 SHA1 或 SHA512 哈希值获取对应的版本信息：

```python
example_sha1 = "9e1ccb3b136cff0715004bbd418c66eb38bb8383"
example_sha512 = "5677d011800d88c5259a2a3c82d0e90b5dec83a7505fc7502a68a2ff7f21834564f02764dc8813f910bd768bff253892cf54ce7d3300d6d0bbc8b592db829251"

# sha1
client.get_version_from_hash(sha1=example_sha1)

# 或者使用 SHA512
client.get_version_from_hash(sha512=example_sha512)
```

### 批量通过哈希值获取版本信息

你可以通过多个哈希值批量获取版本信息：

```python
versions = client.get_versions_from_hashes(hashes=[example_sha1], algorithm=Algorithm.SHA1)
for version in versions.values():
    print(version)

# 或者使用 SHA512
client.get_versions_from_hashes(hashes=[example_sha512], algorithm=Algorithm.SHA512)
```

### 获取最新版本信息

通过哈希值、加载器和游戏版本获取最新的版本信息：

```python
# sha1
client.get_latest_version_from_hash(example_sha1, loaders=["fabric"], game_versions=["1.16.5"])


# 或者使用 SHA512
client.get_latest_version_from_hash(sha512=example_sha512, loaders=["fabric"], game_versions=["1.16.5"])
```

### 批量获取最新版本信息

通过多个哈希值、加载器和游戏版本批量获取最新的版本信息：

```python
versions = client.get_latest_versions_from_hashes(hashes=[example_sha1], algorithm=Algorithm.SHA1, loaders=["fabric"], game_versions=["1.16.5"])


# 或者使用 SHA512

client.get_latest_versions_from_hashes(hashes=[example_sha512], algorithm=Algorithm.SHA512, loaders=["fabric"], game_versions=["1.16.5"])
```

### 获取标签信息

你可以获取 Modrinth 平台上的各种标签信息，例如类别、加载器、游戏版本等：

```python
tags = client.get_tag(tag="category")

tags = client.get_tag(tag="loader")
```

## 贡献

如果你有任何问题或建议，欢迎提交 Issue 或 Pull Request！

## 许可证

本项目采用 MIT 许可证。
