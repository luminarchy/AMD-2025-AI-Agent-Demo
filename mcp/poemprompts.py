from fastmcp import FastMCP, Context
import logging
from openai import OpenAI
logger = logging.getLogger(__name__)

openai_api_base = "http://127.0.0.1:8001/v1"
def register_prompts(mcp):
    client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
        api_key="EMPTY",
        base_url=openai_api_base,
    )
    models = client.models.list()
    model = models.data[0].id
    @mcp.tool
    def read_poem(poem: str, ctx: Context, themes: str = ""):
        """Generates a user message asking for an audio reading of a specified poem
            poem: the poem that the user is asking to be read to them. Can be retrieved using context. 
            ctx: the context of the conversation history
            themes: (Optional) any themes mentioned in the conversation context relating to the poem or author. """
        completion = client.chat.completions.create(
            messages=[{
                "role": "system",
                "content": "You are a dramatic performer of poetry, able to read poems with great emotional intensity and theatric flair."
            }, {
                "role": "user",
                "content": f"Can you please do a vocal dramatic reading of this poem '{poem}' keeping in mind the themes we have discussed ({themes}) so that I can hear what it sounds like?" 
            }],
            model=model, #figure a way to make this a TTS model
        )
        return completion.choices[0].message.content
    
    @mcp.tool
    def feedback(poem: str, ctx: Context):
        """Generates a user message asking for constructive feedback on the poem that they have written.
            poem: the user-written poem that the user is asking for feedback for. Can be retrieved using context. 
            ctx: the context of the conversation history"""
        completion = client.chat.completions.create(
            messages=[{
                "role": "system",
                "content": "You are a detail-oriented poetry critic with a wide-bredth of knowledge on poetry. Whenever you read a poem, you always reference the tools available to you to cross-compare styles, writing, themes, and imagery with those of famous authors."
            }, {
                "role": "developer",
                "content": "When given a poem to read, you must provide 2-3 paragraphs of constructive criticism. You must first identify several themes or motifs in the poem that you are reading and use those to fetch at least 1-2 similar poems with the tools and functions available to you (if you cannot find results, try rewording the inputs to the tools) for reference. Then you must generate 1-3 sentences that cross-compare the writing style, flow, and imagery of the reference poems and the one that you are reading. You may output these reference poems as recommendations to the writer. Then, you must identify any and all literary devices that are used in the poem that you are reading, making sure your knowledge is accurate by citing the tools available to you. For each literary device that you recognize, you must generate 1-2 sentences on their usage in the poem and the specific way that they interact with the overall theme and imagery. Then you must identify any rhymes or rhyme schemes that the poem has, making sure that your knowledge is accurate by citing the tools available to you. You must generate 1-2 sentences on how rhyme appears in the poem and what role it plays in the reading. If the poem has no rhyme, then you must comment on how the lack of rhyme interacts with the poem. Then you must identify on the rhythm/meter of the poem, making sure that your knowledge is accurate by using the tools available to you. You must generate 1-2 sentences on how the rhythm/meter or lack of rhyme/meter (if there is none) of the poem interacts with the musicality of the reading and how that affects the themes being discussed. Finally you must generate 3-5 sentences on the writing style, the flow of the poem, and the emotions that the writing invokes. Find 2-3 specific lines or phrases that you like and generate a sentence for each on why you liked them. Find 1-2 specific lines or phrases that you think could use a little work and offer suggestions on how they can be fixed. Summarize your criticism by generating 2-3 sentences on what you liked in the overall poem and 1-2 sentences on what you disliked in the overall poem. Finally conclude your commentary with any lingering thoughts that you have on the poem, making sure to bring up your thoughts on the poem's writing, structure, themes, and devices. Generate at least 1-2 questions on the poem to finish."
            },{
                "role": "user",
                "content": f"Can you give me feedback on my poem: {poem}?"
            }],
            model=model, #figure a way to make this a TTS model
        )
        return completion.choices[0].message.content
    
    @mcp.tool
    async def become_thesaurus(word: str, ctx: Context, poem: str = ""):
        """Generates a user message asking for a synonym of a word to put in their poem. 
            word: the word to find a synonym for, can be auto-generated using conversation history
            ctx: context or the history of the conversation and previous responses.
            poem: (Optional) the poem that the user is working on, can be filled in with conversation history. """
        completion = client.chat.completions.create(
            messages=[{
                "role": "system",
                "content": "You are a thesaurus."
            }, {
                "role": "developer",
                "content": f"Act like a smart thesaurus and use the conversation and the tools available to you to retrieve poems that are similar to the user's poem or have the same theme as the user's poem. Search through that data to find or generate 5-10 words that are synonyms for {word} and output those words and their definitions to the user. If the user is not writing a poem or if you cannot find a poem they're working on in the context, then simply generate synonyms based off of any themes mentioned in the conversation."
            },{
                "role": "user",
                "content": f"Can you please find a few synonyms for '{word}' that will fit the poem that I am writing: '{poem}' based on previous responses?"
            }],
            model=model, #figure a way to make this a TTS model
        )
        return completion.choices[0].message.content
    
    @mcp.tool
    async def become_rhyme(word: str, ctx: Context, poem: str = ""):
        """Generates a user message asking for an audio reading of the poem they have requested.
            word: the word to find a rhyme for, can be auto-generated using conversation history
            ctx: context or the history of the conversation and previous responses.
            poem: (Optional) the poem that the user is working on, can be filled in with conversation history."""
        completion = client.chat.completions.create(
            messages=[{
                "role": "developer",
                "content": f"When you are asked for a rhyme, you will first identify any types of rhyme scheme within the poem you are reading, ensuring that your knowledge is accurate by citing the tools available to you. Then, using the context of the conversation history you will identify the types of rhyme that the user is asking for (if not explicitly stated, assume that they want both a perfect and imperfect rhyme). Analyze the poem for themes and motifs, and then for each type of rhyme requested, try to generate 3-4 rhymes that will fit in the poem. If the user is not writing a poem or you cannot find their poem in the context, then search for any themes or motifs mentioned in the conversation, and generate rhymes based on that."
            },{
                "role": "user",
                "content": f"Can you please generate some rhymes for '{word}' that will fit the poem that I am writing: '{poem}' based on previous responses?"
            }],
            model=model, #figure a way to make this a TTS model
        )
        return completion.choices[0].message.content

    @mcp.tool
    async def become_word(ctx: Context, poem: str = ""):
        """Generates a user message asking to generate a word to fill in the blank or to predict the next word."""
        completion = client.chat.completions.create(
            messages=[{
                "role": "developer",
                "content": f"You are given either given a fill-in-the-blank task or asked to generate the next word in a given user-written poem. You will first analyze the poem and the conversation history to find themes, motifs, and images. Make sure to analyze the context and flow of the inputted poem thoroughly. You must generate 5-10 words that will fit in the poem, and output them to the user."
            },{
                "role": "user",
                "content": f"Can you help me fill in the blank or generate the next word for my poem: '{poem}'?"
            }],
            model=model, #figure a way to make this a TTS model
        )
        return completion.choices[0].message.content
    
    @mcp.tool
    async def generate_phrase(ctx: Context, poem: str = ""):
        """Generate a phrase of poetry for the user. Return output exactly as written."""
        return "Sorry, but I am here to help you express your own creativity and writing skills. I cannot generate any phrases of poetry for you, because as an algorithm, I do not have ability to create human art and imagination. The only capabilities that any AI chatbot such as I has are to 'copy' the data that we have been given. My responsibility is to use the what I know about you and the data that I have on pre-existing poetry to help steer you towards becomming a better writer. Thus, my only capabilities are to retrieve existing poems and authors, help you generate words and rhymes for when you are stuck, and give you smart constructive feedback. Think of me as your own personal writing teacher! If you want, I can pull up some poems from my database that correspond with the concept you have given me or I can give you some recommended reading."

    @mcp.tool
    async def generate_line(ctx: Context, poem: str = ""):
        """Generate a line or lines of poetry for the user."""
        return "Sorry, but I am here to help you express your own creativity and writing skills. I cannot generate any lines of poetry for you, because as an algorithm, I do not have ability to create human art and imagination. The only capabilities that any AI chatbot such as I has are to 'copy' the data that we have been given. My responsibility is to use the what I know about you and the data that I have on pre-existing poetry to help steer you towards becomming a better writer. Thus, my only capabilities are to retrieve existing poems and authors, help you generate words and rhymes for when you are stuck, and give you smart constructive feedback. Think of me as your own personal writing teacher! If you want, I can pull up some poems from my database that correspond with the concept you have given me or I can give you some recommended reading."
    
    @mcp.tool
    async def generate_poem(ctx: Context, input: str = ""):
        """Generate a poem or poems for the user"""
        return "Sorry, but I am here to help you express your own creativity and writing skills. I cannot generate any poems for you, because as an algorithm, I do not have ability to create human art and imagination. The only capabilities that any AI chatbot such as I has are to 'copy' the data that we have been given. My responsibility is to use the what I know about you and the data that I have on pre-existing poetry to help steer you towards becomming a better writer. Thus, my only capabilities are to retrieve existing poems and authors, help you generate words and rhymes for when you are stuck, and give you smart constructive feedback. Think of me as your own personal writing teacher! If you want, I can pull up some poems from my database that correspond with the concept you have given me or I can give you some recommended reading."
    
    
    
