from openai import OpenAI

openai_api_base = "http://10.194.176.195/v1"


client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="EMPTY",
    base_url=openai_api_base,
)
models = client.models.list()
model = models.data[0].id
chat_completion = client.chat.completions.create(
    messages=[{
        "role": "system",
        "content": "You are a helpful assistant."
    }, {
        "role": "user",
        "content": "Who won the world series in 2020?"
    }, {
        "role":
        "assistant",
        "content":
        "The Los Angeles Dodgers won the World Series in 2020."
    }, {
        "role": "user",
        "content": "Where was it played?"
    }],
    model=model,
)

print("Chat completion results:")
print(chat_completion.choices[0].message.content)
