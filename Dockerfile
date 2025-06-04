FROM rocm/vllm:latest
# Install basic development tools
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install additional dependencies
RUN pip3 install --no-cache-dir \
    transformers \
    accelerate \
    safetensors

# Create directories for models and benchmarks
RUN mkdir -p /data/benchmarks && \
   chmod 777 /data/benchmarks

# Make our entrypoint script executable
COPY --chown=vllm:vllm entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"] 

