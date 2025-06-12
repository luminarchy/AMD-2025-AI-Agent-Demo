<div align="center">

<h1>Voice AI Agent</h1>
<div align="left">

<details>
  <summary>Table of Contents</summary>
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
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

Model Context Protocols (MCPs) have brought a new perspective on AI and Large Language Models (LLMs), emerging as a powerful tool able to connect multiple models and APIs to remote machines. MCPs, introduced by ANthropic in 2024, are an open-source framework that universalizes the way that AI agents integrate into systems. The design works similar to REST API and provides an interface that allows models to interact with data and context. This project demonstrates the capabilities of MCPs and how they can be used with AMD ROCm machines. The repository contains a Docker Compose file that uses vLLM to build an AI Agent that has function calling capabilities. It also has a skeleton MCP server that can be integrated with OpenWebUI.

### Built With

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

* **Linux**: see the [supported Linux distributions](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-operating-systems).
* **ROCm**: see the [installation instructions](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/quick-start.html).
* **GPU**: AMD Instinct™ MI300X accelerator or [other ROCm-supported GPUs](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html).
* **Docker**: with Docker Compose - [install](https://docs.docker.com/engine/install/).

### Installation

<!-- USAGE EXAMPLES -->

1. Clone the repo
   
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Change git remote url to avoid accidental pushes to base project
   
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```
3. Run the docker compose file to build and start up OpenWebUI and the vLLM container
   
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

**If you are hosting your own MCP server**
The skeleton server is stored in the MCP file in `server.py`. To start the server, first install MCPO using pip:

```sh
pip install mcpo
```

Then run:

```sh
mcpo --port 8004 -- python server.py
```

**If you are hosting an MCP server from Smithery.ai**
Install the server using auto install. You may have to install npm first.

```sh
sudo apt install npm
```

Then you can run the server with the given command from smithery inputted to mcpo.

```sh
mcpo --port 8004 -- <server start up command>
```

The MCP server should automatically connect to the running OpenWebUI image. If it does not, simply go to `settings` and add a new tool server with the url ``

## Usage

This is the Open WebUI with two available MCP servers, the skeleton server `server.py` and the [Balldontlie server at smithery](https://smithery.ai/server/@mikechao/balldontlie-mcp "https://smithery.ai/server/@mikechao/balldontlie-mcp"),

* ![tools](assets/toolservers.png)

This is the response from the AI agent when using an MCP tool from the `Balldontlie` MCP server.

* ![mcp1](assets/mcp1.png)

Command line logs with requests to the skeleton test server.

* ![logs](assets/mcplogs.png)

