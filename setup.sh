#!/bin/bash

# Upgrade pip first (optional but recommended)
pip install --upgrade pip

# Install torch and related libs first (must be before GPTQModel)
pip install torch torchvision torchtext --extra-index-url https://download.pytorch.org/whl/cu117

# Install other packages
pip install streamlit transformers accelerate safetensors

# Install GPTQModel from GitHub with --no-build-isolation to avoid build errors related to torch missing
pip install --no-build-isolation git+https://github.com/ModelCloud/GPTQModel.git
