# Proyecto curso 2

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def strip_punctuation(string):
    for item in punctuation_chars:
        string = string.replace(item, "")
    return string

def get_pos(string):
    count = 0
    string_lst = string.split()
    for word in string_lst :
        word = strip_punctuation(word).lower()
        if word not in positive_words:
            count = count
        else:
            count = count + 1  
    return count

def get_neg(string):
    count = 0
    string_lst = string.split()
    for word in string_lst :
        word = strip_punctuation(word).lower()
        if word not in negative_words:
            count = count
        else:
            count = count + 1  
    return count

twitterfile = open("project_twitter_data.csv", "r")
twitterfile_d = open("resulting_data.csv", "w")
b_words = 0
p_words = 0
n_rtw = 0
n_rpl = 0
twitterfile_d.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
for line in twitterfile:
    line_lst = line.split(",")
    tweet = line_lst[0]
    if tweet == "tweet_text":
        continue
    b_words = get_neg(tweet)
    p_words = get_pos(tweet)
    n_score = p_words - b_words
    n_rtw = line_lst[1]
    n_rpl = line_lst[2]
    n_rpl = n_rpl.strip("\n")
    line_basic = '{},{},{},{},{}'.format(n_rtw,n_rpl,p_words,b_words,n_score)
    twitterfile_d.write(line_basic+'\n')

twitterfile_d.close()
twitterfile.close()


twitterfile_d = open("resulting_data.csv", "r")
for line in twitterfile_d:
    for line in twitterfile_d:
        print(line)

twitterfile_d.close()