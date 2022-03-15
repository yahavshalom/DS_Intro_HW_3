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
    new_list = list()
    for line in file: ## Read line-by-line
        line = line.strip()
        new_file.append(line.split())      
    for word in new_file: ## read word by word
        longest= " "
        for num in range(len(word)): ## cheack if the word longest then the others
            if len(longest) < len(word[num]):
                longest = word[num]
                new_list.append(longest)
            sort_word= sorted(new_list, key = len, reverse= True) ## sorted by the longest first
    return (sort_word[1:6]) ## return the 5th longest words

    


