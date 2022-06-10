import requests
import json


endpoint = 'https://emmapythonimageanalyzer.cognitiveservices.azure.com/vision/v3.2/'
region = 'southafricanorth'
key_path = "../api_keys.txt"
SUBSCRIPTION_KEY = open(key_path, "rb").read()
print('API keys: ', SUBSCRIPTION_KEY)
# Add the name of the function you want to call to the address
address = "{}analyze".format(endpoint)

# According to the documentation for the analyze image function
# There are three optional parameters: language, details & visualFeatures
parameters = {'visualFeatures': 'Description,Color',
              'language': 'en'}

# Open the image file to get a file object containing the image to analyze
image_path = "./TestImages/HouseArea.png"
image_data = open(image_path, "rb").read()

# According to the documentation for the analyze image function
# we need to specify the subscription key and the content type
# in the HTTP header. Content-Type is application/octet-stream when you pass in a image directly
headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

# According to the documentation for the analyze image function
# we use HTTP POST to call this function
response = requests.post(address, headers=headers,
                         params=parameters, data=image_data)

# Raise an exception if the call returns an error code
response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(json.dumps(results))
