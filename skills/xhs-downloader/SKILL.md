---
name: xhs-downloader
description: 小红书笔记下载器。当用户贴入小红书链接并要求下载时，默认下载到当前工作目录下的xhs_downloader文件夹，并建立CSV记录。支持单个链接下载和批量下载（从urls.txt、markdown等文件读取URL），自动清洗URL数据。
---

# 小红书下载器 Skill

## 功能说明

本Skill用于下载小红书笔记内容，支持：
- 单个链接下载
- 批量下载（从文件读取URL列表）
- 自动URL清洗
- CSV记录管理
- 按用户名分类文件夹

## 触发条件

当用户出现以下情况时使用此Skill：
- 贴入小红书链接并要求下载
- 提到"小红书下载"、"xhs下载"等关键词
- 指定urls.txt或其他包含URL的文件进行批量下载
- 要求下载小红书笔记内容

## 安全约束

- 仅下载用户明确要求的内容
- 不读取或修改用户未授权的文件
- 下载目录限制在指定的xhs_downloader文件夹内
- 对于批量下载前需确认用户意图

## 工作流程

### 1. 分析用户需求
- 识别用户是单个链接还是批量下载
- 检查用户是否提及不需要Cookies
- 确定下载路径

### 2. 准备环境
- 确保下载路径：当前工作目录/xhs_downloader
- 确保目标目录存在
- xhs_downloader.py已经包含在skill/scripts目录中，不需要额外复制

### 3. 单个链接下载
- 用户提供单个小红书URL
- 询问是否需要Cookies（如用户未明确说不需要）
- 执行下载

### 4. 批量下载
- 从指定文件（urls.txt、markdown等）读取URL
- URL清洗：去除空格、空行、错误换行
- 提取有效的小红书URL
- 执行批量下载

### 5. 记录管理
- 自动生成CSV记录
- 记录下载历史

## URL清洗规则

从文件读取URL时执行以下清洗：
1. 去除每行首尾空格
2. 过滤空行
3. 提取包含`xiaohongshu.com`或`xhslink.com`的行
4. 去除Markdown格式（如`[链接](url)`只保留url）
5. 合并被错误换行的URL

## 使用示例

### 单个下载
&gt; 用户：下载这个小红书链接 https://www.xiaohongshu.com/explore/...

### 批量下载
&gt; 用户：用urls.txt批量下载
&gt; 用户：下载这个markdown文件里的小红书链接

## 详细操作指南

### 步骤1：检查用户输入
- 分析用户消息中是否包含小红书URL
- 检查是否指定了文件路径（urls.txt、.md等）
- 注意用户是否明确说"不需要cookies"
- 注意用户是否明确说"不按用户名分类"，**默认按用户名分类**

### 步骤2：准备下载脚本
- xhs_downloader.py已经包含在skill/scripts目录中，直接使用
- 使用skill中的完整功能，不需要额外复制

### 步骤3：创建下载目录
- 默认下载目录：当前工作目录/xhs_downloader
- 使用os.makedirs确保目录存在

### 步骤4：分类设置
- 默认：按用户名分类文件夹（username_classification_enabled=True）
- 只有用户明确说"不按用户名分类"时，才设置为False

### 步骤5：询问Cookies
- 如果用户没有明确说"不需要cookies"，则询问："是否需要提供Cookies用于登录态下载？(y/n)"
- 如果用户提供Cookies，保存供后续使用

### 步骤6：处理单个URL
- 提取用户消息中的小红书URL
- 创建临时Python脚本来调用XHSDownloader类
- 设置download_dir为当前工作目录/xhs_downloader
- 默认按用户名分类，除非用户明确要求不分类
- 执行下载

### 步骤7：处理批量下载
- 读取用户指定的文件内容
- 使用scripts/url_cleaner.py清洗URL
- 提取有效的小红书URL列表
- 默认按用户名分类，除非用户明确要求不分类
- 创建批量下载脚本，依次下载所有URL

### 步骤8：反馈结果
- 告知用户下载完成
- 说明下载位置
- 显示CSV记录位置

## 脚本调用方式

### 单个URL下载
使用 `scripts/single_downloader.py`:

```bash
python scripts/single_downloader.py --url "https://www.xiaohongshu.com/explore/..." --dir "xhs_downloader"
```

可选参数:
- `--cookies "cookie字符串"` - 提供Cookies用于登录态下载
- `--no-classify` - 不按用户名分类文件夹

### 批量下载
使用 `scripts/batch_downloader.py`:

```bash
# 从文件读取URL
python scripts/batch_downloader.py --file "urls.txt" --dir "xhs_downloader"

# 直接提供URL列表
python scripts/batch_downloader.py --urls "url1" "url2" --dir "xhs_downloader"
```

可选参数:
- `--cookies "cookie字符串"` - 提供Cookies用于登录态下载
- `--no-classify` - 不按用户名分类文件夹

### URL清洗
使用 `scripts/url_cleaner.py` 从文件中提取并清洗URL:

```bash
python scripts/url_cleaner.py "urls.txt"
```

