# import os
# import openai
# import config_api_keys
# openai.api_key = config_api_keys.OPENAI_API_KEY
# from gtts import gTTS
# #this is a Q&A machine learning algorithm using OPEN AI 
# def gpt3_question_and_answer(query):
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=query,
#         temperature=0,
#         max_tokens=100,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0,
#         # stop=["\n"]
#         )

#     if 'choices' in response:
#         if len(response['choices']) >0:
#             gpt_answer = response['choices'][0]['text']
#     else:
#         gpt_answer = 'Opps sorry, you broke the AI algorithm'
    
#     return gpt_answer


# #this is a chat bot conversation query using OPEN AI
# def gpt3_chat_with_ai(query):
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt= query,
#         temperature=0.9,
#         max_tokens=150,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0.6,
#         stop=[" Human:", " AI:"]
#         )

#     if 'choices' in response:
#         if len(response['choices']) >0:
#             gpt_answer = response['choices'][0]['text']
#     else:
#         gpt_answer = 'Opps sorry, you broke the AI algorithm'
    
#     return gpt_answer




# # query = 'What is the name of elon musks mother'
# # print(gpt3_question_and_answer(query))

# query = 'why am I sad?'
# gpt3_text = gpt3_chat_with_ai(query)


# #reproducing the GPT-3 ANSWER IN A VOICE FORMAT
# language = 'en'
# myobj = gTTS(text=gpt3_text, lang=language, slow=False)
# myobj.save("trial.mp3")
# os.system("trial.mp3")