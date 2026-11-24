# 球小策五大联赛与主流赛事历史赛果及 xG 开放数据集

[![DOI](https://img.shields.io/badge/DOI-10.6084%2Fm9.figshare.33583846-blue)](https://doi.org/10.6084/m9.figshare.33583846)
[![Website](https://img.shields.io/badge/Official-QiuXiaoCe.com-10b981)](https://www.qiuxiaoce.com/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

> *Compiled from publicly available sports statistics and processed by QiuXiaoCe Data Engine ([https://www.qiuxiaoce.com](https://www.qiuxiaoce.com/)).*

本数据集收录欧洲五大联赛、欧冠欧联及主流职业联赛的**已完赛客观历史赛果与高阶技术统计**（含 `expected_goals (xG)`、射门、射正、角球与控球率），每周自动脱敏更新。

- **当前记录规模**：**4,000 场**已完赛官方比赛（其中 **3,799 场**含完整 xG 统计）
- **最近更新时间**：2026-11-24 15:30 UTC
- **学术引用 DOI**：[`10.6084/m9.figshare.33583846`](https://doi.org/10.6084/m9.figshare.33583846)

## 核心文件

- `data/european_top5_matches_sample.csv`（标准 UTF-8 CSV，可直接导入 Pandas / Excel / SQL）
- `data/european_football_matches.parquet`（Parquet 列式存储，适合 Polars / DuckDB）

## 官方服务入口

- **球小策官网**：https://www.qiuxiaoce.com/
- **每日赛事报告速览**：https://www.qiuxiaoce.com/mei-ri-bao-gao-su-lan/
- **创作者开放 API 控制台**：https://www.qiuxiaoce.com/data-account/
