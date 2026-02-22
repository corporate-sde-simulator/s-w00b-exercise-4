"""
Domain Concept Matcher — match concepts to definitions.

Fill in the 'answers' dictionary below with the correct letter for each concept.
Run this file to check your score: python concept_matcher.py
"""

concepts = {
    1: "Rate Limiting",
    2: "Circuit Breaker",
    3: "Idempotent",
    4: "Cache Invalidation",
    5: "Dead Letter Queue",
    6: "Feature Flag",
    7: "Blue-Green Deploy",
    8: "SLA",
    9: "PII",
    10: "API Versioning",
}

definitions = {
    'A': "A toggle that enables/disables features without redeploying code",
    'B': "Restricting how many requests a client can make in a time window",
    'C': "A pattern that stops calling a failing service to prevent cascade failure",
    'D': "An operation that produces the same result no matter how many times you run it",
    'E': "A storage area for messages that couldn't be processed successfully",
    'F': "Ensuring outdated data is removed from fast-access storage when source changes",
    'G': "Running two identical environments and switching traffic between them",
    'H': "A contract guaranteeing uptime/performance (e.g., 99.9% availability)",
    'I': "Personal data that can identify an individual (name, email, SSN)",
    'J': "Supporting multiple versions of an API simultaneously (e.g., /v1/, /v2/)",
}

# ────────────────────────────────────
# YOUR TASK: Fill in the correct letter for each concept number.
# Example: If concept 1 matches definition 'B', write:  1: 'B'
# ────────────────────────────────────
answers = {
    1: '?',   # Rate Limiting = ?
    2: '?',   # Circuit Breaker = ?
    3: '?',   # Idempotent = ?
    4: '?',   # Cache Invalidation = ?
    5: '?',   # Dead Letter Queue = ?
    6: '?',   # Feature Flag = ?
    7: '?',   # Blue-Green Deploy = ?
    8: '?',   # SLA = ?
    9: '?',   # PII = ?
    10: '?',  # API Versioning = ?
}

# ── Self-check (don't modify below) ──
correct_answers = {1:'B', 2:'C', 3:'D', 4:'F', 5:'E', 6:'A', 7:'G', 8:'H', 9:'I', 10:'J'}

if __name__ == '__main__':
    score = sum(1 for k, v in answers.items() if v == correct_answers[k])
    print(f"\nScore: {score}/10")
    if score == 10:
        print("Perfect! You know your domain concepts.")
    elif score >= 8:
        print("Great! Review the ones you missed in REFERENCE.md")
    else:
        print("Keep studying! Re-read REFERENCE.md and try again.")

    for k in sorted(answers.keys()):
        status = "correct" if answers[k] == correct_answers[k] else f"wrong (correct: {correct_answers[k]})"
        print(f"  {k}. {concepts[k]}: {status}")
