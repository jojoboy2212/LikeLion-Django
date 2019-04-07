from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

wordlist=[]
d={}
wordlen = 0
def result(request):
    
    text = request.GET['fulltext']
    wordlist = text.split()
    wordlen = len(wordlist)
    word = {}
    wordcount={}

    for words in wordlist:
        if words in wordcount:
            wordcount[words] += 1
        else:
            wordcount[words] = 1
    
    return render(request, 'result.html', {
        'text':text,
        'word':word,
        'wordlen':wordlen,
        'wordcount':wordcount.items,
    })