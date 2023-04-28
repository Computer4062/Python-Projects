import openai

API_KEY = open('API KEY', 'r').read()
openai.api_key = API_KEY

log = []

while True:
    message = input(">>")
    if message.lower() == "exit":
        break
    else:
        log.append({"role": "user", "content":message})
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = log
        )

        response = response['choices'][0]['message']['content']

        print("Bot: ")
        for sentence in response.split('.'):
            print(sentence)

        log.append({"role":"assistant", "content":response})
