import json


# ------------------------
# Diff Utility
# ------------------------
def diff_versions(v1_json: str, v2_json: str):
    """
    Compares two JSON strings representing event versions and returns the differences.
    """
    v1 = json.loads(v1_json)
    v2 = json.loads(v2_json)

    diffs = {}
    for key in set(v1.keys()).union(set(v2.keys())):
        if v1.get(key) != v2.get(key):
            diffs[key] = {
                "from": v1.get(key),
                "to": v2.get(key)
            }
    return diffs
