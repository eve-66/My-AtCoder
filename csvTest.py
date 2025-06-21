import csv
from collections import defaultdict

# 読み込む CSV ファイルのパス
csv_path = "PartnerBank.csv"

# 名前ごとの出現回数をカウント
name_counts = defaultdict(int)

count = 0

with open(csv_path, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row["name"]
        name_counts[name] += 1
        print(name)
        count += 1

# 重複を表示
duplicates = {name: count for name, count in name_counts.items() if count > 1}

if duplicates:
    print("⚠️ 重複している名前があります:")
    for name, count in duplicates.items():
        print(f"  - {name}: {count} 回出現")
else:
    print("✅ すべての名前はユニークです。")
    print(count)
