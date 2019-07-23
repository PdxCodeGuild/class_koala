# filename: count_words.py
import string

def load(filepath):
    """accepts a text file as input and returns a list of all of the words with newlines, punctuation, etc. all removed"""
    with open("book_of_mormon.txt", "r") as file:
        filename = "book_of_mormon.txt"
        text = file.read().lower().replace("\n", "")
        translator = text.maketrans("", "", string.punctuation)
        text_stripped = text.translate(translator)
        word_list = text_stripped.split(" ")
        return filename, word_list

def count(word_list):
    """accepts a list of words, counts number of times each word appears in text, then returns a dictionary with the word as the key and its respective frequency as the number value"""
    word_dict = {}
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1
    return word_dict

def sort(word_dict):
    """accepts a dictionary, converts to a list of tuples, sorts based on value number, removes all common stopwords, then returns the top ten"""
    stopwords = ['and', 'unto', 'which', 'came', 'come', 'shall', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'youre', 'youve', 'youll', 'youd', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'shes', 'her', 'hers', 'herself', 'it', 'its', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'thatll', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'upon', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'also', 'very', 's', 't', 'can', 'will', 'just', 'don', 'dont', 'should', 'shouldve', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'arent', 'couldn', 'couldnt', 'didn', 'didnt', 'doesn', 'doesnt', 'hadn', 'hadnt', 'hasn', 'hasnt', 'haven', 'havent', 'isn', 'isnt', 'ma', 'mightn', 'mightnt', 'mustn', 'mustnt', 'needn', 'neednt', 'shan', 'shant', 'shouldn', 'shouldnt', 'wasn', 'wasnt', 'weren', 'werent', 'won', 'wont', 'wouldn', 'wouldnt']
    words = list(word_dict.items())
    words.sort(key=lambda tup: tup[1], reverse=True)
    top_ten = []
    for i in range(min(10, len(words))):
        for word, value in words:
            if word in stopwords:
                words.remove((word, value))
        top_ten.append(words[i])
    return top_ten

def pprint(top_ten, filename):
    """accepts the top ten words as input, then prints a user friendly version of the result"""
    print(f"\nTop Ten words in {filename}:")
    print("-" * 36)
    for word in top_ten:
        print(f"{str(word[0])}: {str(word[1])}")
    print("")

# stores function results as variables
filename, word_list = load("book_of_mormon.txt")
word_dict = count(word_list)
top_ten = sort(word_dict)
pprint(top_ten, filename) # calls final function to display results


# BUGS TO BE RESOLVED: "and", "unto" and "which" still being included in results / some words are being conjoined in the first function
