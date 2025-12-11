"""Example: Using Google Gemini with Research Agent

This example shows how to use Google's Gemini API instead of OpenAI.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.core import create_agent
from agent.utils import print_section


def gemini_research_example():
    """Run a research task using Gemini."""
    
    # Create agent with Gemini provider
    agent = create_agent(provider="gemini", verbose=True)
    
    # Example task
    task = """Research the latest developments in machine learning and provide:
    1. Recent breakthroughs (last 6 months)
    2. Key trends to watch
    3. Major applications
    Provide a concise summary."""
    
    print_section("GEMINI AGENT - RESEARCH TASK")
    print(f"Using: {agent.get_status()}\n")
    
    result = agent.run(task)
    
    if result['success']:
        print_section("RESULT")
        print(result['output'])
        
        print_section("METRICS")
        for key, value in result['metrics'].items():
            print(f"  {key}: {value}")
    else:
        print_section("ERROR", result.get('error', 'Unknown error'))


def gemini_code_review():
    """Use Gemini for code review."""
    
    agent = create_agent(provider="gemini", verbose=True)
    
    code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def process_list(items):
    result = []
    for item in items:
        if item > 0:
            result.append(item * 2)
    return result
"""
    
    task = f"""Review this Python code for quality and provide suggestions:

```python
{code}
```

Focus on:
1. Efficiency
2. Readability
3. Best practices
4. Potential improvements"""
    
    print_section("GEMINI - CODE REVIEW")
    result = agent.run(task)
    
    if result['success']:
        print_section("CODE REVIEW")
        print(result['output'])
    else:
        print_section("ERROR", result.get('error', 'Unknown error'))


def compare_providers():
    """Compare Gemini and OpenAI on the same task."""
    
    task = "Explain what makes a good software architecture in 3 bullet points"
    
    print_section("COMPARING PROVIDERS")
    print(f"Task: {task}\n")
    
    # Try Gemini
    print("=" * 60)
    print("GEMINI RESPONSE")
    print("=" * 60)
    try:
        gemini_agent = create_agent(provider="gemini", verbose=False)
        result = gemini_agent.run(task)
        if result['success']:
            print(result['output'][:500])
            print(f"\nExecution time: {result['metrics']['execution_time']}s")
        else:
            print("Failed - no Gemini API key?")
    except Exception as e:
        print(f"Error: {e}")
    
    # Try OpenAI
    print("\n" + "=" * 60)
    print("OPENAI RESPONSE")
    print("=" * 60)
    try:
        openai_agent = create_agent(provider="openai", verbose=False)
        result = openai_agent.run(task)
        if result['success']:
            print(result['output'][:500])
            print(f"\nExecution time: {result['metrics']['execution_time']}s")
        else:
            print("Failed - no OpenAI API key?")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("  GEMINI AGENT EXAMPLES")
    print("="*60)
    
    import os
    if os.getenv("GEMINI_API_KEY"):
        gemini_research_example()
    else:
        print("\n⚠️  GEMINI_API_KEY not set. Examples will fail.")
        print("Please set: export GEMINI_API_KEY='your-key-here'")
