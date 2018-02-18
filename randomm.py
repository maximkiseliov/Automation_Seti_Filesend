def random_poem():
    import random

    poems = ['poem1', 'poem2', 'poem3', 'poem4']
    randompoem = random.choice(poems)
    file = open("poems/" + randompoem + ".txt", 'r')
    poem = file.read()
    file.close()
    return poem


