import mcp
from mcp.client.streamable_http import streamablehttp_client
import json
import base64
# smitery: 357f2a7e-1797-4875-9964-7a46c6d35a08
# balldontlie: a6cfa536-43b1-4edb-9f9b-04f351dc8087
# command to start for amy: mcpo --port 8004 -- npx -y @smithery/cli@latest run @mikechao/balldontlie-mcp --key f6364c70-c3e1-4f93-9624-887ff01c8943 --profile narrow-hamster-nO6iEx
config = {
  "balldontlieApiKey": "a6cfa536-43b1-4edb-9f9b-04f351dc8087"
}
# Encode config in base64
config_b64 = base64.b64encode(json.dumps(config).encode())
smithery_api_key = "f6364c70-c3e1-4f93-9624-887ff01c8943"
profileId = "narrow-hamster-nO6iEx"

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
    asyncio.run(main())# b4d9c384-9f59-4165-947c-794519cc1f3c