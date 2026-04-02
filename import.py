import pandas as pd
df  = pd.read_csv("/Users/munavathsai/project.ds/IMDB-Movie-Data.csv",encoding="latin1",on_bad_lines="skip",engine="python")
print("data load succesfull")
print("shaped data",df.shape)
print("\n columes",df.columns.tolist())
print("top five data")
print(df.head())
print("\n datatype")
print(df.dtypes)
#Missing value percentage per column
missing = pd.DataFrame({
    'Missing Count': df.isnull().sum(),
    'Missinf %': (df.isnull().sum() / len(df)) * 100
})
missing.to_csv("null-values.csv")
print("null sucessfull")
print("📊 Missing Value Report:")
print(missing[missing['Missing Count'] > 0])
#  Fill missing Revenue and Budget with median
df['Revenue (Millions)'] = pd.to_numeric(df['Revenue (Millions)'], errors='coerce')
# df['Revenue (Millions)'].fillna(df['Revenue (Millions)'].median(), inplace=True)
df["Revenue (Millions)"].fillna(df["Revenue (Millions)"].median(),inplace=True)


df['Runtime (Minutes)'] = pd.to_numeric(df['Runtime (Minutes)'], errors='coerce')
df['Runtime (Minutes)'].fillna(df['Runtime (Minutes)'].median(), inplace=True)

df['Rating'].fillna(df['Rating'].median(), inplace=True)
df['Metascore'].fillna(df['Metascore'].median(), inplace=True)
df["Revenue (Millions)"] = (df["Revenue (Millions)"]*83)
print("sucss")


# 2. Standardize Genre names
df['Genre'] = df['Genre'].str.strip()

# # 3. Remove negative or zero revenue
# df = df[df["Revenue(Millions)"] >0]
df = df[df['Revenue (Millions)'] > 0]
df["budget"] = (df["Revenue (Millions)"]*60.0)
print("sucss")
df["profit"] = (df["budget"]-df['Revenue (Millions)'])
print("sucss")

# # 4. Add Profit column
# df['Profit (Millions)'] = df['Revenue (Millions)'] - df['Metascore']

# 5. Add ROI column
df['ROI'] = (df["profit"] / df["budget"]) * 100
print("sucss")
# # 6. Add Hit or Flop column
df['Hit_Flop'] = df['Revenue (Millions)'].apply(
    lambda x: 'Hit' if x > df['Revenue (Millions)'].median() else 'Flop'
)

print("✅ Data Cleaned!")
print("Shape after cleaning:", df.shape)
print(df.head())
df = df.rename(columns={"Revenue (Millions)":"collations"})
print("succes")
df.to_csv("clead-calltions.csv",index=False)
print("dataclean sunccesfull")
print(df.dtypes)
any_duplicate  = df["Title"].duplicated().any()
print(any_duplicate)

dupicate = df[df["Title"].duplicated()]
print(dupicate)
df["Title"] = df["Title"].replace("The Host", "The Host Movie")
print("sucss")

