FROM python
# Install basic development tools
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /mcp
COPY mcp/poem.py .
COPY mcp/poemtools.py .
COPY mcp/poemprompts.py .
COPY mcp/format.py .
COPY mcp/PoetryFoundationData.xlsx .
COPY mcp/requirements.txt .

# Install additional dependencies
RUN pip3 install -r requirements.txt



