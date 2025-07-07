from django.http import HttpResponse


def index(request):
    with open('F:\jamil\python.py\Django\mysite\mysite\One.txt', 'r', encoding='utf-8') as file:
        file_content = file.read()
    return HttpResponse(file_content)

def about(request):
    return HttpResponse("This is the about page. <h1>About Us</h1><p>Welcome to our website!</p>")

def contact(request):
    return HttpResponse("This is the contact page. <h6>Contact Us</h6><p>Feel free to reach out!</p> <a href='https://www.google.com'>Google</a> <img src='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png' alt='Google Logo'>")