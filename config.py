"""Configuration for the Research Agent."""

import os
from dotenv import load_dotenv

load_dotenv()

# LLM Configuration
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")  # "openai" or "gemini"
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4-turbo-preview")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.7"))
LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "4096"))

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Agent Configuration
MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "10"))
TIMEOUT_SECONDS = int(os.getenv("TIMEOUT_SECONDS", "300"))
VERBOSE = os.getenv("VERBOSE", "True").lower() == "true"

# Tool Configuration
ENABLE_WEB_SEARCH = os.getenv("ENABLE_WEB_SEARCH", "True").lower() == "true"
ENABLE_FILE_ACCESS = os.getenv("ENABLE_FILE_ACCESS", "True").lower() == "true"
ENABLE_CODE_ANALYSIS = os.getenv("ENABLE_CODE_ANALYSIS", "True").lower() == "true"

# Directories
WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
