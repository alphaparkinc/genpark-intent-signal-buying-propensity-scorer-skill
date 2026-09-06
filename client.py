import math
import datetime
from typing import Dict, Any, List

class IntentSignalPropensityScorer:
    """
    Computes weighted, time-decayed buying intent propensity scores from heterogeneous B2B signals.
    """
    SIGNAL_WEIGHTS = {
        "executive_hire": 25.0,
        "funding_announcement": 30.0,
        "active_job_opening_match": 15.0,
        "website_traffic_surge": 12.0,
        "tech_stack_migration": 18.0,
        "vendor_evaluation_review": 22.0
    }

    def __init__(self, half_life_days: float = 30.0):
        self.half_life_days = half_life_days

    def calculate_decay(self, signal_age_days: float) -> float:
        if signal_age_days < 0:
            signal_age_days = 0
        return math.exp(-math.log(2) * (signal_age_days / self.half_life_days))

    def score_account_intent(self, account_name: str, signals: List[Dict[str, Any]], reference_date: Optional[str] = None) -> Dict[str, Any]:
        if reference_date:
            ref_dt = datetime.date.fromisoformat(reference_date)
        else:
            ref_dt = datetime.date.today()

        total_weighted_points = 0.0
        max_possible_points = 0.0
        audited_signals: List[Dict[str, Any]] = []

        for sig in signals:
            sig_type = sig.get("type", "unknown")
            base_weight = self.SIGNAL_WEIGHTS.get(sig_type, 10.0)
            sig_date_str = sig.get("date", ref_dt.isoformat())
            try:
                sig_dt = datetime.date.fromisoformat(sig_date_str)
                age_days = (ref_dt - sig_dt).days
            except Exception:
                age_days = 0

            decay_multiplier = self.calculate_decay(max(0, age_days))
            effective_score = base_weight * decay_multiplier
            total_weighted_points += effective_score
            max_possible_points += base_weight

            audited_signals.append({
                "type": sig_type,
                "description": sig.get("description", ""),
                "age_days": age_days,
                "base_weight": base_weight,
                "decay_multiplier": round(decay_multiplier, 3),
                "effective_points": round(effective_score, 2)
            })

        # Propensity Score bounded 0 - 100
        propensity_score = min(100.0, round(total_weighted_points * 1.25, 2))
        
        if propensity_score >= 80:
            intent_tier = "Urgent Outbound Trigger"
            recommended_action = "Execute hyper-personalized multi-channel sequence within 24 hours."
        elif propensity_score >= 55:
            intent_tier = "In-Market High Intent"
            recommended_action = "Target VP/C-level stakeholders with ROI benchmark case studies."
        elif propensity_score >= 30:
            intent_tier = "Warm Engagement"
            recommended_action = "Enroll in mid-funnel nurture flow with industry insights."
        else:
            intent_tier = "Cold Baseline"
            recommended_action = "Maintain quarterly automated touchpoint."

        return {
            "account_name": account_name,
            "propensity_score": propensity_score,
            "intent_tier": intent_tier,
            "recommended_action": recommended_action,
            "active_signal_count": len(signals),
            "signal_audit": audited_signals
        }
