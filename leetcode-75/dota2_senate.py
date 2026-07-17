class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        # Scan the senate
        dire_voters = []
        radiant_voters = []
        for i, vote in enumerate(senate):
            if vote == "R":
                radiant_voters.append(i)
            else:
                dire_voters.append(i)

        # Process of elimination

        while True:
            # [0]
            # [1, 2]
            if len(dire_voters) == 0:
                return "Radiant"
            if len(radiant_voters) == 0:
                return "Dire"

            d_i = 0
            r_i = 0
            while True:
                if len(dire_voters) == d_i or len(radiant_voters) == r_i:
                    # one side can not vote no more. Remove the one vote on the other for each remaining
                    if d_i == len(dire_voters):
                        to_remove = len(radiant_voters) - r_i
                        for _ in range(to_remove):
                            if len(dire_voters) == 0:
                                break
                            dire_voters.pop(0)

                    if r_i == len(radiant_voters):
                        to_remove = len(dire_voters) - d_i
                        for _ in range(to_remove):
                            if len(radiant_voters) == 0:
                                break
                            radiant_voters.pop(0)
                    break

                if dire_voters[d_i] < radiant_voters[r_i]:
                    radiant_voters.pop(r_i)
                    d_i += 1
                else:
                    dire_voters.pop(d_i)
                    r_i += 1
