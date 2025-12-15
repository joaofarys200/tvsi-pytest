def smart_sum(a, b):
    if a < 0 or b < 0:
        raise ValueError("Negative numbers not allowed")

    if a == 0 and b == 0:
        return 0

    total = a + b
    if total > 100:
        return 100

    return total
