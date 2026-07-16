class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        n = len(senate)
        score = 0

        # first removes
        first = senate[0]
        for i, vote in enumerate(senate):
            if vote == "R":
                score += 1
            elif vote == "D":
                score -= 1

        # output: "Dire" "Radiant"
        if score == 0:
            if first == "R":
                return "Radiant"
            else:
                return "Dire"

        winner = "Dire" if score < 0 else "Radiant"
        return winner
