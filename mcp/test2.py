from openai import OpenAI

openai_api_base = "http://vllm:8001/v1"


client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="EMPTY",
    base_url=openai_api_base,
)
models = client.models.list()
model = models.data[0].id
print(model)