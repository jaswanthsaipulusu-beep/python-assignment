
from itertools import combinations

def balance_groups(scores, group_sizes):
    if any(not isinstance(s, (int, float)) or isinstance(s, bool)
           for s in scores):
        raise ValueError("Scores must be numeric.")

    if any(not isinstance(n, int) or isinstance(n, bool) or n < 0
           for n in group_sizes):
        raise ValueError("Group sizes must be non-negative integers.")

    if sum(group_sizes) != len(scores):
        raise ValueError("Group sizes must equal the number of students.")

    if not group_sizes or any(n == 0 for n in group_sizes):
        raise ValueError("Every group must have at least one student.")

    best_groups = None
    best_difference = float("inf")

    def search(remaining, sizes, groups):
        nonlocal best_groups, best_difference

        if not sizes:
            totals = [sum(g) for g in groups]
            difference = max(totals) - min(totals)

            if difference < best_difference:
                best_difference = difference
                best_groups = [g[:] for g in groups]
            return

        size = sizes[0]

        # Choose students for the current group
        for chosen in combinations(remaining, size):
            chosen_set = set(chosen)
            next_remaining = [
                s for s in remaining if s not in chosen_set
            ]

            search(
                next_remaining,
                sizes[1:],
                groups + [list(chosen)]
            )

    search(list(scores), list(group_sizes), [])

    print("=== STUDENT GROUP REPORT ===")
    for i, group in enumerate(best_groups, start=1):
        print(f"Group {i}: {group}")
        print(f"Total Score: {sum(group)}")

    totals = [sum(g) for g in best_groups]
    print("\nHighest Group Total:", max(totals))
    print("Lowest Group Total:", min(totals))
    print("Score Difference:", best_difference)

    return best_groups


# Example input
scores = [90, 85, 80, 75, 70, 65, 60, 55]
group_sizes = [3, 3, 2]

balance_groups(scores, group_sizes)
