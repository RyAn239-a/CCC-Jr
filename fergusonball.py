def main():
    stars = 0
    players = int(input())
    for i in range(players):
        points = int(input())
        fouls = int(input())
        total += points * 5 - fouls * 3
        if total > 40:
            stars += 1
    if stars == players:
        print(f"{stars}+")
    else:
        print(stars)

if __name__ == "__main__":
    main()

