import pandas as pd

# قراءة ملف البيانات الخام
df = pd.read_csv("../../data/raw/doha_restaurants_google_places_full.csv")

# تنظيف البيانات
df = df.dropna(subset=["Rating", "Reviews"])

df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
df["Reviews"] = pd.to_numeric(df["Reviews"], errors="coerce")

# نظام التصنيف
def classify(row):
    if row["Rating"] >= 4.3 and row["Reviews"] >= 500:
        return "🔥 High Potential"
    elif row["Rating"] >= 4.0 and row["Reviews"] >= 200:
        return "🟡 Medium Potential"
    else:
        return "⚪ Low Potential"

df["Category"] = df.apply(classify, axis=1)

# ترتيب
df = df.sort_values(by="Reviews", ascending=False)

# حفظ الملف المعالج
df.to_csv("../../data/processed/doha_restaurants_classified.csv", index=False)

print("تم إنشاء ملف التصنيف داخل data/processed")
def activity_score(posts_count):
    """
    تقييم النشاط بناءً على عدد المنشورات الكلي
    """
    if posts_count >= 300:
        return 80
    elif posts_count >= 150:
        return 60
    elif posts_count >= 50:
        return 40
    elif posts_count >= 10:
        return 20
    else:
        return 10