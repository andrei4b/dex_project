def valid_sol(w1,w2):
    prefixes = ['re', 'de', 'co', 'pre', 'in', 'pro', 'di', 'ca', 'cu', 
    'ba', 'des', 'al', 'bi', 'mi', 'ta', 'tri', 'ex', 'ar', 'st', 'anti', 
    'para', 'im', 'per', 'ci', 'mono', 'ce', 'că', 'la', 'si', 'dis', 'mă', 
    'poli', 'or', 'mu', 'fi', 'ga', 'cur', 'ha', 'sur', 'col', 
    'ad', 'no', 'tele', 'bă', 'fa', 'ter', 'aero', 'să', 'pu', 'na', 'va', 
    'inter', 'câr', 'ti', 'dec', 'for', 'sta', 'bur', 'șu', 'uni', 
    'peri', 'pal', 'ap', 'bor', 'pan', 'ana', 'deca', 'supra', 'sal', 'hi', 
    'șo', 'și', 'sil', 'tal', 'mus', 'neo', 'op', 'ante', 'cop', 'post', 'ser', 
    'mol', 'sin', 'bal', 'za', 'ni', 'ho', 'pic', 'mega', 'hă', 'mas', 'înde', 'prea', 
    'hidro', 'cont', 'tar', 'por', 'pis', 'sul', 'super', 'băl', 'he', 'cam', 'meta', 
    'deci', 'ai', 'iz', 'acu', 'hâr', 'pot', 'cel', 'et', 'cea', 'din', 'fan', 'uș', 
    'but', 'reo', 'pol', 'sec', 'rad', 'bon', 'moto', 'tor', 'exa', 'fon', 'lip']

    sufixes = ['re', 'tor', 'or', 'ic', 'ie', 'ar', 'ist', 'că', 'aș', 
    'ură', 'al', 'ală', 'ui', 'el', 'iu', 'iță', 'et', 'ier', 'tiv', 
    'ta', 'dă', 'in', 'ian', 'ci', 'mă', 'tic', 'abil', 'ia', 'ni', 
    'oare', 'eu', 'na', 'nat', 'st', 'ol', 'tar', 'să', 'rit', 'en', 
    'ti', 'la', 'atic', 'ca', 'uș', 'ion', 'bă', 'eră', 'și', 
    'da', 'fon', 'ter', 'ura', 'graf', 'tină', 'nare', 'ce', 'fă', 'va', 
    'nit', 'pa', 'ei', 'za', 'ut', 'lar', 'urat', 'urare', 'cat', 'di', 'tal', 
    'care', 'oară', 'mat', 'ai', 'orie', 'ir', 'die', 'dină', 'ga', 'cel', 'ța', 
    'ici', 'ba', 'cit', 'un', 'tui', 'dare', 'iac', 'scop', 'tura', 'țel', 'lat', 
    'niu', 'tos', 'logic', 'pune', 'pare', 'sor', 'sat', 'logie', 'de', 'țar', 
    'fer', 'inic', 'bie', 'var', 'etic', 'pus', 'ler', 'cea', 'tip', 'dat', 
    'ral', 'aci', 'tea', 'for', 'iar', 'fonie', 'rar', 'ex', 'tist', 'zare', 
    'pan', 'liță', 'rină', 'ament', 'bi', 'im', 'mer', 'dan', 'sta']

    if w1 in prefixes:
        return False

    if w2 in sufixes:
        return False

    return True

def solutions(words, each_min_len, full_len):
    """
    2 esential parameters, for min length of partial word, 
    and max length of full word
    """
    #each_min_len = 2
    #full_len = 7

    #list of possible full words 
    full_words = [w for w in words if len(w) == full_len]
    #list of possible partial words
    part_words = [w for w in words if len(w) >= each_min_len and len(w) <= full_len - each_min_len]

    #build solution list
    solution = []
    for w in full_words[::-1]:
        each_max_len = len(w) - each_min_len + 1
        for first_word_len in range(each_min_len, each_max_len):
            w1 = w[:first_word_len]
            w2 = w[first_word_len:]
            if not valid_sol(w1, w2):
                continue
            if w1 in part_words and w2 in part_words:
                solution.append((w1, w2))
    
    solution = solution[::-1]
    
    return solution

def valid(word,words):
    """
        function used to eliminate words with upper first letter, 
        words that contain spaces and duplicate words
    """
    
    if len(word) == 1:
        return False
    
    if len(words) > 0:
        if word == words[-1]:
            return False

    if ' ' in word:
        return False

    if word[0].isupper():
        return False

    return True

def create_word_list():
    #create word list
    words = []
    invalid_words = 0
    infile = open('dex09.txt', 'r')
    for line in infile:
        word = line[:-1]
        if not valid(word,words):
            invalid_words+=1
            continue    
        words.append(word)  
    infile.close()

    #sort it 
    words.sort(key = len)

    #write it to outfile 
    outfile = open('mydex.txt', 'w')
    for w in words:
        outfile.write(w + '\n')
    outfile.close()

    print("cuvinte invalide: " + str(invalid_words))

    return words

def palindromes(words):
    """
        identify and write palindroms
    """
    palindromes_f = open('palindromes.txt', 'w')
    for w in words:
        if(w == w[::-1]):
            palindromes_f.write(w + '\n')
    palindromes_f.close()

def reversibles(words):
    reversibles = []
    reversibles_f = open('reversibles.txt', 'w')
    for w in words:
        if w[::-1] in words and w[::-1] not in reversibles:
            reversibles.append(w)
            print(w + ' <--> ' + w[::-1])
            reversibles_f.write(w + ' <--> ' + w[::-1] + '\n')
    reversibles_f.close()
    return reversibles

words = create_word_list()

# mydex = open('mydex.txt', 'r')
# n = 0
# words = []
# for line in mydex:
#         word = line[:-1]    
#         words.append(word)  
#         n += 1
# mydex.close()
# print(str(n) + ' words')

solution = []
for j in range(4,11):
    solution += solutions(words,2,j)
    print(str(j) + 'finished')

solution.sort(key = lambda x: x[0])

#write to file
outfile2 = open('solutii.txt', 'w')
for s in solution:
    outfile2.write(s[0] + ' + ' + s[1] + '\n')
outfile2.close()



# dict1 = {}
# dict2 = {}
# for j in range(4,10):
#     solution = solutions(words,2,j)
    
#     for s in solution:
#         if s[0] in dict1:
#             dict1[s[0]] += 1
#         else:
#             dict1[s[0]] = 1

#         if s[1] in dict2:
#             dict2[s[1]] += 1
#         else:
#             dict2[s[1]] = 1

# statistics = open('statistics2.txt', 'w')

# statistics.write("first word:" + '\n')
# for pair in sorted(dict1.items(), key = lambda x: x[1], reverse=True):
#     statistics.write(str(pair) + '\n')

# statistics.write("second word:" + '\n')  
# for pair in sorted(dict2.items(), key = lambda x: x[1], reverse=True):
#     statistics.write(str(pair) + '\n')  

# statistics.close()

#palindromes(words)
#reversibles(words)