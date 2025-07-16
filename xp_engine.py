def calculate_xp(matched_skills, missing_skills):
    """
    XP is calculated as:
    - +10 XP per matched skill
    - +2 XP encouragement for each missing skill (user attempted analysis)
    """
    return len(matched_skills) * 10 + len(missing_skills) * 2


def get_level(xp):
    """
    Convert XP to fun gamified levels.
    You can modify levels and XP thresholds as you like.
    """
    if xp >= 200:
        return "🚀 Expert"
    elif xp >= 150:
        return "🔥 Pro"
    elif xp >= 100:
        return "🎯 Intermediate"
    elif xp >= 50:
        return "📘 Learner"
    else:
        return "🌱 Beginner"
