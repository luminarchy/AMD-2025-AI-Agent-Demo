<div align="center">

<h1> ⭐  AMD AI Agent ⭐ </h1>
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

Model Context Protocols (MCPs) have brought a new perspective on AI and Large Language Models (LLMs), emerging as a powerful tool able to connect multiple models and APIs to remote machines. The  open-source framework works similar to REST API and provides an interface that allows models to interact with data and context, universalizing the way that AI agents integrate into systems. This project demonstrates the capabilities of MCPs and how they can be used with AMD ROCm machines. The repository contains a Docker Compose file that uses vLLM to build an AI Agent that has function calling capabilities. It also contains a skeleton MCP server that can be integrated with OpenWebUI.


### ✨ Built With ✨

* not entirely sure what to put here

<!-- GETTING STARTED -->

## 🌟 Getting Started 🌟

### ✨ Prerequisites ✨

* **Linux**: see the [supported Linux distributions](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-operating-systems).
* **ROCm**: see the [installation instructions](https://rocm.docs.amd.com/projects/ install-on-linux/en/latest/tutorial/quick-start.html).
* **GPU**: AMD Instinct™ MI300X accelerator or [other ROCm-supported GPUs](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html).
* **Docker**: with Docker Compose - [install](https://docs.docker.com/engine/install/).

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
3. Run the docker compose file to build and start up the containers
   
   ```sh
   docker compose up -d
   ```

* The current docker compose file is set up with the model Llama-xLAM-2-70b-fc-r, which is optimized for function calling capabilities. To change the model, replace the command parameter of the vllm service with:
  
  ```yaml
  command: ["/bin/sh", 
            "-c", 
            "vllm serve <model_name> 
            --port 8001 --enforce-eager 
            --gpu-memory-utilization 0.95 --tensor-parallel-size 2"]
  ```
* Make sure to set up the vllm container to direct to your local models folder. You can do this by modifying the volumes parameter
  
  ```yaml
  volumes:
    - </path/to/your/models>:/hf_home
  ```
* Ensure that the OpenWebUI container is redirected to the proper local path
  
  ```yaml
  volumes:
    - volumes:
      - </path/to/your/repository>/open-webui:/app/backend/data
  ```
* The AI agent should automatically connect to the OpenWebUI image. If it does not, simply go to the `admin panel`, and in `settings` under `connections` add a new connection with the url `http://vllm:8000/v1` and verify the connection.

4. To stop the Ai Agent, simply do
   
   ```sh
   docker compose down
   ```

## 🌟 Usage 🌟

✨ **If you are using the Poetry MCP Server**
The Poetry mcp server code is set up in the `/mcp` directory which contains the scripts to run the MCP server as well as a separate README for the server contianing information about the recommended setup for Open WebUI. 

To set up the model, go to Open WebUI's workspace tab located on the left panel and in `Models`, create a new model titled "Poetry AI Assistant". In the custom model's settings, set the system prompt to the value stored under `System Prompt` in `mcp/setup.txt`. Choose the Base Model and save changes.
Next, go to the `admin panel`, and find the model that is connected to your OpenAI base url. Change that model's system prompt to the value stored under `Model Prompt` in setup.txt. Save the changes.
This will allow you to use a singular model as two separate AI agents, ensuring that all tool functions are called correctly.

✨ **If you are hosting your own MCP server**
A skeleton test MCP server is located in the `/base-mcp` folder for convenience. Simply modify the Dockerfile to copy over your MCP server files to the docker container, and everything else should run smoothly. 


The MCP server should automatically connect to the running OpenWebUI image. If it does not, simply go to `settings` and add a new tool server with the server url. 

### ✨ Examples ✨

This is the Open WebUI with two available MCP servers: the skeleton server `server.py` and the [Balldontlie server at smithery](https://smithery.ai/server/@mikechao/balldontlie-mcp "https://smithery.ai/server/@mikechao/balldontlie-mcp"),

* ![tools](assets/toolservers.png)

This is the response from the AI agent when using an MCP tool from the `Balldontlie` MCP server.

* ![mcp1](assets/mcp1.png)

Command line logs with requests to the skeleton test server.

* ![logs](assets/mcplogs.png)


## 🌟 Troubleshooting 🌟

* If Kokoro does not connect using the `localhost` url:
  Find the docker container network url. In VSCode, locate the docker tab on the left menu bar and locate the parent docker container under the `networks` section and open the corresponding file. Find the network url for the Kokoro container in the file. 
  
  In Open WebUI, open the admin panel, and click the `Audio` tab. Under TTS, change the engine to `OpenAI`. Fill in the OpenAI base url with the docker container network url and fill in the OpenAI key with `not-needed`. Change the model name to `Kokoro`. To see all voices available, go to `http://localhost:8880/docs`. 

  

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

