class HackathonEvaluator:
    def __init__(self, min_size: int = 2, max_size: int = 4):
        """
        Initializes the hackathon configuration limits.
        """
        self.min_size = min_size
        self.max_size = max_size
        self.valid_teams = []
        self.disqualified_teams = []

    def process_teams(self, teams_data: list):
        """
        Validates team formations, aggregates round scores, and filters out non-compliant structures.
        """
        for team in teams_data:
            team_name = team["team_name"]
            members = team["members"]
            round_scores = team["round_scores"]  # Expected to be a list of integers/floats

            team_size = len(members)

            # 1. Validation Rule: Team Size Constraint Check
            if team_size < self.min_size or team_size > self.max_size:
                self.disqualified_teams.append({
                    "team_name": team_name,
                    "reason": f"Invalid size ({team_size} members). Must be between {self.min_size} and {self.max_size}."
                })
                continue

            # 2. Score Aggregation
            total_score = sum(round_scores)
            highest_single_round = max(round_scores) if round_scores else 0

            # Map compiled stats to validation array
            self.valid_teams.append({
                "team_name": team_name,
                "members": members,
                "round_scores": round_scores,
                "total_score": total_score,
                "highest_round": highest_single_round
            })

    def generate_rankings(self):
        """
        Sorts the valid teams using primary total scores and handles tied conditions
        using the highest single round score as a secondary tie-breaker.
        """
        # Sort Logic: Primary sort key is total_score descending (-x['total_score'])
        # Secondary sort key (tie-breaker) is highest_round descending (-x['highest_round'])
        sorted_rankings = sorted(
            self.valid_teams,
            key=lambda x: (x["total_score"], x["highest_round"]),
            reverse=True
        )
        return sorted_rankings

    def display_leaderboard(self):
        """
        Outputs clean visual tables for the finalized standings and alerts.
        """
        rankings = self.generate_rankings()

        print("=== HACKATHON LEADERBOARD ===")
        print(f"{'Rank':<5} | {'Team Name':<20} | {'Members':<8} | {'Total Score':<12} | {'Tie-Breaker (Max Rd)'}")
        print("-" * 70)

        for rank, team in enumerate(rankings, start=1):
            print(
                f"{rank:<5} | {team['team_name']:<20} | {len(team['members']):<8} | {team['total_score']:<12} | {team['highest_round']}")

        if self.disqualified_teams:
            print("\n🚨 DISQUALIFICATION ALERTS:")
            for dq in self.disqualified_teams:
                print(f"  - Team '{dq['team_name']}': {dq['reason']}")
        print("=" * 70)


# --- Execution Example ---
if __name__ == "__main__":
    # Test dataset mapping hackathon metrics
    raw_hackathon_data = [
        {
            "team_name": "Byte Builders",
            "members": ["Alice", "Bob", "Charlie"],
            "round_scores": [85, 90, 92]  # Total: 267, Max Rd: 92
        },
        {
            "team_name": "Code Cruisers",
            "members": ["David", "Eva"],
            "round_scores": [95, 82, 90]  # Total: 267, Max Rd: 95 (Tied total with Byte Builders!)
        },
        {
            "team_name": "Solo Hacker",
            "members": ["Frank"],
            "round_scores": [90, 95, 100]  # Disqualified: Too small
        },
        {
            "team_name": "Data Wizards",
            "members": ["Grace", "Hank", "Ivy", "Jack"],
            "round_scores": [88, 85, 87]  # Total: 260, Max Rd: 88
        },
        {
            "team_name": "Mega Syndicate",
            "members": ["Liam", "Mona", "Ned", "Opal", "Pete"],
            "round_scores": [99, 99, 99]  # Disqualified: Too large
        }
    ]

    # Initialize evaluator with rules: Teams must be between 2 and 4 members
    evaluator = HackathonEvaluator(min_size=2, max_size=4)

    # Process and rank
    evaluator.process_teams(raw_hackathon_data)
    evaluator.display_leaderboard()
