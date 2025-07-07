from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Welcome to the TextUtils Home Page!')
    return render(request, 'home.html')

def about(request):
    return HttpResponse('This is the About Page of TextUtils. Here you can find information about the application and its features.')

def contact(request):
    return HttpResponse('This is the Contact Page of TextUtils. You can reach us at')

def removepunc(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Please select the Remove Punctuation option.")
    
def capitalizefirst(request):
    djtext = request.GET.get('text', 'default')
    capitalizefirst = request.GET.get('capitalizefirst', 'off')

    if capitalizefirst == 'on':
        analyzed = ""
        for word in djtext.split():
            analyzed += word.capitalize() + " "
        params = {'purpose': 'Capitalized First Letter', 'analyzed_text': analyzed.strip()}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Please select the Capitalize First Letter option.")

def newlineremove(request):
    djtext = request.GET.get('text', 'default')
    newlineremove = request.GET.get('newlineremove', 'off')

    if newlineremove == 'on':
        analyzed = djtext.replace('\n', '')
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Please select the Remove New Lines option.")
    
def spaceremove(request):
    djtext = request.GET.get('text', 'default')
    spaceremove = request.GET.get('spaceremove', 'off')

    if spaceremove == 'on':
        analyzed = " ".join(djtext.split())
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Please select the Remove Extra Spaces option.")
    
def charcount(request):
    djtext = request.GET.get('text', 'default')
    charcount = request.GET.get('charcount', 'off')

    if charcount == 'on':
        count = len(djtext)
        params = {'purpose': 'Character Count', 'analyzed_text': f'The number of characters is: {count}'}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Please select the Character Count option.")


def analyze(request):
    # Get the text from the request
    djtext = request.GET.get('text', 'default')

    # Get the checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremove = request.GET.get('newlineremove', 'off')
    spaceremove = request.GET.get('spaceremove', 'off')
    charcount = request.GET.get('charcount', 'off')
    
    if removepunc == 'on':
        # Remove punctuations
        analyzed = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        # Prepare the parameters for rendering    
        params = {'purpose': 'Analyze Text', 'analyzed_text': analyzed}
        # Render the analyze.html template with the parameters
        return render(request, 'analyze.html', params)
    elif fullcaps == 'on':
        # Convert to uppercase
        analyzed = djtext.upper()
        params = {'purpose': 'Convert to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif newlineremove == 'on':
        # Remove new lines
        analyzed = djtext.replace('\n', '').replace('\r', '')
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif spaceremove == 'on':
        # Remove extra spaces
        analyzed = ' '.join(djtext.split())
        params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif charcount == 'on':
        # Count characters
        count = len(djtext)
        analyzed = f'The number of characters is: {count}'
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    else:
        return render(request, 'analyze.html', {'purpose': 'No Operation Selected', 'analyzed_text': 'Please select at least one operation and try again.'})