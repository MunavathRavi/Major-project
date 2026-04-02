import pandas as pd
import sqlite3
df = pd.read_csv("/Users/munavathsai/project.ds/IMDB-Movie-Data.csv")
conn = sqlite3.connect("calend.db")
df.to_sql("movie", conn, if_exists="replace", index=False)
rsumt = pd.read_sql_query("select count(*) as total from movie",conn)
print(rsumt["total"][0])

conn.execute("""alter table movie rename column `Revenue (Millions)` to `Revenue`""")
conn.execute("""alter table movie rename column `Runtime (Minutes)` to 'Duration'""")
print("succs")
d2 =pd.read_sql_query("select avg (revenue) from movie",conn)
print(d2)
conn.execute("""UPDATE movie
SET revenue = (
    SELECT avg(revenue) FROM movie
)
WHERE revenue IS NULL
""")

print("Updated successfully")

d5 = pd.read_sql_query("""select count(*) from movie where revenue is null""",conn)
print(d5)
conn.execute("""update movie set  metascore = rating*10 where metascore is null""")
print("sucess")
conn.execute("""update movie set  revenue=revenue*91*1000000""")
conn.execute("""update movie set revenue=round(revenue)""")
print("suncss")
# r6 = pd.read_sql_query("select* from movie",conn)
# print(r6)
conn.execute("""alter table movie
add column budget bigint""")
print("sucess")
conn.execute("""update movie set budget=(
case
when rating>=8 then revenue*0.55
when rating>=6 then revenue*0.65
when rating>=4 then revenue*0.75
when rating>=3 then revenue*0.85
else revenue*0.95
end)""")
print("sucess")
# r6 = pd.read_sql_query("desc movie",conn)
# print(r6)
conn.execute("""alter table movie
add column profit bigint""")
print("sucess")
conn.execute("""update movie set profit = revenue - budget""")
print(conn)
conn.execute("""alter table movie
add column ROI bigint""")
print("sucess")

conn.execute("""update movie set roi=(profit/budget)*100""")
print("sucss")
conn.execute("""update movie 
set revenue =(
select avg_rev 
from(select avg(revenue) as avg_rev from movie) as temp)
where revenue= 0""")
print("sucss")
conn.execute("""update movie set revenue=round(revenue)""")
print("sucss")
conn.execute("""update movie set budget=(
case
when rating>=8 then revenue*0.55
when rating>=6 then revenue*0.65
when rating>=4 then revenue*0.75
when rating>=3 then revenue*0.85
else revenue*0.95
end) where budget=0""")
print("sucess")
ft = pd.read_sql_query("""select * from movie where profit=0""",conn)
print(ft)
conn.execute("""alter table movie
add column movie_status text""")
print("sucess")
# conn.execute("""alter table movie
# add column movie_status text""")

# print("success")
try:
    conn.execute("ALTER TABLE movie ADD COLUMN movie_status TEXT")
except:
    print("Column already exists")

conn.execute("""update movie set movie_status=(
case
when roi >=80 then "BlockBuster"
when roi >=50 then "Hit"
when roi >=30 then "Average"
when roi >=15 then "Flop"
else "Disaster"
end)""")
print("sucss")
conn.execute("""update movie set title="The Host(2006)" where `rank`=633""")
print("sucss")
conn.execute("""update movie set title="The Host(2006)" where `rank`=633""")
print("sucss")
# df.to_csv("movie_data.csv",index=False)
# print("sucs")
def format_rupees(val):
    if val >= 1_000_000_000_000:
        return f"₹{val/1_000_000_000_000:.2f}T"
    elif val >= 1_000_000_000:
        return f"₹{val/1_000_000_000:.2f}B"
    elif val >= 1_000_000:
        return f"₹{val/1_000_000:.2f}M"
    else:
        return f"₹{val:,.0f}"
df = pd.read_sql_query("select * from movie",conn)
print(df)
df = pd.read_sql_query("select * from movie", conn)

for col in ['revenue', 'budget', 'profit']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').apply(
            lambda x: format_rupees(x) if pd.notna(x) and x != 0 else x
        )

print(df)
print("dataclean sunccesfull")
# REPLACE WITH THIS:
df['Rank'] = pd.to_numeric(df['Rank'], errors='coerce').fillna(0).astype(int)
df['Rank'] = range(1, len(df) + 1)
df['Rank'] = df['Rank'].apply(lambda x: f"{x//1000}K" if x >= 1000 else str(x))
print("sucess")
df['Rank'] = range(1, len(df) + 1)  # keep Rank as numbers 1-1000

# Add new column at the end
df['total_movies'] = df['Rank'].apply(lambda x: f"{x//1000}K" if x >= 1000 else str(x))

df.to_csv('movie_data_fixed.csv', index=False)
print("success")
# After your data is loaded



# df.to_csv("movie_data.csv",index=False)
# print("dataclean sunccesfull")