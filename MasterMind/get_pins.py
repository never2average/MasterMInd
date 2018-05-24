def copy(List):
    copy_L=[]
    for i in List:
        copy_L.append(i)
    return copy_L
def get_pins(guess,answer):
    red_pins=0
    white_pins=0
    guess_copy=copy(guess)
    answer_copy =copy(answer)

    for i in range(4):
        if guess_copy[i]==answer_copy[i]:
            red_pins+=1
            answer_copy[i]=""
            guess_copy[i]=""
    for i in range(4):
        for j in range(4):
            if guess_copy[i]==answer_copy[j] and answer_copy[j] !='':
                white_pins+=1
                guess_copy[i]=""
                answer_copy[j]=""
    
    return [red_pins,white_pins]
