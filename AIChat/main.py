# To retrieve the Open AI key from System Environment Variable (SEV). This is an in-built python module. So pip install not required.
import os

# Pre Requisite to import : install open ai package through pip install
import openai

# Prerequisite -> Save the Variable name & Variable Value under SEV
# value pair Retrieve api key from system variables from the system. This makes it easy to share code with others
openai.api_key = os.getenv("OPENAI_API_KEY")

# Warm up section before we start invoking the API
username = input(":: Hi there, I am here to assist. What is your name ? >> ")
print ("Hi "+ username + "..Let's get strated")

def get_answers():

    #Build the payload
    messages=[]
    message=input(':: What would you like to know ? >>  ')
    messages.append({
        "role":"user",
        "content": message})

    #Query Open AI Engine with the payload as input and get response
    response=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
    )

    #Full JSon message is not very useful for the user. Hence extract content from the JSON
    reply = response["choices"][0]["message"]["content"]
    print(reply)

continue_chat="Yes"

while continue_chat == "Yes":
    get_answers()
    terminate_session = input("To terminate chat, type T, to continue type C >>")
    if terminate_session.lower()== 't' :
        continue_chat == "No"
        break
        
print("Thank you "+username+ " for trying the chat facility. Have a nice rest of the day !!")
