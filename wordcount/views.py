from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html') #,{'hifucks':'anaconda bitch'})

def about(request):
    return render(request,'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split() # splits string into list of words divided by spaces
    worddic = {}
    for word in wordlist:
        if word in worddic:
            # increment word count
            worddic[word] += 1
        else:
            # add word to dictionary
            worddic[word] = 1
    sortedwords = sorted(worddic.items(), key=operator.itemgetter(1), reverse=True)

    numwords = len(wordlist)
    message = ''
    if numwords <= 0:
        message = 'There are no words in your text'
    elif numwords > 1:
        message = 'There are {} words in your text'.format(numwords)
    else:
        message = 'There is 1 word in your text'



    return render(request,'count.html',{'fulltext':fulltext, 'message':message, 'sortedwords':sortedwords })

#def eggs(request):
#    return HttpResponse('over-easy')
