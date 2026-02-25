import csv

from instagram_logic import instagram_opportunity
from google_logic import apply_google_filter
from ranking_engine import rank_accounts, build_result


def main():
    results = []

    with open("accounts.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            insta_opp = instagram_opportunity(row)
            final_opp = apply_google_filter(insta_opp, row["google_rating"])

            result = build_result(
                row["username"],
                insta_opp,
                final_opp
            )

            results.append(result)

    ranked = rank_accounts(results)

    print("\n=== STABLE V1 MARKET ENGINE ===\n")

    for r in ranked:
        print(f"{r['username']}")
        print(f"  Instagram Opportunity: {r['instagram_opportunity']}/100")
        print(f"  Final Opportunity: {r['final_opportunity']}/100")
        print(f"  Classification: {r['classification']}")
        print("")


if __name__ == "__main__":
    main()