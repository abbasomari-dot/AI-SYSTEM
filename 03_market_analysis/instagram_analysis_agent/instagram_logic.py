from scoring_engine import (
    calculate_engagement,
    engagement_score,
    opportunity_score,
    bio_score,
    activity_score
)


def instagram_opportunity(account):
    engagement = calculate_engagement(
        int(account["followers"]),
        int(account["avg_likes"]),
        int(account["avg_comments"])
    )

    eng_score = engagement_score(engagement)
    bio_sc = bio_score(account["bio"])
    activity_sc = activity_score(int(account["posts_count"]))

    instagram_total = (
        (eng_score * 0.5) +
        (bio_sc * 0.3) +
        (activity_sc * 0.2)
    )
    instagram_total = round(instagram_total, 2)

    return opportunity_score(instagram_total)