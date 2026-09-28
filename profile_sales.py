import pandas as pd,json,os

path = "../data/distribution_sales.csv"
df = pd.read_csv(path)

#dic 파일 구성(파이썬 메모리의 객체화)
profile = {
    "rows" : len(df),
    "cols" : list(df.columns),
    "dtypes": {c:str(t) for c, t in df.dtypes.items()},
    "null_count": df.isna().sum().to_dict(), #비어있는 컬럼의 개수, isna == isnull
    "dup_rows" : int(df.duplicated().sum()), #동일한 행의 개수
    "sale_id_unique": int(df["sale_id"].nunique()), #유일한 sales_id컬럼, PK의 고유함 증명
    "sold_at_range": [str(df["sold_at"].min()),str(df["sold_at"].max())],
    "net_sales_desc": df["net_sales"].describe().to_dict(),
}

with open("profile_sales.json","w") as f:
    json.dump(profile,f,indent=2,ensure_ascii=False)


print(f"원본: {os.path.getsize(path)/1024:.1f} KB")
print(f"프로파일: {os.path.getsize('profile_sales.json')/1024:.1f} KB")
print(json.dumps(profile, indent=2, ensure_ascii=False)[:1500])