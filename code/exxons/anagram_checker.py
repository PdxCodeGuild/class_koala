
ordered_word_list = []

def check_anagram(user_word): 
    lower_case = (user_word.lower())
    #return (lower_case)
    
    no_space_string = (lower_case.replace(' ',''))
    
    
    non_arranged_word = (no_space_string)
    arranged_word = sorted(non_arranged_word)
    return ordered_word_list.append(arranged_word)
    #ordered_word_list.append(arranged_word)



user_word = input('Enter your first word: ' )

(check_anagram(user_word))





user_word2 = input('Enter your second word: ' )

(check_anagram(user_word2))
    

if ordered_word_list[0] == ordered_word_list[1]:
    print(f'yes \'{user_word}\' and \'{user_word2}\' are anagrams')
    
if ordered_word_list[0] != ordered_word_list[1]:
    print(f'no \'{user_word}\' and \'{user_word2}\' are  not anagrams')
        