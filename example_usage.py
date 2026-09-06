import json
from client import IntentSignalPropensityScorer

def main():
    scorer = IntentSignalPropensityScorer(half_life_days=25.0)
    signals = [
        {"type": "funding_announcement", "date": "2026-09-01", "description": "Closed $20M Series B"},
        {"type": "executive_hire", "date": "2026-08-25", "description": "Hired new VP of Sales"},
        {"type": "active_job_opening_match", "date": "2026-09-04", "description": "Hiring 5 Senior Data Engineers"}
    ]
    result = scorer.score_account_intent("Nexus Cloud Analytics", signals, reference_date="2026-09-06")
    print("Intent Propensity Scoring Result:")
    print(json.dumps(result, indent=2))
    assert result["propensity_score"] > 50.0
    print("Intent scorer verification complete: PASS")

if __name__ == "__main__":
    main()
