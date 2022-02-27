def Search_Movie_title(value):
    import urllib.request
    import os
    import sys
    import json
    # print(value)
    client_id = '[네이버 dev Id]'
    client_secret = '[네이버 dev Secret]'

    encText = urllib.parse.quote(value)
    url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText+"&display=100"
    ##  &display=10 &start=1 &genre=1
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    # print(rescode)
    if (rescode == 200):
        response_body = response.read().decode('utf-8')
        # print(response_body)
        res = json.loads(response_body)
        res_list = res['items']
        return res_list
    else:
        print("Error code:" + rescode)
        return []