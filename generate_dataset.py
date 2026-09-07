"""
欧洲五大联赛攻防与比分样本数据集生成脚本
数据来源：球小策数据库 (https://www.qiuxiaoce.com)
"""

import csv
import os
import sys

# 切换并引入工程上级 core
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../.."))
sys.path.append(project_root)

from core.db import engine
from sqlalchemy import text


def export_matches_csv(output_path: str, limit: int = 1000):
    query = f"""
        SELECT 
            f.fixture_id,
            f.date,
            f.season_year,
            l.name as league_name,
            ht.name as home_team,
            at.name as away_team,
            f.home_goals,
            f.away_goals,
            f.halftime_home,
            f.halftime_away,
            f.status_short,
            f.referee
        FROM abv2_fixtures f
        JOIN abv2_leagues l ON f.league_id = l.league_id
        JOIN abv2_teams ht ON f.home_team_id = ht.team_id
        JOIN abv2_teams at ON f.away_team_id = at.team_id
        WHERE f.league_id IN (39, 140, 135, 78, 61)
          AND f.status_short = 'FT'
          AND f.home_goals IS NOT NULL
        ORDER BY f.date DESC
        LIMIT {limit}
    """

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with engine.connect() as conn:
        rows = conn.execute(text(query)).fetchall()
        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "fixture_id", "date", "season", "league",
                "home_team", "away_team", "fulltime_home_goals", "fulltime_away_goals",
                "halftime_home_goals", "halftime_away_goals", "result", "referee", "data_source"
            ])
            for r in rows:
                fid, dt, season, lg, h_team, a_team, h_goals, a_goals, ht_h, ht_a, status, referee = r
                res = "H" if h_goals > a_goals else ("A" if h_goals < a_goals else "D")
                writer.writerow([
                    fid, dt, season, lg, h_team, a_team, h_goals, a_goals,
                    ht_h if ht_h is not None else "",
                    ht_a if ht_a is not None else "",
                    res, referee or "", "https://www.qiuxiaoce.com"
                ])
    print(f"✅ 成功导出 {len(rows)} 条比赛记录至 {output_path}")


if __name__ == "__main__":
    out_file = os.path.join(current_dir, "data", "european_top5_matches_sample.csv")
    export_matches_csv(out_file, limit=500)
