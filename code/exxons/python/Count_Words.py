import string
f = open('captain_peabody.txt', encoding = "utf8") 

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
contents = f.read()

def format_text(x):
    new_format = contents.lower()
    new_format = new_format.replace("\n", " ")
    for each in string.punctuation:
        new_format = new_format.replace(each, "")
    return new_format


def words(x):
    new_contents = format_text(contents)
    new_contents = new_contents.split(" ")
    return new_contents

def unique(x):
    new_contents = words(contents)
    new_contents = set(new_contents)
    original = set(contents)
    stopwords_set  = set(stopwords)
    new_contents = new_contents | original
    new_contents = new_contents - stopwords_set
    new_contents = list(new_contents)
    new_contents =  [each for each in new_contents if each != ""]
    return new_contents

unique_words = unique(contents)
counts = [1 for each in unique_words]

how_many = dict(zip(unique_words, counts))

def count_words(x):
    check = words(contents)
    for i in check:
        if i in how_many:
            value = how_many[i]
            value += 1
            how_many[i] = value
    return how_many

how_many = count_words(contents)

top_words = list(how_many.items())
top_words.sort(key=lambda tup: tup[1], reverse=True) 
print(top_words[:10])
for i in range(min(10, len(top_words))):
    print(top_words[i])