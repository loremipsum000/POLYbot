#!/bin/bash

# Activate virtual environment
if [ -f "venv/bin/activate" ]; then
    . venv/bin/activate
fi

# Export environment from .env if present (ensures bundle thresholds are loaded)
if [ -f ".env" ]; then
    set -a
    . ./.env
    set +a
fi

# Run the taker (bundle arbitrage) entrypoint
python3 strategies/taker/run_taker.py "$@"

