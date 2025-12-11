# Gemini Setup Guide

This guide walks you through setting up the Research Agent with Google's Gemini API.

## Why Gemini?

✅ **Free tier available** - Get started without a credit card  
✅ **Fast inference** - Quick response times  
✅ **Good for general tasks** - Excellent for research and analysis  
✅ **Easy setup** - Simple API key management  

## Step 1: Get Your Gemini API Key

1. **Visit Google AI Studio**
   - Go to: https://ai.google.dev/
   - Click "Get API Key"

2. **Create a new API key**
   - Click "Create API key in new project"
   - Copy your API key (starts with `AIza...`)

3. **Keep it safe**
   - Never commit to git
   - Use environment variables or `.env` file

## Step 2: Install Dependencies

```bash
cd research-agent
pip install -r requirements.txt
```

This installs:
- `langchain` - Agent framework
- `langchain-google-genai` - Gemini integration
- `google-generativeai` - Gemini API client

## Step 3: Configure Your API Key

### Option A: Environment Variable (Recommended)
```bash
export GEMINI_API_KEY="AIzaSy..."
```

### Option B: .env File
Create `.env` in project root:
```
GEMINI_API_KEY=AIzaSy...
LLM_PROVIDER=gemini
```

### Option C: Programmatically
```python
import os
os.environ['GEMINI_API_KEY'] = 'AIzaSy...'
```

## Step 4: Run Your First Task

### Using Command Line
```bash
python main.py "What is machine learning?"
```

### Interactive Mode
```bash
python main.py
```
Then type your task at the prompt.

### Python Script
```python
from agent.core import create_agent

agent = create_agent(provider="gemini", verbose=True)
result = agent.run("Research AI trends in 2025")
print(result['output'])
```

## Example Tasks

```bash
# Research
python main.py "Research the latest AI breakthroughs in 2025"

# Analysis
python main.py "Analyze the pros and cons of microservices architecture"

# Planning
python main.py "Create a 3-month plan for learning machine learning"

# Code Review
python main.py "Review this code: def factorial(n): return 1 if n <= 1 else n * factorial(n-1)"
```

## Configuration Options

### Change Temperature (Creativity)
```bash
export LLM_TEMPERATURE=0.9  # More creative
export LLM_TEMPERATURE=0.3  # More deterministic
```

### Increase Iterations
```bash
export MAX_ITERATIONS=15
```

### Enable Verbose Logging
```bash
export VERBOSE=True
```

## Running Examples

```bash
# Gemini-specific examples
python examples/gemini_examples.py

# General research tasks
python examples/research_task.py

# Code analysis
python examples/code_analysis.py

# Content planning
python examples/content_planning.py
```

## Troubleshooting

### "API key not found" Error
**Solution:**
```bash
# Check if environment variable is set
echo $GEMINI_API_KEY

# If empty, set it
export GEMINI_API_KEY="AIzaSy..."
```

### "ModuleNotFoundError: No module named 'langchain_google_genai'"
**Solution:**
```bash
pip install langchain-google-genai
```

### Agent responses are too short
**Solution:** Increase temperature and iterations
```python
agent = create_agent(
    provider="gemini",
    temperature=0.9,  # More creative
    max_iterations=15  # More steps
)
```

### Rate limit exceeded
**Solution:**
- Wait a few minutes before running again
- Gemini has generous free tier limits (60 requests/minute)
- Consider upgrading to paid plan for higher limits

### Connection timeout
**Solution:**
- Check your internet connection
- Try again (temporary server issues)
- Use OpenAI as fallback

## Best Practices

1. **Use appropriate temperature:**
   - 0.3-0.5: Factual research, code review
   - 0.7: General purpose (default)
   - 0.9: Creative tasks, brainstorming

2. **Set reasonable iterations:**
   - 5-10: Simple tasks
   - 10-15: Complex analysis
   - 20+: Very complex reasoning

3. **Batch process efficiently:**
   ```python
   tasks = ["task1", "task2", "task3"]
   results = agent.run_batch(tasks)
   ```

4. **Handle API errors:**
   ```python
   result = agent.run(task)
   if not result['success']:
       print(f"Error: {result['error']}")
   ```

## Performance Tips

- **Gemini is faster than GPT-4** for most general tasks
- **Use batch processing** for multiple tasks
- **Reduce verbosity** if logs are too large
- **Cache results** for repeated tasks

## Free Tier Limits

| Metric | Limit |
|--------|-------|
| Requests per minute | 60 |
| Tokens per minute | 300,000 |
| Daily quota | Effectively unlimited* |

*Within reasonable usage patterns

## Next Steps

1. ✅ Set up your API key
2. ✅ Install dependencies
3. ✅ Run your first task
4. 📚 Explore examples
5. 🛠️ Customize tools
6. 🚀 Deploy your agent

## Support

For issues:
- Check troubleshooting section above
- Review [Gemini API docs](https://ai.google.dev/)
- Check [LangChain docs](https://python.langchain.com/)

## Quick Reference

```bash
# Setup
export GEMINI_API_KEY="your-key"
pip install -r requirements.txt

# Run
python main.py "Your task here"

# Interactive
python main.py

# Batch
python examples/gemini_examples.py

# With options
export LLM_TEMPERATURE=0.9
export MAX_ITERATIONS=15
python main.py "Your task"
```

---

**Enjoy using your AI Research Agent with Gemini!** 🚀
