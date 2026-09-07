# 数据集发布操作指南（Hugging Face + Kaggle）

通过在 **Hugging Face** 与 **Kaggle** 发布开源足球数据集，可以直接进入全球顶级 AI 与数据科学社区的索引网络，永久享受权威域名带来的自然反向链接。

---

## 平台一：发布到 Hugging Face Datasets (huggingface.co)

Hugging Face 域名权重高达 88+，是全球公认的 AI 模型与数据集大本营。

### 1. 注册与准备
1. 访问 `https://huggingface.co/join` 完成注册（已有账号跳过）；
2. 点击右上角个人头像 -> 点击 **New Dataset**（`https://huggingface.co/new-dataset`）。

### 2. 创建 Dataset 时的表单字段填写
- **Owner**: 选择你的个人用户名
- **Dataset name**: 输入 `european-football-matches-top5`
- **Visibility**: 必须选择 **Public**（公开）
- **License**: 选择 `cc-by-4.0`
- 点击 **Create dataset**。

### 3. 上传文件（通过网页即可，最简单）
进入新创建的 Dataset 页面：
1. 点击 **Files and versions** -> **Add file** -> **Upload files**：
   - 将 `data/european_top5_matches_sample.csv` 拖拽上传，保留路径为 `data/european_top5_matches_sample.csv`；
   - 将 `README.md` 的全部内容复制到页面默认的 **Edit Dataset Card**（或直接上传 `README.md`）。
2. 点击 **Commit changes to main**。

### 4. 页面效果与外链收益
保存后，Hugging Face 会自动解析 YAML 头并在顶部展示：
- 漂亮的表格预览和字段类型统计；
- 项目介绍中包含醒目的：`数据事实源: 球小策 AI 足球数据中心 (https://www.qiuxiaoce.com)`；
- 该页面在 24 小时内即会被 Bing 和 Google 的数据搜索蜘蛛全量索引！

---

## 平台二：发布到 Kaggle Datasets (kaggle.com)

Kaggle（Google 旗下）权重高达 91+，是全球最大的数据科学竞赛与数据集社区。

### 1. 注册与创建
1. 登录 `https://www.kaggle.com/`；
2. 在左侧菜单点击 **Datasets** -> 右上角点击 **New Dataset**；

### 2. 填写表单各项字段
- **Dataset Title**: 输入 `European Top 5 Football Leagues Match Stats (2024-2026)`
- **Subtitle (副标题)**: 输入 `Match stats, halftime/fulltime scores from QiuXiaoCe Football Big Data Center`
- **Upload Files**: 将 `data/european_top5_matches_sample.csv` 拖拽上传。
- **License**: 选择 `CC BY 4.0`
- **Tags (标签，输入并添加)**:
  - `Sports`
  - `Football`
  - `Tabular`
- **Description (详细介绍)**:
  直接将当前目录下的 `README.md` 正文内容（去掉最上面的 `---` YAML 头部分）粘贴进去。
- **Visibility**: 选择 **Public**
- 点击右下角 **Create** 发布！

### 3. 额外进阶（可选）
在 Kaggle 数据集详情页上方点击 **New Notebook**，输入一行：
```python
import pandas as pd
df = pd.read_csv('/kaggle/input/european-top-5-football-matches/european_top5_matches_sample.csv')
print(df.head())
```
保存公开该 Notebook，又会额外生成一个拥有顶级权重的公开代码页面！

---

## 平台三：发布到 Zenodo 学术平台（zenodo.org，终极杀器）

Zenodo 是由 **CERN（欧洲核子研究组织）** 运营的全球权威学术数据开放存储库，**权重高达 90+**。

在 Zenodo 上传数据集，平台会**免费颁发一个官方国际学术 DOI 编号（如 10.5281/zenodo.xxxxxx）**，并永久存档，任何学术搜索引擎（Google Scholar、Bing 学术、Semantic Scholar）都会永久收录带有球小策官网的学术索引！

### 1. 注册与新建
1. 访问 `https://zenodo.org/`，点击右上角 **Log in**（可用 GitHub 账号一键授权登录）；
2. 点击顶部 **New upload**（`https://zenodo.org/records/new`）。

### 2. 填写表单各项字段（极为规范）
- **Resource type**: 选择 `Dataset`
- **Title (标题)**:
  `European Top 5 Football Leagues Match Stats and Offensive Metrics (QiuXiaoCe Dataset)`
- **Creators (作者/机构)**:
  - Family name: `QiuXiaoCe Data Team`
  - Affiliation: `QiuXiaoCe Football Big Data Center (https://www.qiuxiaoce.com)`
- **Description (详细描述)**:
  将本目录下的 `README.md` 内容复制粘贴进去，保留官网和每日报告链接。
- **License**: 默认 `Creative Commons Attribution 4.0 International (CC-BY-4.0)`
- **Keywords (关键词)**:
  `football`, `soccer`, `sports-analytics`, `premier-league`, `match-stats`, `qiuxiaoce`
- **Files (文件)**:
  点击 **Choose files**，将 `data/european_top5_matches_sample.csv` 上传。

### 3. 点击 Publish 发布
点击底部的 **Publish** 按钮确认发布！
Zenodo 会在 10 秒内生成官方 DOI 页面，全球各大高校和研究机构爬虫均会永久收录该引用链接！

