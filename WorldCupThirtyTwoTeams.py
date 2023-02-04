import time


def stable_matching(group1, group2):
    startTime = time.time()

    teamsInGroup1 = {
        0: 'England',
        1: 'France',
        2: 'Tunisia',
        3: 'Brazil',
        4: 'Mexico',
        5: 'Netherlands',
        6: 'Spain',
        7: 'Chile',
        8: 'Canada',
        9: 'Australia',
        10: 'Japan',
        11: 'Belgium',
        12: 'Chile',
        13: 'Iran',
        14: 'Sri Lanka',
        15: 'Czech Republic'
    }
    teamsInGroup2 = {
        0: 'Portugal',
        1: 'Germany',
        2: 'Uruguay',
        3: 'South Korea',
        4: 'USA',
        5: 'Croatia',
        6: 'Sudan',
        7: 'Saudi Arabia',
        8: 'Canada',
        9: 'Morocco',
        10: 'Egypt',
        11: 'Qatar',
        12: 'Paraguay',
        13: 'Poland',
        14: 'Mali',
        15: 'Botswana'
    }
    n = len(group1)
    unPairedTeams = list(range(n))
    team1Pairings = [None] * n
    team2Pairings = [None] * n
    team1Proposals = [0] * n
    while unPairedTeams:
        selectedTeamGroup1 = unPairedTeams[0]
        selectedTeamPreference = group1[selectedTeamGroup1]
        oppGroup2 = selectedTeamPreference[team1Proposals[selectedTeamGroup1]]
        oppositionTeamGroup2Preferences = group2[oppGroup2]
        oppositionTeamCurrentPairing = team2Pairings[oppGroup2]

        if oppositionTeamCurrentPairing is None:
            team2Pairings[oppGroup2] = selectedTeamGroup1
            team1Pairings[selectedTeamGroup1] = oppGroup2
            team1Proposals[selectedTeamGroup1] += 1
            unPairedTeams.pop(0)

        else:
            currentPairedTeamPreferenceNumber = oppositionTeamGroup2Preferences.index(
                oppositionTeamCurrentPairing)
            selectedTeamGroup1PreferenceNumber = oppositionTeamGroup2Preferences.index(selectedTeamGroup1)

            if selectedTeamGroup1PreferenceNumber > currentPairedTeamPreferenceNumber:
                team2Pairings[oppGroup2] = selectedTeamGroup1
                team1Pairings[selectedTeamGroup1] = oppGroup2
                team1Proposals[selectedTeamGroup1] += 1
                unPairedTeams.pop(0)
                unPairedTeams.insert(0, oppositionTeamCurrentPairing)
            else:
                team1Proposals[selectedTeamGroup1] += 1
    for i, num in enumerate(team1Pairings):
        print(teamsInGroup1[i] + ' vs ' + teamsInGroup2[num])

    endTime = time.time()

    print(f"\nTime taken for creating a fixture list with 32 teams: \t: {(endTime-startTime)*10**3:.03f}ms")


# Driver level code to generate output

# Test Case 1:
superGroup1 = [[2, 7, 3, 15, 9, 12, 14, 6, 10, 11, 0, 13, 1, 4, 8, 5],
               [0, 1, 15, 14, 11, 7, 3, 9, 2, 5, 13, 12, 10, 8, 4, 6],
               [12, 5, 1, 2, 15, 14, 9, 8, 3, 11, 7, 10, 13, 6, 4, 0],
               [5, 7, 2, 6, 1, 11, 3, 12, 9, 4, 0, 15, 13, 8, 14, 10],
               [13, 7, 2, 6, 5, 4, 15, 11, 0, 1, 8, 12, 14, 10, 9, 3],
               [8, 3, 14, 2, 11, 13, 12, 7, 9, 1, 4, 15, 10, 0, 6, 5],
               [4, 7, 12, 14, 0, 8, 3, 10, 1, 15, 2, 6, 13, 9, 5, 11],
               [12, 5, 9, 10, 6, 13, 0, 3, 4, 1, 14, 2, 7, 8, 15, 11],
               [1, 12, 3, 15, 6, 7, 10, 14, 5, 11, 2, 8, 0, 13, 4, 9],
               [8, 5, 2, 12, 9, 15, 13, 3, 0, 7, 4, 1, 11, 6, 14, 10],
               [11, 12, 2, 1, 15, 6, 13, 4, 3, 5, 7, 0, 10, 14, 8, 9],
               [11, 2, 7, 10, 5, 12, 8, 6, 9, 15, 4, 0, 1, 3, 14, 13],
               [5, 6, 12, 1, 9, 10, 11, 0, 4, 15, 14, 7, 8, 3, 2, 13],
               [5, 1, 12, 11, 6, 2, 4, 8, 13, 0, 3, 14, 7, 10, 15, 9],
               [15, 3, 5, 7, 8, 2, 11, 14, 6, 9, 1, 4, 12, 10, 13, 0],
               [6, 9, 12, 7, 15, 5, 13, 3, 8, 14, 0, 1, 10, 11, 4, 2]]

superGroup2 = [
    [10, 0, 7, 2, 14, 9, 15, 12, 13, 3, 8, 6, 5, 11, 4, 1],
    [1, 11, 12, 8, 14, 4, 9, 5, 0, 7, 3, 15, 6, 10, 13, 2],
    [0, 10, 1, 2, 4, 13, 14, 5, 9, 7, 12, 6, 3, 15, 11, 8],
    [0, 1, 12, 6, 7, 5, 10, 15, 2, 9, 4, 13, 14, 8, 3, 11],
    [11, 4, 5, 1, 10, 12, 8, 2, 0, 15, 9, 3, 7, 13, 6, 14],
    [0, 2, 11, 4, 10, 9, 5, 13, 7, 6, 1, 14, 12, 15, 3, 8],
    [11, 4, 10, 12, 0, 8, 3, 5, 9, 1, 6, 7, 13, 2, 14, 15],
    [1, 9, 14, 5, 7, 12, 15, 0, 6, 11, 2, 4, 8, 3, 13, 10],
    [13, 2, 10, 9, 5, 15, 11, 14, 4, 7, 6, 12, 1, 3, 8, 0],
    [3, 7, 8, 9, 14, 13, 1, 2, 10, 11, 15, 5, 0, 4, 6, 12],
    [4, 0, 8, 14, 10, 13, 7, 9, 12, 2, 11, 15, 1, 6, 5, 3],
    [7, 13, 6, 1, 2, 8, 15, 10, 3, 5, 12, 11, 0, 9, 4, 14],
    [11, 9, 3, 6, 0, 12, 5, 10, 4, 14, 2, 8, 13, 1, 15, 7],
    [12, 0, 9, 1, 7, 10, 8, 13, 6, 14, 15, 11, 4, 3, 2, 5],
    [2, 0, 3, 10, 4, 15, 13, 11, 8, 1, 12, 14, 6, 9, 7, 5],
    [11, 14, 9, 1, 15, 6, 10, 2, 5, 7, 3, 0, 12, 4, 8, 13]
]

stable_matching(superGroup1, superGroup2)