import numpy as np

def game_core(number, begin, end):
    """Divide the segment in half many times"""    
    count = 0
    while True:        
        count += 1 
        predict = int((begin+end) / 2)
        #print(predict, end=" ")
        if number > predict: 
            begin = predict
        elif number < predict: 
            end = predict
        else: break                
    #print(f" | {count}")
    
    return(count)


def score_game(game_core):
    """Run the game many times"""
    low = 1
    high = 101
    quantity = 1000
    count_ls = []      
    
    np.random.seed(1)    
    random_array = np.random.randint(low, high, size=(quantity))
    #print(random_array)
    for number in random_array:
        count_ls.append(game_core(number, low, high))
    
    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses numbers on average in {score} attempts")
    
    return(score)


score_game(game_core)
