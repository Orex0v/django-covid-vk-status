from django.shortcuts import render
from time import sleep
from pip._vendor import requests


# Create your views here.


def index(request):
    if request.method == "POST":
        token = request.POST.get('token', '')
        app_id = "7362610"
        method = "users.setCovidStatus"
        format = "json&v=5.103"
        replay = int(request.POST.get('replay', ''))
        time_sleep = 0.5
        count = 0
        statis_id_list=[1, 2, 3, 4, 5, 10, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
        while replay > count:
            for status_id in statis_id_list:
                url = f"https://api.vk.com/method/users.setCovidStatus?api_id={app_id}" \
                      f"&method={method}" \
                      f"&format={format}" \
                      f"&status_id={status_id}" \
                      f"&access_token={token}"
                get = requests.post(url)
                data = get.json()
                try:  # Проверяем токен
                    if data["response"]:
                        pass
                except:
                    return render(request, "error.html")
                sleep(time_sleep)
                count += 1
            return render(request, "success.html")
    return render(request, "index.html")
