def create_game():
    from random import randint
    answer=''
    for i in range(4):
        answer+=str(randint(1,9))
    return answer
