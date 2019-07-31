import string

with open('wizard_of_oz.txt', 'r') as file:
    contents = file.read()
    translator = str.maketrans('', '', string.punctuation)
    no_punctuations = contents.translate(translator)
    no_punctuations = no_punctuations.lower().split()

    STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours',  'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your',   'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she',   "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself','they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who' 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are' 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for',   'with', 'about', 'against', 'between', 'into', 'through', 'during',   'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in','out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once' 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor','not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't',   'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now',  'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn',  "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn',   "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won',"won't", 'wouldn', "wouldn't"]

    words_list = dict()
    for w in no_punctuations:
        if w in words_list:
            words_list[w] = words_list[w] + 1
        else:
            words_list[w] = 1

    for w in STOPWORDS:
        if w in words_list:
            words_list.pop(w)

    words = list(words_list.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to   smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or allof them, whichever is smaller
        print(words[i])