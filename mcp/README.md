<div align="center">

<h1> ⭐  Poetry MCP Server ⭐ </h1>
meow
<div align="left">

<!-- TABLE OF CONTENTS -->

<details>
  <summary>✨ Table of Contents ✨ </summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a>
      <ul>
        <li><a href="#examples">Examples</a></li>
      </ul></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## 🌟 About The Project 🌟

Why poetry? Being passionate for both AI and poetry is quite the challenge. AI is indeed elegant and capable, but it has its limitations. Art is human in nature, and thus can never be created by algorithms and machines. AI can only imitate art; it reads data and spits out a replica. So what purpose is a Poetry AI if it cannot create poetry? My friends in academia often say "A better reader makes a better writer". The more literature one reads, the better and more sophisted their writing becomes. In a way, we are similar to the algorithms. We take in data, analyze it for things we like, and replicate those things in our art. But, where we and the technology diverge is with our individuality and creativity. It is the fact of life that each and every person is different, with their own experiences and perceptions. Our personalities, memories, and quirks compose the unique way we read and write. That is what births our creativity, our ability to think of ideas in a way that no one else in the entire world has done. But we cannot possibly read or know everything. At times, we are lost, not knowing where to go next. That is where AI can help.

The Poetry MCP Server provides tools that use SQL queries into a dataset pulled from the Poetry Foundation, enabling the AI agent to access an inhuman amount of poetry data, categorized by Poet, Title, and Tags. It provides basic functionalities, such as searching for particular author or theme or chaining multiple queries to find, for example, poets who write about similar topics. Using context from conversation history, it refines its searches by prioritizing certain preferences or topics. Think of it as an (almost) all-knowing librarian able to provide a myriad of recommendations and references.
The Poetry MCP Server additionally hosts poetry-writing functionalities through OpenAI Chat Completions. When given a user-written poem, it is able to provide guided feedback with citations from the dataset. As a data analysis tool, it is able to cross-compare themes, motifs, imagery, and more. While LLMs cannot create art, they do specialize in next word prediction or fill-in-the-blank tasks, such as finding synonyms or rhymes. Its tools also allow for it to refine its generation with common words in pre-existing poetry. In any and all word generation tools, users are given a wide selection of words and, of their own accord, must choose which to use if they wish to do so.

However, the MCP Server does NOT support any type of generation that attempts to generate full phrases, lines, or poems. As a writer myself, it breaches ethics and reinforces the heavy stigma around AI in the English Literary world. I have created this MCP server in hopes of creating a bridge between my two interests and to use my passion for AI to better young writers and foster their creativity in a current day so engrossed in AI. I wish to show that generative AI can be used ethically and safely by artists.

### ✨ Built With ✨

* FastMCP
* OpenAI
* Pandas

<!-- GETTING STARTED -->

## 🌟 Getting Started 🌟

### ✨ Installation ✨

1. Clone the repo
   
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Change git remote url to avoid accidental pushes to base project
   
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```
3. pip install requirements
   
   ```sh
   pip install -r requirements
   ```
4. Set up the OpenAI base url and key in `poemprompts.py`
   
   ```py
   openai_api_base = "http://localhost:8001/v1"
    openai_key = "EMPTY"
   ```

## 🌟 Usage 🌟

✨ **If you are using Open WebUI (default)**
Inside the `mcp` directory, run the server using the command

```sh
mcpo --port 8002 -- python poem.py
```

For the best experience, please use a model that supports function calling. This can then be enabled with Open WebUI in the model's `advanced params`: `Function Calling = Native`.

To set up the model, go to Open WebUI's workspace tab located on the left panel and in `Models`, create a new model titled "Poetry AI Assistant". In the custom model's settings, set the system prompt to the value stored under `System Prompt` in `setup.txt`. Choose the Base Model and save changes.
Next, go to the `admin panel`, and find the model that is connected to your OpenAI base url. Change that model's system prompt to the value stored under `Model Prompt` in setup.txt. Save the changes.
This will allow you to use a singular model as two separate AI agents, ensuring that all tool functions are called correctly.

The default AMD AI Agent project uses Open WebUI and vllm by default. Ensure that Open WebUI is running before starting up the server. This will allow the server to connect to vllm as the OpenAI endpoint for chat completions. MCPO will host a client connection to the server. Since Open WebUI does not have full support for MCP, the server will be connected as a tool server instead. In order to bypass this restriction, the Poetry MCP Server uses Open AI chat completions as a replacement for MCP sampling requests. If you are using a client that supports sampling, then simply replace the chat completions in `poemprompts.py` with FastMCP sampling, as this is a more integrated solution for chat completions.

✨ **For other Client connections**
The server startup command is

```sh
python poem.py
```

You can find sample system prompts in `setup.txt`.

### ✨ Tools ✨

* **get_all_authors()**
  * gets a list of all poets in the Poetry Foundation database
  * Inputs:
    * none
* **get_author(*author_last, author_first*)**
  * gets a list of the titles of all poems written by a poet
  * Inputs:
    * `author_last` (string) last name of poet to search for
    * `author_first` (string, optional) first name of poet to search for
* **get_complete_author(*author_last, author_first*)**
  * gets a complete list of all poems written by a poet
  * Inputs:
    * `author_last` (string) last name of poet to search for
    * `author_first` (string, optional) first name of poet to search for
* **get_poem_title(*title*)**
  * gets a poem by its title
  * Inputs:
    * `title` (string) title of poem to search for
* **get_poems_keywords(*keyword*)**
  * gets poems that contain a specific keyword
  * Inputs:
    * `keyword` (string) keyword to search for
* **get_tag(*tag*)**
  * gets poems under a Poetry Foundation tag
  * Inputs:
    * `tag` (string) tag to search for
* **get_reference(*authors, tags*)**
  * gets poems based on user preferences
  * Inputs:
    * `author` (Optional, list[string]) poets to search for
    * `tag` (Optional, list[string]) tags to search for
* **become_feedback(*poem*)**
  * generates constructive feedback for a poem based on its structure, themes, rhythm, and rhyme
  * Inputs:
    * `poem` (string) user-submitted poem
* **become_thesaurus(*poem, word*)**
  * generates 5-10 synonyms for a word to be used in poem based on its theme
  * Inputs:
    * `poem` (string) user-submitted poem
    * `word` (string) word to get synonyms for
* **become_rhyme(*poem, word*)**
  * generates 5-10 rhymes for a word to be used in poem based on its theme
  * Inputs:
    * `poem` (string) user-submitted poem
    * `word` (string) word to get rhymes for
* **become_word(*poem*)**
  * generates 5-10 words to be used in poem based on its theme
  * Inputs:
    * `poem` (string) user-submitted poem with a fill-in-the-blank task

### ✨ Examples ✨

This is the Open WebUI with two available MCP servers: the skeleton server `server.py` and the [Balldontlie server at smithery](https://smithery.ai/server/@mikechao/balldontlie-mcp "https://smithery.ai/server/@mikechao/balldontlie-mcp"),

* ![tools](assets/toolservers.png)

This is the response from the AI agent when using an MCP tool from the `Balldontlie` MCP server.

* ![mcp1](assets/mcp1.png)

Command line logs with requests to the skeleton test server.

* ![logs](assets/mcplogs.png)

## 🌟 License 🌟

i also do not know what to put here

<!-- CONTACT -->

## 🌟 Contact 🌟

Amy Suo - amysuwoah@gmail.com / amy.suo@amd.com / as331@rice.edu

Project Link: [https://github.com/luminarchy/AMD-2025-AI-Agent-Demo](https://github.com/luminarchy/AMD-2025-AI-Agent-Demo)

<!-- ACKNOWLEDGMENTS -->

## 🌟 Acknowledgments 🌟

* [AMD ROCm Blogs](https://rocm.blogs.amd.com/)
* [Smithery](https://smithery.ai/)
* [BallDontLie API](https://www.balldontlie.io/)
* [BallDontLie MCP Server](https://github.com/mikechao/balldontlie-mcp)
* Furthermore i do not know what to put here

