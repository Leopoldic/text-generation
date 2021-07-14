import nltk
import gensim


def clean_text(lower_case):
    punctuations = re.sub(r'\W', ' ', str(lower_case))
    stop_words  = stopwords.words('russian')
    w_num = re.sub('\w*\d\w*', '', lower_case).strip()
    lower_case = re.sub(r'\s+[a-zA-Z]\s+', ' ', lower_case)
    lower_case = re.sub(r'\s+', ' ', lower_case, flags=re.I)
    lower_case = re.sub(r'^b\s+', '', lower_case)
    lower_case = re.sub(r'^b\s+', '', lower_case)
    return lower_case
 
def read_article(text):
    data = text.replace('\n','')
    article = data.split(". ")
    print(article)
    sentences = []

    for sentence in article:
        print(sentence)
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop() 
    
    return sentences

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
 
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
 
    return 1 - cosine_distance(vector1, vector2)
 
def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: #ignore if both are same sentences
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix

def generate_summary(file_name, top_n=5):
    stop_words = stopwords.words('russian')
    summarize_text = []

    sentences =  read_article(text)
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)        

    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sentence[i][1]))


    print("Summarize Text: \n", ". ".join(summarize_text))

def summarize(text):
    gensim_summary = gensim.summarization.summarize(text)
    return ' '.join(gensim_summary.split('.')[:2])