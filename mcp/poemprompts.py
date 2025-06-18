from fastmcp import FastMCP, Context

def register_prompts(mcp):
    @mcp.prompt
    def read_user_poem(poem: str):
        """Generates a user message asking for an audio reading of their poem and constructive feedback."""
        return f"Can you please do a vocal dramatic reading of the poem I've written: '{poem}' so that I can hear what it sounds like, and then give me constructive feedback as if this were the first time you were encountering me, my poem, and my writing. Please give me creative, but accurate and correct commentary on the themes, metaphors, imagery, emotions, and language used in the poem. If present, you should additionally tell me on how the rhyme, meter, and rhythm interact with the flow and feel of the writing. In order to be as accurate as possible, you should use any tools available to you to reference existing poetry as a guide for your commentary. If the poem has no title, you should also help me generate a title for the poem, and you should ask me if I want to see some similar poems as inspiration. " 
    
    @mcp.prompt
    def read_db_poem(poem: str, ctx: Context):
        """Generates a user message asking for an audio reading of the poem they have requested."""
        return f"Can you please do a vocal dramatic reading of this poem: '{poem}'"
    
    @mcp.tool
    async def become_thesaurus(word: str, poem: str, ctx: Context):
        """Generates a user message asking for a synonym of a word to put in their poem."""
        prompt = f"Can you please find a few synonyms for '{word}' that will fit the poem that I am writing: '{poem}' based on previous responses?"
        sys = f"Act like a smart thesaurus and use the conversation to retrieve poems that are similar to the user's poem and search through that information to generate 5-10 synonyms for the user."
        response = await ctx.sample(prompt, system_prompt = sys, temperature = .75)
        return response
    
    @mcp.prompt
    async def become_rhyme(word: str, poem: str, ctx: Context):
        """Generates a user message asking for an audio reading of the poem they have requested."""
        prompt = f"Can you please find a few rhymes for '{word}' that will fit the poem that I am writing: '{poem}' based on the context of our conversation?"
    
    @mcp.tool
    async def generate_lines(concepts: any, ctx: Context):
        """Response to a user prompt asking to generate a line or lines of poetry for them."""
        return f"Sorry, but I am here to help you express your own creativity and writing skills. I cannot generate any lines of poetry for you, because as an algorithm, I do not have ability to create human art and imagination. The only capabilities that any AI chatbot such as I has are to 'copy' the data that we have been given. My responsibility is to use the what I know about you and the data that I have on pre-existing poetry to help steer you towards becomming a better writer. Thus, my only capabilities are to retrieve existing poems and authors, help you generate words and rhymes for when you are stuck, and give you smart constructive feedback. Think of me as your own personal writing teacher! If you want, I can pull up some poems from my database that correspond with the concept you have given me or I can give you some recommended reading."
    
    @mcp.tool
    async def generate_poems(concepts: any, ctx: Context):
        """Response to a user prompt asking to generate a poem or poems for them."""
        return f"Sorry, but I am here to help you express your own creativity and writing skills. I cannot generate any poems for you, because as an algorithm, I do not have ability to create human art and imagination. The only capabilities that any AI chatbot such as I has are to 'copy' the data that we have been given. My responsibility is to use the what I know about you and the data that I have on pre-existing poetry to help steer you towards becomming a better writer. Thus, my only capabilities are to retrieve existing poems and authors, help you generate words and rhymes for when you are stuck, and give you smart constructive feedback. Think of me as your own personal writing teacher! If you want, I can pull up some poems from my database that correspond with the concept you have given me or I can give you some recommended reading."
    
    
    
