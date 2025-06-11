
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js"


const config = {
  "balldontlieApiKey": "string"
}
const profileId = "narrow-hamster-nO6iEx"
const apiKey = "f6364c70-c3e1-4f93-9624-887ff01c8943"
const url = new URL("https://server.smithery.ai/@mikechao/balldontlie-mcp/mcp?profile=narrow-hamster-nO6iEx&api_key=f6364c70-c3e1-4f93-9624-887ff01c8943")
const transport = new StreamableHTTPClientTransport(
  url
)

// Create MCP client
import { Client } from "@modelcontextprotocol/sdk/client/index.js"

const client = new Client({
	name: "Test client",
	version: "1.0.0"
})
await client.connect(transport)
console.log("hello")

// Use the server tools with your LLM application
