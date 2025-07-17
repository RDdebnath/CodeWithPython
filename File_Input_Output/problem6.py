import random

def game():
    print("You are playing the game..")
    score = random.randint(1, 100)
    with open("HighScore.txt") as f:
        HighScore = f.read()
        if(HighScore!=""):
            HighScore = int(HighScore)
        else:
            HighScore = 0
    
    print(f"Your Score: {score}")
    if(score>HighScore):
        with open("HighScore.txt", "w") as f:
            f.write(str(score))
    return score

game()