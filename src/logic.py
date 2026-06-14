#LOGICS FOR GUARDIAN.

def compute_risk(objects):
    risk = 0

    if "cell phone" in objects:
        risk += 2

    if "person" not in objects:
        risk +=2  # idle state

    if len(objects) > 6:
        risk += 1

    if risk >= 3:
        return "high"
    elif risk >= 1:
        return "medium"
    else:
        return "low"
    
def focus_score(objects):
    score = 100

    if "cell phone" in objects:
        score -= 30

    if "person" not in objects:
        score -= 10

    if len(objects) > 6:
        score -= 15

    return max(score, 0)   

def workspace_state(objects):

    if "person" not in objects:
        return "Workspace Unattended"

    elif "cell phone" in objects:
        return "Phone Usage Detected"

    elif "laptop" in objects and len(objects) <= 3:
        return "Deep Focus"

    else:
        return "Minor Distraction"
    

#Guardian says (Verdict)    
def guardian_verdict(state):

    verdicts = {
        "Deep Focus":
            "Guardian approves. Keep cooking.",

        "Phone Usage Detected":
            "Phone spotted again. Nice try.",

        "Workspace Unattended":
            "Guardian is wondering where you went.",

        "Minor Distraction":
            "Guardian sees someone slacking again."
    }

    return verdicts.get(state, "Monitoring workspace.")

#Ext. Recommendations

def recommendation(state):

    tips = {
        "Deep Focus":
            "Current setup looks good.",

        "Phone Usage Detected":
            "Move phone away from workspace.",

        "Workspace Unattended":
            "Resume session or pause tracking.",

        "Minor Distraction":
            "Reduce unnecessary desk items."
    }

    return tips.get(state, "Stay focused.")

#Reasoning the risks.

def risk_reasoning(objects):

    reasons = []

    if "cell phone" in objects:
        reasons.append("Phone detected (+2)")

    if "person" not in objects:
        reasons.append("No person detected (+1)")

    if len(objects) > 6:
        reasons.append("Many objects detected (+1)")

    if not reasons:
        reasons.append("No major distractions")

    return reasons

