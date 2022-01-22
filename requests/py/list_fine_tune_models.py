import openai
from key import key

openai.api_key = key
print(openai.FineTune.list())
