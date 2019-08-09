print('\n')
user_word = input('which word would you like to check? ')
print('\n')
reversed_word_list = []
ordered_word_list = []



def check_anagram(user_word): 
    lower_case = (user_word.lower())
    #return (lower_case)
    
    no_space_string = (lower_case.replace(' ',''))
    
    
    non_arranged_word = (no_space_string)
    arranged_word = sorted(non_arranged_word)
    return ordered_word_list.append(arranged_word)
    #ordered_word_list.append(arranged_word)


(check_anagram(user_word))


def check_palindrome(user_word):
    user_word = user_word[::-1]
    reversed_word_list.append(user_word)
    return (user_word)




#user_word = user_word


(check_palindrome(user_word))


if user_word == reversed_word_list[0]:
    print(f'{user_word} is a palindrome!')

if user_word != reversed_word_list[0]:
        print(f'{user_word} is not a palindrome')   

    
    
    
print('\n\n\t--- Now to see if you can find an anagram for your word ---\n\n')
# print('\n')
# print('\n'
print(f'your original word was \'{user_word}\'')

(check_anagram(user_word))
print('\n')




user_word2 = input('Enter your second word: ' )
print('\n')

(check_anagram(user_word2))
    

if ordered_word_list[0] == ordered_word_list[2]:
    print(f'yes \'{user_word}\' and \'{user_word2}\' are anagrams')
    
if ordered_word_list[0] != ordered_word_list[2]:
    print(f'no \'{user_word}\' and \'{user_word2}\' are  not anagrams')
