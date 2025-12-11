# Research & Task Automation Agent

A powerful AI agent that breaks down complex tasks, performs research, and coordinates multiple actions to solve real-world problems.

## Features

- **ReAct Pattern Implementation** - Combines reasoning and action in feedback loops
- **Multi-Provider Support** - Works with OpenAI GPT-4 and Google Gemini
- **Multiple Tools** - Web search, text analysis, file operations, code review
- **Error Handling** - Graceful failure recovery and retry logic
- **Production Ready** - Proper structure, configuration, documentation
- **Extensible Architecture** - Easy to add new tools and capabilities
- **Interactive & Batch Modes** - Single task, batch, or interactive

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set API Keys

**Using Google Gemini (Free):**
```bash
export GEMINI_API_KEY="your-api-key"
```

**Using OpenAI:**
```bash
export OPENAI_API_KEY="sk-your-api-key"
```

Get Gemini API key (free): https://ai.google.dev/  
Get OpenAI API key: https://platform.openai.com/account/api-keys

### 3. Run the Agent

**With Gemini (default):**
```bash
python main.py "Research AI trends in 2025"
```

**With OpenAI:**
```bash
python main.py --provider openai "Your task here"
```

**Interactive mode:**
```bash
python main.py
```

## Usage Examples

### Command Line
```bash
# Single task with default provider (Gemini)
python main.py "Research the latest AI breakthroughs"

# Use OpenAI
python main.py --provider openai "Review this code for best practices"

# Interactive mode
python main.py
```

### Python API
```python
from agent.core import create_agent

# Use Gemini (default)
agent = create_agent(provider="gemini", verbose=True)
result = agent.run("Research AI trends")
print(result['output'])

# Use OpenAI
agent = create_agent(provider="openai")
result = agent.run("Write a technical article outline")
print(result['output'])
```

## Project Structure

```
research-agent/
├── agent/                    # Core agent implementation
│   ├── core.py              # ResearchAgent class
│   ├── tools.py             # Tool definitions
│   ├── prompts.py           # System prompts
│   └── utils.py             # Utilities
├── examples/                # Usage examples
│   ├── research_task.py     # Research automation
│   ├── code_analysis.py     # Code review
│   ├── content_planning.py  # Strategic planning
│   └── gemini_examples.py   # Gemini-specific examples
├── main.py                  # CLI entry point
├── config.py                # Configuration
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## Available Tools

1. **web_search** - Search for information online
2. **analyze_text** - Summarize or extract key points
3. **read_file** - Extract content from files
4. **list_files** - Browse directory structure
5. **calculate** - Perform mathematical operations
6. **code_review** - Analyze code quality

## Configuration

Create a `.env` file or set environment variables:

```env
# Provider selection
LLM_PROVIDER=gemini              # "gemini" or "openai"

# API Keys
GEMINI_API_KEY=your-gemini-key
OPENAI_API_KEY=sk-your-openai-key

# Agent settings
LLM_TEMPERATURE=0.7              # Creativity (0-1)
MAX_ITERATIONS=10                # Max reasoning steps
VERBOSE=True                     # Show detailed logs
```

## How It Works

The agent uses the **ReAct (Reasoning + Acting)** pattern:

```
1. UNDERSTAND - Parse the task
2. REASON - Plan the approach
3. ACT - Execute tools
4. OBSERVE - Process results
5. REFLECT - Check completion
6. REPEAT - Continue until complete
```

## Supported Providers

### Google Gemini
- **Pros**: Free tier, fast, good for general tasks
- **Model**: gemini-pro
- **Setup**: `export GEMINI_API_KEY="your-key"`

### OpenAI GPT-4
- **Pros**: More powerful, better reasoning
- **Model**: gpt-4-turbo-preview
- **Setup**: `export OPENAI_API_KEY="sk-your-key"`

## Running Examples

```bash
# Research task automation
python examples/research_task.py

# Code analysis and review
python examples/code_analysis.py

# Content planning
python examples/content_planning.py

# Gemini-specific examples
python examples/gemini_examples.py
```

## Advanced Usage

### Batch Processing
```python
from agent.core import create_agent

agent = create_agent(provider="gemini", verbose=False)

tasks = [
    "What is machine learning?",
    "Explain neural networks",
    "What are transformers?"
]

results = agent.run_batch(tasks)
```

### Custom Tools
Edit `agent/tools.py` to add custom tools:

```python
@tool
def my_tool(param: str) -> str:
    """Tool description."""
    return result

TOOLS.append(my_tool)
```

### Different Models
```python
# Use specific model
agent = create_agent(provider="openai", model="gpt-3.5-turbo")

# Adjust creativity
agent = create_agent(temperature=0.9)  # More creative
agent = create_agent(temperature=0.2)  # More deterministic
```

## Troubleshooting

**"API key not found"**
- Set environment variable: `export GEMINI_API_KEY="..."`
- Or create `.env` file with your key

**"ModuleNotFoundError"**
- Install dependencies: `pip install -r requirements.txt`

**Agent not detailed enough**
- Increase temperature: `temperature=0.9`
- Increase iterations: `max_iterations=15`
- Use more capable model (GPT-4 vs Gemini)

**Rate limit exceeded**
- Wait before running again
- Use Gemini (higher free tier limits)

## Requirements

- Python 3.10+
- OpenAI API key OR Google Gemini API key
- Internet connection (for web search tools)

## Architecture

The agent is built with:
- **Framework**: LangChain (agents, tools, prompts)
- **Pattern**: ReAct (Reasoning + Acting)
- **Providers**: OpenAI, Google Gemini
- **Design**: Modular, extensible

## Use Cases

- Research automation and competitive analysis
- Code review and refactoring assistance
- Content creation and planning
- Data analysis and reporting
- Technical documentation generation
- Project planning and task breakdown

## Next Steps

1. **Get an API key** (Gemini is free to start)
2. **Run an example**: `python main.py "Your question"`
3. **Customize tools** in `agent/tools.py`
4. **Create specialized agents** for your domain
5. **Deploy** as web service or cloud function

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Google Gemini API](https://ai.google.dev/)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
