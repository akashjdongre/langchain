from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
model = init_chat_model("claude-sonnet-4-6")

info_txt = "My name is Akash Dongre & my Email id is akashjdongre@gmail.com." \
    "My age is 35 years, i am Python Developer and working in Saregama India Ltd."\
    " My friends are Nikhil,Sanket and Amit Varma."

res = model.invoke(f"Please give me Name, Email id, Age, Profession and Friends name from below text : {info_txt}")
# print(res.content)

#-------------------------------------------------------------------# 

from modules.structure import LLMResponseStructure, MovieResponseStructure, MoviesResponseStructure

llmStructOutput = model.with_structured_output(LLMResponseStructure)

llm_response = llmStructOutput.invoke(f"Please give me name, email_id, age, rofession and best_friends name from below text : {info_txt}")
print(llm_response.model_dump())

#-------------------------------------------------------------------#

movie_info_txt = "Give me one Hollywood horror movie details"
movieStructOutput = model.with_structured_output(MovieResponseStructure)
movie_response = movieStructOutput.invoke(f"{movie_info_txt}")
print(movie_response.model_dump())
print(movie_response.title)

#-------------------------------------------------------------------#

movies_info_txt = "Give me 3 Hollywood Thriller movie details"
movieStructOutput = model.with_structured_output(MoviesResponseStructure)
movies_response = movieStructOutput.invoke(f"{movies_info_txt}")
print(movies_response.model_dump())
print(movies_response.movies[1])
