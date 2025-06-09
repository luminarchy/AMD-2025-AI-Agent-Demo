from llama_index.tools.mcp import BasicMCPClient, McpToolSpec

# MCP server configuration
MCP_URL = "http://localhost:8000/sse"

client = BasicMCPClient(MCP_URL)
print(f"Connecting to MCP server at {MCP_URL}...")
        
# Get available tools
tools_spec = McpToolSpec(client=client)
tools = await asyncio.wait_for(
            tools_spec.to_tool_list_async(),
            timeout=10
        ) 