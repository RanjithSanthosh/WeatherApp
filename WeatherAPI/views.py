from django.shortcuts import render
import requests

# Create your views here.
def get_weather(request):
    weatherData = None
    errorData = None
    if request.method == 'POST':
        city = request.POST.get('city') #check
        apiKEY = 'df22019d48f77a6a3316874c33fc3355'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKEY}&units=metric'
        
        response = requests.get(url)
        if response.status_code == 200:
            weatherData = response.json()
        else:
            errorData = "Invalid City Name or Problem in API.."
    return render(request,'index.html',{'weather':weatherData ,'error':errorData})
        