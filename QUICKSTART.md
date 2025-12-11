# Quick Start Guide

## Installation

1. **Clone and navigate to the project:**
```bash
cd research-agent
```

2. **Create a virtual environment (optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Setup

1. **Get an OpenAI API Key:**
   - Visit https://platform.openai.com/account/api-keys
   - Create a new API key
   - Copy your key

2. **Set your API key:**
```bash
export OPENAI_API_KEY="sk-your-api-key-here"
```

Or create a `.env` file in the project root:
```
OPENAI_API_KEY=sk-your-api-key-here
LLM_MODEL=gpt-4-turbo-preview
LLM_TEMPERATURE=0.7
MAX_ITERATIONS=10
VERBOSE=True
```

## Running Examples

**Simple Research Task:**
```bash
python examples/research_task.py
```

**Code Analysis and Review:**
```bash
python examples/code_analysis.py
```

**Content Planning:**
```bash
python examples/content_planning.py
```

## Using the Agent in Your Code

```python
from agent.core import create_agent

# Create an agent
agent = create_agent(verbose=True)

# Run a task
task = "Research the latest AI trends and summarize them"
result = agent.run(task)

# Check the result
if result['success']:
    print(result['output'])
else:
    print(f"Error: {result['error']}")
```

## Running Multiple Tasks

```python
from agent.core import create_agent

agent = create_agent(verbose=False)

tasks = [
    "What is machine learning?",
    "Explain neural networks",
    "What are transformers?"
]

results = agent.run_batch(tasks)

for task, result in zip(tasks, results):
    print(f"\nTask: {task}")
    print(f"Answer: {result['output'][:200]}...")
```

## Customization

### Change the LLM Model
```python
agent = create_agent(model="gpt-3.5-turbo", verbose=True)
```

### Adjust Temperature (Creativity)
```python
agent = create_agent(temperature=0.5)  # More deterministic
agent = create_agent(temperature=0.9)  # More creative
```

### Increase Max Iterations
```python
agent = create_agent(max_iterations=15)
```

## Troubleshooting

**Issue: "OpenAI API key not found"**
- Make sure you've set the OPENAI_API_KEY environment variable
- Check: `echo $OPENAI_API_KEY` (Linux/Mac) or `echo %OPENAI_API_KEY%` (Windows)

**Issue: "ModuleNotFoundError: No module named 'langchain'"**
- Install dependencies: `pip install -r requirements.txt`

**Issue: "Rate limit exceeded"**
- The agent is making too many API calls
- Reduce max_iterations or wait before running again

**Issue: Agent not providing detailed answers**
- Increase temperature (more creative)
- Increase max_iterations (more reasoning steps)
- Use a more capable model (gpt-4 instead of gpt-3.5)

## Architecture Overview

The agent uses the **ReAct (Reasoning + Acting)** pattern:

1. **Understand**: Parse the task
2. **Reason**: Plan the approach
3. **Act**: Execute tools to gather information
4. **Observe**: Process results
5. **Reflect**: Decide if more action is needed
6. **Repeat**: Continue until complete

### Available Tools

- **web_search**: Search for information online
- **analyze_text**: Summarize or analyze text
- **read_file**: Read file contents
- **list_files**: Browse directories
- **calculate**: Perform mathematical operations
- **code_review**: Analyze code quality

## Next Steps

1. **Add custom tools**: Edit `agent/tools.py` to add your own tools
2. **Modify prompts**: Edit `agent/prompts.py` to customize agent behavior
3. **Extend the agent**: Create specialized agent subclasses for specific domains
4. **Build a UI**: Create a web interface using Flask or FastAPI
5. **Deploy**: Package as Docker container or serverless function

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
