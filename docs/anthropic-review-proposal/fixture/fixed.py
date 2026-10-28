def can_reserve(used, amount, limit):
    return used + amount <= limit


def restore(snapshot, limit):
    used = snapshot["used"]
    if used < 0 or used > limit:
        raise ValueError("negative usage")
    return used
