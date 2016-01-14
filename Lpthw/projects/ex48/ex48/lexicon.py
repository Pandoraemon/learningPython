lexicon = [('direction','north'), ('direction','south'), ('direction','west'),
	   ('direction','east'),('verb','go'), ('verb','kill'), ('verb','eat'),
	   ('stop','the'), ('stop','in'), ('stop', 'of'),('noun','bear'), 
	   ('noun','princess')]

def scan(setence):
    res = []
    words = setence.split()
    for word in words:
        flag = 0
        try:
           res.append(('number', int(word)))
        except ValueError:
            for result in lexicon:
                if word in result:
                    res.append(result)
                    flag = 1
                else:
                    continue
            if flag == 0:
                res.append(('error', word))
    return res
 
