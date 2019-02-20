class Life(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_neighbours(self):
        neighbours = set()
        neighbours.add(Life(self.x + 1, self.y))
        neighbours.add(Life(self.x + 1, self.y + 1))
        neighbours.add(Life(self.x + 1, self.y - 1))
        neighbours.add(Life(self.x - 1, self.y - 1))
        neighbours.add(Life(self.x - 1, self.y))
        neighbours.add(Life(self.x - 1, self.y + 1))
        neighbours.add(Life(self.x, self.y + 1))
        neighbours.add(Life(self.x, self.y - 1))

        return neighbours

    def show(self):
        print("x = " + str(self.x) + ", y + " + str(self.y) + "; ")
        # print("x = %s, y = %s;" % (self.x, self.y))


life = Life(3, 5)
for el in life.get_neighbours():
    el.show()


class Game(object):
    def __init__(self):
        self.lives = set()

    def add_lives(self, lives):
        self.lives.add(lives)

    def get_possible_to_emerge(self):
        possible_to_emerge = set()

        for live in self.lives:
            neighbour = live.get_neighbours()
            possible_to_emerge = possible_to_emerge.union(neighbour)

        return possible_to_emerge
