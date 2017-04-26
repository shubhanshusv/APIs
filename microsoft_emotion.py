import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, json
import codecs
from pprint import pprint
 
n = int(input())


for i in range(n):

    pic = input()

    headers = {
        # Request headers. Replace the placeholder key below with your subscription key.
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '77d8471d26184cde9fcfa9a411d5cad5',
    }

    params = json.dumps({'url': pic })

    # Replace the example URL below with the URL of the image you want to analyze.

    class JSONObject:
        def __init__(self, d):
            self.__dict__ = d

    try:
        reader = codecs.getreader("utf-8")
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s", params, headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        #print(data)
        conn.close()
        
        result = json.loads(data)
        
        for i in result:
            em = [0,0,0,0,0,0,0,0]
            
            em[0] = float(i.get('scores').get('sadness'))
            em[1] = float(i.get('scores').get('neutral'))
            em[2] = float(i.get('scores').get('contempt'))
            em[3] = float(i.get('scores').get('disgust'))
            em[4] = float(i.get('scores').get('anger'))
            em[5] = float(i.get('scores').get('surprise'))
            em[6] = float(i.get('scores').get('fear'))
            em[7] = float(i.get('scores').get('happiness'))
            
            maxi = max(em)
            
            if maxi is em[0]:
                print('sadness')
            elif maxi is em[1]:
                print('neutral')
            elif maxi is em[2]:
                print('contempt')
            elif maxi is em[3]:
                print('disgust')
            elif maxi is em[4]:
                print('anger')
            elif maxi is em[5]:
                print('surprise')
            elif maxi is em[6]:
                print('fear')
            elif maxi is em[7]:
                print('happiness')

            
    except Exception as e:
        print(e.args)