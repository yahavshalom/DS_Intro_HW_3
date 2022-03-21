## Yahav Shalom
## 207650052

#QA 1
def read_line(n, file):
    if type(n) != int:
        return "invalid input detected"
    if file != 'ex3_text.txt':
        return "file not found"
    count = 0
    file = open('ex3_text.txt')  ## read the file
    new_file = list()  ## convert the file to list
    for line in file: ## Read line-by-line
        count+= 1
        line = line.strip()
        new_file.append(line.strip())
    if n > count: ## if there isnt that number line
        return "line " + str(n) + " doesn't exist"
    else: ## if none above happens
        return str(new_file[n-1])


def longest_words(file):
    if file != 'ex3_text.txt': ## if the file name incorrect
        return "file not found"
    file = open('C:\\Users\\yahav\\.spyder-py3\\ex3_text.txt')  ## read the file
    new_file = list()
    final_list = list()
    sort_list = list()
    for line in file: ## Read line-by-line
        word = line.split()
        for new_word in word: ## read word-by-word
           new_file.append(new_word)
    for dot in new_file: ## separate the dot from the word
        if dot.startswith("-") == False:
            words = dot.split(".")
        for new in words:
            final_list.append(new)
    sort_word= sorted(final_list, key = len, reverse= True) ## sorted by the longest first
    sort_list = sort_word[:5]
    return (sort_list) ## return the 5th longest words

    


