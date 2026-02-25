def calculate_engagement(followers, avg_likes, avg_comments):
    if followers == 0:
        return 0
    return ((avg_likes + avg_comments) / followers) * 100


def engagement_score(engagement_rate):
    if engagement_rate >= 8:
        return 90
    elif engagement_rate >= 5:
        return 75
    elif engagement_rate >= 3:
        return 60
    elif engagement_rate >= 1:
        return 40
    else:
        return 20


def opportunity_score(total_score):
    return 100 - total_score


def classify_opportunity(opportunity):
    if opportunity >= 70:
        return "🔥 HIGH TARGET"
    elif opportunity >= 40:
        return "🟡 MEDIUM TARGET"
    else:
        return "⚪ LOW TARGET"


def bio_score(bio):
    score = 0
    bio_lower = bio.lower()

    if len(bio) > 20:
        score += 20

    if "@" in bio or "www" in bio or "http" in bio:
        score += 20

    if "order" in bio_lower or "call" in bio_lower or "contact" in bio_lower:
        score += 20

    keywords = ["restaurant", "cafe", "food", "grill", "kitchen"]
    if any(word in bio_lower for word in keywords):
        score += 20

    return min(score, 80)


def activity_score(posts_count):
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