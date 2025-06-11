"use strict";
exports.__esModule = true;
var streamableHttp_js_1 = require("@modelcontextprotocol/sdk/client/streamableHttp.js");
var config = {
    "balldontlieApiKey": "string"
};
var profileId = "narrow-hamster-nO6iEx";
var apiKey = "f6364c70-c3e1-4f93-9624-887ff01c8943";
var url = new URL("https://server.smithery.ai/@mikechao/balldontlie-mcp/mcp?profile=narrow-hamster-nO6iEx&api_key=f6364c70-c3e1-4f93-9624-887ff01c8943");
var transport = new streamableHttp_js_1.StreamableHTTPClientTransport(url);
// Create MCP client
var index_js_1 = require("@modelcontextprotocol/sdk/client/index.js");
var client = new index_js_1.Client({
    name: "Test client",
    version: "1.0.0"
});
await client.connect(transport);
// Use the server tools with your LLM application
