def get_best_word(points, words):
    scores = []
    best = [0, 0]
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for word in words:
        score = 0 
        for letter in word.lower():
            ind = alphabet.index(letter)
            
            score += points[ind]
               
        if score > best[0]:
            best = [score, words.index(word)]
        elif score == best[0]:
            if len(word) < len(words[best[1]]):
                best[1] = words.index(word)
    
    return best[1]
