#!/bin/bash

# Base configuration with defaults
MODE=${MODE:-"serve"}
MODEL=${MODEL:-"amd/Llama-3.2-1B-FP8-KV"}
PORT=${PORT:-3000}

# Benchmark configuration with defaults
INPUT_LEN=${INPUT_LEN:-512}
OUTPUT_LEN=${OUTPUT_LEN:-256}
NUM_PROMPTS=${NUM_PROMPTS:-1000}
NUM_ROUNDS=${NUM_ROUNDS:-3}
MAX_BATCH_TOKENS=${MAX_BATCH_TOKENS:-8192}
NUM_CONCURRENT=${NUM_CONCURRENT:-8}

# Additional args passed directly to vLLM
EXTRA_ARGS=${EXTRA_ARGS:-""}

case $MODE in
  "serve")
    echo "Starting vLLM server on port $PORT with model: $MODEL"
    echo "Additional arguments: $EXTRA_ARGS"
    python3 -m vllm.entrypoints.openai.api_server \
      --model $MODEL \
      --port $PORT \
      $EXTRA_ARGS
    ;;
    
  "benchmark")
    echo "Running vLLM benchmarks with model: $MODEL"
    echo "Additional arguments: $EXTRA_ARGS"
    
    # Create timestamped directory for this benchmark run
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    BENCHMARK_DIR="/data/benchmarks/$TIMESTAMP"
    mkdir -p "$BENCHMARK_DIR"
    
    # Throughput benchmark
    echo "Running throughput benchmark..."
    python3 /app/vllm/benchmarks/benchmark_throughput.py \
      --model $MODEL \
      --input-len $INPUT_LEN \
      --output-len $OUTPUT_LEN \
      --num-prompts $NUM_PROMPTS \
      --max-num-batched-tokens $MAX_BATCH_TOKENS \
      --output-json "$BENCHMARK_DIR/throughput.json" \
      $EXTRA_ARGS
    echo "Throughput benchmark complete - results saved in $BENCHMARK_DIR/throughput.json"
    
    # Latency benchmark
    echo "Running latency benchmark..."    
    python3 /app/vllm/benchmarks/benchmark_latency.py \
      --model $MODEL \
      --input-len $INPUT_LEN \
      --output-len $OUTPUT_LEN \
      --output-json "$BENCHMARK_DIR/latency.json" \
      $EXTRA_ARGS
    echo "Latency benchmark complete - results saved in $BENCHMARK_DIR/latency.json"

    echo "All results have been saved to $BENCHMARK_DIR"
    ;;
    
  *)
    echo "Unknown mode: $MODE"
    echo "Please use 'serve' or 'benchmark'"
    exit 1
    ;;
esac