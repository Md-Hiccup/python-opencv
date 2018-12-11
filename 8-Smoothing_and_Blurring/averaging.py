# import numpy as np
# import argparse
# import cv2

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True,
# help = "Path to the image")
# args = vars(ap.parse_args())

# image = cv2.imread(args["image"])
# cv2.imshow("Original", image)

# #+17123557451
# +918884724549







# way2sms
# import requests
# import json

# apiKey = '2MA1RRB5P8QLDMOJ2MRLVCHWE305BYSG'
# secretKey = '1ESZ4QAAKBHP9RRW'
# textMessage = "Hey Machaa how are you"
# senderId = 'jack'

# URL = 'http://www.way2sms.com/api/v1/sendCampaign'

# # get request
# def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
#     req_params = {
#     'apikey':apiKey,
#     'secret':secretKey,
#     'usetype':'stage',
#     'phone': '7753052819',
#     'message': 'textMessage',
#     'senderid':'senderId'
#     }
    
#     ret = requests.post(reqUrl, req_params)
#     return ret

# # get response
# response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile', 'active-sender-id', 'message-text' )
# """
# Note:-
#     you must provide apikey, secretkey, usetype, mobile, senderid and message values
#     and then requst to api
# """
# # print response if you want
# print(response.text)






# Download the helper library from https://www.twilio.com/docs/python/install
# from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# account_sid = 'AC03e73b9372b0d45e483f0463127cf187'
# auth_token = '37fc8212ea1ed29da38731a95de93810'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#                     body="Hey Man, Just For testing Purpose",
#                     from_='+918861691118',
#                     to='+17123557451'
#                 )

# print(message.sid)
