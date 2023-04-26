
import os
import sys
import time
import requests

#googleapis
googleapisToken = "APJWN8d_akrTxpNEJiw499RPvFKeaiU2Ij4BxzVqFm2IvmUIKI61qM7Z_hLR-aAuGQi0aJeFqiK9zYdrguSs0X_TVksiLqcQJeEE98VhgFaLhsEZXT2jln80_tqI1DqPEOaJ3QrWmcEv2TtD_SZaJ5QOEFLfIo3H1yMA3PIJG1zq6PLDMmNUQiJaz2_Xo2L98zaIKEKe6kI_"

googleapisHeaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
    'Accept': '*/*',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://www.fishtank.live/',
    'X-Client-Version': 'Firefox/JsCore/9.15.0/FirebaseCore-web',
    'X-Firebase-gmpid': '1:38037891221:web:fa5237486b8256d700d39c',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.fishtank.live',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site'
}

while True:
    #get authToken
    params = {
        'key': "AIzaSyBOOpV21k6o3cJc56-4uRNb0jDMzIxShMY",
    }
    
    data = {
        'grant_type': "refresh_token",
        'refresh_token': googleapisToken,
    }
    
    response = requests.post('https://securetoken.googleapis.com/v1/token', params=params, headers=googleapisHeaders, data=data)
    
    data = response.json()
    authToken = data['access_token']
    
    fishtankHeaders = {
        'User-Agent': 'SAM HYDE LOVES CHILDREN',
        'Accept': '*/*',
        'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': 'https://www.fishtank.live/',
        'AuthToken': authToken,
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }
    
    #fishtank
    response = requests.get('https://www.fishtank.live/api/live-streams', headers=fishtankHeaders)
    
    data = response.json()
    data = data['liveStreams']

    for camera in data:
        camera = camera['url']
        baseURL = "https://iframe.cloudflarestream.com/{}?preload=metadata&autoplay=false&controls=true".format(camera)
        print(baseURL)

    #time.sleep(3600) #timer
    sys.exit()