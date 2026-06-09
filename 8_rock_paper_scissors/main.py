names = { "r":"Rock", "p":"Paper", "s":"Scissors" }
choices = { "r":"s", "p":"r",  "s":"p" }


def start():
    input("Press any key to start Rock, Paper, Scissors ")
    input("Grab another player ")
    input("Or be a loser and play by yourself ")
    input("POG")

    while True:
        p1 = (input("Player 1, choose: r (Rock), p (Paper), or s (Scissors): ")).lower()
        while (p1 not in choices): p1= (input("????? Choose R, P, OR S: ")).lower()

        p2 = (input("Player 2, choose: r (Rock), p (Paper), or s (Scissors): ")).lower()
        while (p2 not in choices): p2= (input("????? Choose R, P, OR S: ")).lower()

        if (choices[p1] == p2): input(f"{names[p1]} beats {names[p2]}. Player 1 wins! ")
        elif (choices[p2] == p2): input(f"{names[p2]} beats {names[p1]}. Player 2 wins! ")
        elif (p1 == p2): input(f"Both players chose {names[p2]}. Its a tie! ")
        else: return print("Something went wrong. Kisha fix this shit ")

        again = input("Press y to go again or literally any other key to quit")
        if (again != "y"): return

start()
