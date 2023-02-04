import time


def doStableMatchingWorldCup(group1, group2):
    startTime = time.time()
    n = len(group1)
    teamGroup1 = {
        0: 'England',
        1: 'France',
        2: 'South Korea',
        3: 'New Zealand',
        4: 'Sri Lanka',
        5: 'Nigeria',
        6: 'Japan',
        7: 'Canada',
    }
    teamGroup2 = {
        0: 'China',
        1: 'Spain',
        2: 'Uruguay',
        3: 'Morocco',
        4: 'USA',
        5: 'Mexico',
        6: 'Italy',
        7: 'Turkey',
    }
    unPairedTeams = list(range(n))
    finalTeam1Pairings = [None] * n
    finalTeam2Pairings = [None] * n
    proposalsMadeMyTeam1 = [0] * n
    while unPairedTeams:
        selectedTeamGroup1 = unPairedTeams[0]
        prefSelectedTeam = group1[selectedTeamGroup1]
        oppTeamGroup2 = prefSelectedTeam[proposalsMadeMyTeam1[selectedTeamGroup1]]
        prefOppTeamGroup2 = group2[oppTeamGroup2]  # [2, 1, 0]
        currPairingOppTeam = finalTeam2Pairings[oppTeamGroup2]

        if currPairingOppTeam is None:
            finalTeam2Pairings[oppTeamGroup2] = selectedTeamGroup1
            finalTeam1Pairings[selectedTeamGroup1] = oppTeamGroup2
            proposalsMadeMyTeam1[selectedTeamGroup1] += 1
            unPairedTeams.pop(0)

        else:
            prefNumbCurrPairedTeam = prefOppTeamGroup2.index(
                currPairingOppTeam)
            prefNumSelectedTeamGroup1 = prefOppTeamGroup2.index(selectedTeamGroup1)

            if prefNumSelectedTeamGroup1 > prefNumbCurrPairedTeam:
                finalTeam2Pairings[oppTeamGroup2] = selectedTeamGroup1
                finalTeam1Pairings[selectedTeamGroup1] = oppTeamGroup2
                proposalsMadeMyTeam1[selectedTeamGroup1] += 1
                unPairedTeams.pop(0)
                unPairedTeams.insert(0, currPairingOppTeam)
            else:
                proposalsMadeMyTeam1[selectedTeamGroup1] += 1
    endTime = time.time()
    print(startTime)
    print(endTime)
    for i, num in enumerate(finalTeam1Pairings):
        print(teamGroup1[i] + ' vs ' + teamGroup2[num])

    print(f"Time taken for creating a fixture list with 16 teams: \t: {(endTime - startTime) * 10 ** 3:.03f}ms")


superGroup1 = [
    [6, 7, 1, 2, 0, 3, 4, 5],
    [6, 0, 3, 7, 1, 5, 2, 4],
    [4, 1, 5, 3, 2, 7, 6, 0],
    [6, 7, 3, 1, 5, 4, 2, 0],
    [1, 4, 3, 6, 5, 2, 7, 0],
    [2, 5, 3, 7, 4, 6, 1, 0],
    [7, 1, 0, 2, 5, 3, 4, 6],
    [5, 1, 7, 4, 3, 2, 6, 0]
]
superGroup2 = [
    [0, 6, 4, 2, 5, 7, 1, 3],
    [7, 1, 4, 6, 0, 3, 5, 2],
    [7, 5, 6, 0, 2, 3, 4, 1],
    [6, 2, 3, 0, 4, 7, 5, 1],
    [6, 7, 5, 1, 4, 2, 0, 3],
    [1, 3, 4, 2, 0, 6, 5, 7],
    [6, 3, 4, 7, 0, 2, 5, 1],
    [6, 4, 3, 0, 7, 2, 5, 1]
]


doStableMatchingWorldCup(superGroup1, superGroup2)