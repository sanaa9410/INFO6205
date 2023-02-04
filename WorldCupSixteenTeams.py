import random


def stable_matching(group1, group2):
    roundEightTeams = []
    teamsInSemiFinal = []
    teamsInFinal = []

    teamsGroup1 = {
        0: 'England',
        1: 'France',
        2: 'Argentina',
        3: 'Brazil',
        4: 'Mexico',
        5: 'Netherlands',
        6: 'Italy',
        7: 'India',
    }
    teamsGroup2 = {
        0: 'Portugal',
        1: 'Germany',
        2: 'Uruguay',
        3: 'Denmark',
        4: 'USA',
        5: 'Croatia',
        6: 'Wales',
        7: 'Saudi Arabia',
    }

    # Round of Sixteen at World Cup
    print("Round of 16\n")
    team1Pairings = doStableMatchingOnWorldCupRounds(group1, group2)

    for i, num in enumerate(team1Pairings):
        print(teamsGroup1[i] + ' vs ' + teamsGroup2[num])
        teamsPaired = [teamsGroup1[i], teamsGroup2[num]]
        winner = random.choice(teamsPaired)
        print("Winner is: " + winner)
        print("===============================\n")
        roundEightTeams.append(winner)

    random.shuffle(roundEightTeams)

    # For Quarters
    print("Quarter Finals\n")
    group1Quarters = [roundEightTeams.pop() for i in range(8) if i < 4]
    group2Quarters = [roundEightTeams.pop() for i in range(4)]
    mappingGrp1Quarters = {}
    mappingGrp2Quarters = {}

    for index, team in enumerate(group1Quarters):
        mappingGrp1Quarters[index] = team

    for index, team in enumerate(group2Quarters):
        mappingGrp2Quarters[index] = team

    indexes = list(range(4))
    group1PreferencesQtr = []
    group2PreferencesQtr = []
    for x in range(4):
        shuffledList = random.sample(indexes, len(indexes))
        group1PreferencesQtr.append(shuffledList)
        shuffledList2 = random.sample(shuffledList, len(indexes))
        group2PreferencesQtr.append(shuffledList2)

    print("===============================\n")

    team1PairingsQtr = doStableMatchingOnWorldCupRounds(group1PreferencesQtr,
                                                                group2PreferencesQtr)
    for i, num in enumerate(team1PairingsQtr):
        print(mappingGrp1Quarters[i] + ' vs ' + mappingGrp2Quarters[num])
        teamsPaired = [mappingGrp1Quarters[i], mappingGrp2Quarters[num]]
        winner = random.choice(teamsPaired)
        print("Winner is: " + winner)
        print("===============================\n")
        teamsInSemiFinal.append(winner)

    # For Semis
    print("Semi Finals\n")
    groupOneForSemis = [teamsInSemiFinal.pop() for i in range(4) if i < 2]
    groupTwoForSemis = [teamsInSemiFinal.pop() for i in range(2)]
    grp1SemisMapping = {}
    grp2SemisMapping = {}

    for index, team in enumerate(groupOneForSemis):
        grp1SemisMapping[index] = team

    for index, team in enumerate(groupTwoForSemis):
        grp2SemisMapping[index] = team

    indexes = list(range(2))
    group1PreferencesSemis = []
    group2PreferencesSemis = []
    for x in range(2):
        shuffledList = random.sample(indexes, len(indexes))
        group1PreferencesSemis.append(shuffledList)
        shuffledList2 = random.sample(shuffledList, len(indexes))
        group2PreferencesSemis.append(shuffledList2)

    print("\n")

    team1PairingsForSemis = doStableMatchingOnWorldCupRounds(group1PreferencesSemis,
                                                             group2PreferencesSemis)
    for i, num in enumerate(team1PairingsForSemis):
        print(grp1SemisMapping[i] + ' vs ' + grp2SemisMapping[num])
        teamsPaired = [grp1SemisMapping[i], grp2SemisMapping[num]]
        winner = random.choice(teamsPaired)
        print("Winner is: " + winner)
        print("===============================\n")

        teamsInFinal.append(winner)

    print("Finals: " + teamsInFinal[0] + " vs " + teamsInFinal[1])


def doStableMatchingOnWorldCupRounds(group1, group2):
    n = len(group1)
    unPairedTeams = list(range(n))
    team1Pairings = [None] * n
    team2Pairings = [None] * n
    proposalsMadeMyTeam1 = [0] * n
    while unPairedTeams:
        selectedTeamFromGroup1 = unPairedTeams[0]
        preferencesOfSelectedTeam = group1[selectedTeamFromGroup1]
        oppositionTeamFromGroup2 = preferencesOfSelectedTeam[proposalsMadeMyTeam1[selectedTeamFromGroup1]]
        preferencesOfOppositionTeamGroup2 = group2[oppositionTeamFromGroup2]
        currentPairingOfOppositionTeam = team2Pairings[oppositionTeamFromGroup2]

        if currentPairingOfOppositionTeam is None:
            team2Pairings[oppositionTeamFromGroup2] = selectedTeamFromGroup1
            team1Pairings[selectedTeamFromGroup1] = oppositionTeamFromGroup2
            proposalsMadeMyTeam1[selectedTeamFromGroup1] += 1
            unPairedTeams.pop(0)

        else:
            preferenceNumberOfCurrentPairedTeam = preferencesOfOppositionTeamGroup2.index(
                currentPairingOfOppositionTeam)
            preferenceNumberOfSelectedTeamGroup1 = preferencesOfOppositionTeamGroup2.index(selectedTeamFromGroup1)

            if preferenceNumberOfSelectedTeamGroup1 > preferenceNumberOfCurrentPairedTeam:
                team2Pairings[oppositionTeamFromGroup2] = selectedTeamFromGroup1
                team1Pairings[selectedTeamFromGroup1] = oppositionTeamFromGroup2
                proposalsMadeMyTeam1[selectedTeamFromGroup1] += 1
                unPairedTeams.pop(0)
                unPairedTeams.insert(0, currentPairingOfOppositionTeam)
            else:
                proposalsMadeMyTeam1[selectedTeamFromGroup1] += 1
    return team1Pairings




# Test Case 1:
superGroup1 =  [[2, 3, 1, 5, 0, 4, 6, 7],
                [2, 4, 3, 1, 7, 6, 0, 5],
                [2, 7, 4, 6, 5, 0, 1, 3],
                [3, 7, 5, 1, 0, 6, 4, 2],
                [5, 4, 3, 1, 2, 7, 0, 6],
                [1, 2, 3, 6, 0, 7, 4, 5],
                [5, 3, 0, 2, 6, 1, 7, 4],
                [4, 6, 2, 3, 0, 5, 1, 7]
                ]
superGroup2 = [[7, 1, 6, 0, 5, 2, 4, 3],
               [6, 1, 3, 4, 2, 0, 7, 5],
               [4, 0, 3, 6, 5, 2, 1, 7],
               [4, 3, 0, 2, 7, 5, 6, 1],
               [5, 4, 1, 7, 0, 2, 3, 6],
               [6, 7, 5, 4, 1, 3, 0, 2],
               [7, 1, 6, 3, 4, 2, 0, 5],
               [2, 7, 0, 5, 3, 4, 1, 6]
               ]

stable_matching(superGroup1, superGroup2)