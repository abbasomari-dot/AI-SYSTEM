def google_quality_multiplier(rating):
    """
    Google يعمل كفلتر جودة فقط
    لا يزيد الفرصة — فقط يخفضها إذا الجودة ضعيفة
    """
    rating = float(rating)

    if rating >= 4.0:
        return 1.0
    elif rating >= 3.5:
        return 0.8
    else:
        return 0.5


def apply_google_filter(instagram_opportunity, rating):
    multiplier = google_quality_multiplier(rating)
    return round(instagram_opportunity * multiplier, 2)