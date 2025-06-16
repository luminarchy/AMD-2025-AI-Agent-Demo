# AI Agents

## 1. Project Overview

Fully functional AI agents using MCP and vLLM with complete open-source framework, as well as complete documentation to demo for customers.

## 2. Core Components

### 2.1 AI Agent

- **vLLM**
    - Model: xLAM-2-70b-fc-r
    - Features:
        - Multi-turn Conversation
        - Function-calling
        - vLLM integration

### 2.2 MCP

- **FastMCP**
    - Features:
        - Exposes data
        - Provides tools
        - Define interaction patterns
        - Modular
    - Output: an MCP server connecting to any number of API databases


- **MCPO**
    - Features:
        - Connects MCP instantly with OpenAI, SDKs, and UIs
        - Trusted web standards
        - Auto-generates interactive docs for tools
        - Pure HTTP
    - Output: Connection between MCP server and Open Web UI

### 2.3 Input/Output

- **Open Web UI**
    - Features:
        - Built-in inference engine for RAG
        - OpenAI API Integration
        - Model Builder
        - Concurrent Model Utilization
    - Feature-rich and user-friendly self-hosted AI Platform

- **Speech to Text**
    - Model: Systran Faster Whisper
    - Features:
        - Encoder-decoder model
        - Open WebUI integration
        - GPU Acceleration support
        - Background noise robustness
    - Output: Text transcription of audio


- **Text to Speech**
    - Model: Kokoro
    - Features:
        - GPU acceleration
        - Multiple voice support
        - Audio playback capability
        - Open WebUI compatability 
    - Output: High quality speech synthesis

## 3. Script Requirements

### 3.1 Setup

#### 3.1.2 Directory Structure Creation

- **Root Directory Files**
    - `README.md` - Project documentation
    - `PRD.md` - Product requirements document
    - `compose.yaml` - Docker Compose file

- **Child Directories**
    - `mcp/` - MCP servers
        - `format.py` - response formatting
        - `poem.py` - MCP server for poetryDB API
        - `server.py` - test skeleton MCP server
    - `open-webui/` - Open WebUI 
    - `assets/` - documentation screenshots and images

#### 3.1.3 Environment Setup


## 4. Technical Requirements

