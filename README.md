# Research & Task Automation Agent

A powerful AI agent that breaks down complex tasks, performs research, and coordinates multiple actions to solve real-world problems.

## Features

- **Task Decomposition**: Breaks complex tasks into manageable subtasks
- **Tool Integration**: Executes specialized tools (search, analysis, summarization)
- **Reasoning Loop**: Thinks through problems step-by-step before taking action
- **Error Handling**: Gracefully handles failures and retries
- **Extensible Architecture**: Easy to add new tools and capabilities

## Project Structure

```
research-agent/
├── agent/
│   ├── __init__.py
│   ├── core.py              # Main agent class
│   ├── tools.py             # Tool definitions
│   ├── prompts.py           # System prompts and templates
│   └── utils.py             # Utility functions
├── examples/
│   ├── research_task.py     # Example: Research automation
│   ├── code_analysis.py     # Example: Code analysis
│   └── content_planning.py  # Example: Content planning
├── config.py                # Configuration
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Environment Variables
```bash
export OPENAI_API_KEY="your-api-key"
```

### 3. Run an Example
```bash
python examples/research_task.py
```

## How It Works

The agent follows a ReAct (Reasoning + Acting) pattern:

1. **Think**: Analyzes the task and plans an approach
2. **Act**: Uses available tools to gather information
3. **Observe**: Processes tool outputs
4. **Reflect**: Determines if the task is complete
5. **Repeat**: Continues until task is solved

## Available Tools

- **web_search**: Search for information online
- **analyze_text**: Summarize or analyze text content
- **list_files**: Browse local file system
- **read_file**: Extract content from files
- **calculate**: Perform mathematical operations
- **code_review**: Analyze code and provide feedback

## Adding Custom Tools

Edit `agent/tools.py` to add new tools:

```python
@tool
def my_custom_tool(param: str) -> str:
    """Tool description for the agent."""
    # Implementation
    return result
```

## Use Cases

- Research automation and competitive analysis
- Code review and refactoring
- Content creation and planning
- Data analysis and reporting
- Technical documentation generation
- Project planning and task breakdown

## Configuration

Edit `config.py` to customize:
- Model selection (GPT-4, Claude, etc.)
- Temperature and sampling parameters
- Max iterations and timeout settings
- Tool availability

## Requirements

- Python 3.10+
- OpenAI API key (or alternative LLM)
- Internet connection (for web search tools)
