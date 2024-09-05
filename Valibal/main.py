def game(total_game):

    for i in range(total_game):
        q = 0
        c = 0

        total_game_sets = int(input())
        games = input()

        for j in range(total_game_sets):
            if games[j] == "Q":
                q += 1
            elif games[j] == "C":
                c += 1

        if q > c:
            print("Quera")
        elif q < c:
            print("CodeCup")

number_games = int(input())
game(number_games)