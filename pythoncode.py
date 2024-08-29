def minion_game(string):
    vowels = 'AEIOU'
    kevinscore = 0
    stuartscore = 0
    print(len(string))
    for index, char in enumerate(string):
        if char in vowels:
            # Calculate how many substrings Kevin can form starting with this vowel
            kevinscore += len(string) - index
        else:
            # Calculate how many substrings Stuart can form starting with this consonant
            stuartscore += len(string) - index

    # Compare scores and print the winner
    if stuartscore > kevinscore:
        print(f"Stuart {stuartscore}")  
    elif kevinscore > stuartscore:
        print(f"Kevin {kevinscore}")  
    else:
        print("Draw")

if __name__ == '__main__':
    s = input("Please enter a string: ")
    minion_game(s)
