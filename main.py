from src.game import Game

if __name__ == '__main__':
    currentDirec = "down"
    game = Game()
    game.login()
    game.run(currentDirec)