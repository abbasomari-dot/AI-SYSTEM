from scoring_engine import classify_opportunity


def rank_accounts(results):
    ranked = sorted(results, key=lambda x: x["final_opportunity"], reverse=True)
    return ranked


def build_result(username, instagram_opportunity, final_opportunity):
    return {
        "username": username,
        "instagram_opportunity": instagram_opportunity,
        "final_opportunity": final_opportunity,
        "classification": classify_opportunity(final_opportunity)
    }