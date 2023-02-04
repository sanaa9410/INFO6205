import random


def doStableMatchingOnWorldCupRounds(group1, group2):
    n = len(group1)
    numStableMatches = 0
    for x in range(1000):
        random.shuffle(group1)
        random.shuffle(group2)
        unPairedTeams = list(range(n))  
        finalTeam1Pairings = [None] * n  
        finalTeam2Pairings = [None] * n  
        proposalsByTeam1 = [0] * n
        while unPairedTeams:
            selectedTeamGroup1 = unPairedTeams[0]
            prefSelectedTeam = group1[selectedTeamGroup1]
            oppTeamGroup2 = prefSelectedTeam[
                proposalsByTeam1[selectedTeamGroup1]]
            prefOppTeamGroup2 = group2[oppTeamGroup2]
            currPairingOppTeam = finalTeam2Pairings[oppTeamGroup2]

            if currPairingOppTeam is None:
                finalTeam2Pairings[oppTeamGroup2] = selectedTeamGroup1
                finalTeam1Pairings[selectedTeamGroup1] = oppTeamGroup2
                proposalsByTeam1[selectedTeamGroup1] += 1
                unPairedTeams.pop(0)  

            else:
                prefNoCurrentPairedTeam = prefOppTeamGroup2.index(
                    currPairingOppTeam)
                prefNoSelectedTeamGroup1 = prefOppTeamGroup2.index(selectedTeamGroup1)

                if prefNoSelectedTeamGroup1 > prefNoCurrentPairedTeam:
                    finalTeam2Pairings[oppTeamGroup2] = selectedTeamGroup1
                    finalTeam1Pairings[selectedTeamGroup1] = oppTeamGroup2
                    proposalsByTeam1[selectedTeamGroup1] += 1
                    unPairedTeams.pop(0)
                    unPairedTeams.insert(0, currPairingOppTeam)
                else:
                    proposalsByTeam1[selectedTeamGroup1] += 1

        if None not in finalTeam1Pairings:
            numStableMatches += 1

    percentageSuccessfulMatches = (numStableMatches/1000) * 100
    print("Percentage of successful matches :", percentageSuccessfulMatches, "%")



superGroup1 = [
    [0, 2, 4, 6, 7, 3, 5, 1],
    [0, 2, 1, 3, 5, 6, 4, 7],
    [1, 2, 3, 4, 7, 6, 5, 0],
    [7, 6, 1, 3, 4, 2, 5, 0],
    [4, 6, 7, 2, 1, 3, 0, 5],
    [3, 7, 4, 1, 2, 0, 5, 6],
    [5, 7, 1, 0, 2, 4, 3, 6],
    [0, 2, 4, 6, 7, 3, 5, 1],
]
superGroup2 = [
    [0, 1, 4, 7, 6, 3, 5, 2],
    [0, 2, 1, 7, 5, 4, 6, 3],
    [3, 2, 1, 7, 4, 6, 5, 0],
    [1, 5, 7, 3, 4, 2, 6, 0],
    [5, 6, 7, 2, 0, 3, 1, 4],
    [2, 6, 4, 1, 3, 5, 0, 7],
    [4, 6, 1, 0, 7, 5, 3, 2],
    [1, 2, 4, 7, 6, 3, 5, 0],
]

doStableMatchingOnWorldCupRounds(superGroup1, superGroup2)