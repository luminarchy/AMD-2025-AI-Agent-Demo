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

This MCP server uses the Poetry MCP architecture to conduct SQL querying and inserting into a database without needing APIs. Using SQLite, this method of retrieving data is faster and simpler and has a large breadth of applications.

### ✨ Built With ✨

* FastMCP
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
4. Import dataset into the base-mcp folder as database.xlsx

## 🌟 Usage 🌟

✨ **If you are using Open WebUI (default)**
Inside the `base-mcp` directory, run the server using the command

```sh
mcpo --port 8002 -- python server.py -e <env_variables>
```

The default AMD AI Agent project uses Open WebUI and vllm by default. Ensure that Open WebUI is running before starting up the server. This will allow the server to connect to vllm as the OpenAI endpoint for chat completions. MCPO will host a client connection to the server. Since Open WebUI does not have full support for MCP, the server will be connected as a tool server instead.

✨ **For other Client connections**
The server startup command is

```sh
python server.py
```

### ✨ Tools ✨

* **get_one_parameter(*parameter, value, limit = 10*)**
  * Searches through the database using the value of one column
  * Inputs:
    * `parameter` (string) the name of the column to search through
    * `value` (string) the value to match
    * `limit` (int default 10) limits the number of returned entries
* **get_multiple_parameter(*parameter, value, al = True, limit = 10*)**
  * Searches through the database using the values of multiple columns
  * Inputs:
    * `parameter` (list[string]) the name of the columns to search through
      * ie: ["a", "b", "c"]
    * `value` (list[string]) the values to match, indiexed respective to corresponding column name in `parameter`
      * ie: ["a_val", "b_val", "c_val"]
    * `al` (bool default True) whether returned entries have to match all search conditions or at least one (akin to and/or)
    * `limit` (int default 10) limits the number of returned entries
* **get_one_parameter_mult(*parameter, value, al = True, limit = 10*)**
  * Searches through the database using multiple values of one column
  * Inputs:
    * `parameter` (string) the name of the columns to search through
      * ie: "a"
    * `value` (list[string]) the values to match, indiexed respective to corresponding column name in `parameter`
      * ie: ["a_val1", "a_val2", "a_val3"]
    * `limit` (int default 10) limits the number of returned entries
    * `al` (bool default True) whether returned entries have to match all search conditions or at least one (akin to and/or)
* **get_mult_parameter_mult(*parameter, value, al = True, limit = 10*)**
  * Searches through the database using multiple values of multiple columns
  * Inputs:
    * `parameter` (list[string]) the name of the columns to search through
      * ie: ["a", "b", "c"]
    * `value` (list[list[string]]) the values to match, indexed respective to corresponding column name in `parameter`
      * ie: [["a_val1", "a_val2", "a_val3"], ["b_val1", "b_val2"], ["c_val1", "c_val2"]]
    * `al` (bool default True) whether returned entries have to match all search conditions or at least one (akin to and/or)
    * `limit` (int default 10) limits the number of returned entries
* **put_entry(*values*)**
  * Inserts an entry into the database instance. This does not modify the underlying file. 
  * Inputs:
    * `values` (dict) Mapping of the values to insert into the datase
      * ie: {"a": "a_val", "b": "b_val", "c": "c_val"}

## 🌟 Contact 🌟

Amy Suo - amysuwoah@gmail.com / amy.suo@amd.com / as331@rice.edu

Project Link: [https://github.com/luminarchy/AMD-2025-AI-Agent-Demo](https://github.com/luminarchy/AMD-2025-AI-Agent-Demo)

