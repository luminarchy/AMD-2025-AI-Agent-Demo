import mcp
from mcp.client.streamable_http import streamablehttp_client
import json
import base64

config = {
  "balldontlieApiKey": "string"
}
# Encode config in base64
config_b64 = base64.b64encode(json.dumps(config).encode())
smithery_api_key = "api-key"
profileId = "profile"

# Create server URL
url = f"https://server.smithery.ai/@mikechao/balldontlie-mcp/mcp?config={config_b64}&api_key={smithery_api_key}&profile={profileId}"

async def main():
    # Connect to the server using HTTP client
    async with streamablehttp_client(url) as (read_stream, write_stream, _):
        async with mcp.ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            tools_result = await session.list_tools()
            print(f"Available tools: {', '.join([t.name for t in tools_result.tools])}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())