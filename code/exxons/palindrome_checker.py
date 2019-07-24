user_word = input('which word would you like to check? ')

reversed_word_list = []

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


