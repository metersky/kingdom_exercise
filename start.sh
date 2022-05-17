#!/usr/bin/env bash

# tear down db if exists to maintain idempotency
rm experiments.db

python exercise/insert_data.py && \
    python exercise/dashboard.py && \
    python exercise/visualization.py \

mv output.png visualization/output.png
