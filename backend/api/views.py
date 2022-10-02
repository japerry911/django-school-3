import json

from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    body = request.body

    data = {}
    try:
        data = json.loads(body)
    except:
        pass

    data["params"] = dict(request.GET)
    data["headers"] = request.headers

    print(data)

    return JsonResponse({
        "message": "Hi There, Django API response..."
    })