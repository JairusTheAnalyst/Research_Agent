"""Example: Research Task Automation

This example demonstrates the agent researching a topic and providing
comprehensive findings.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.core import create_agent
from agent.utils import print_section, print_result


def research_task_example():
    """Run a research task example."""
    
    # Create the agent
    agent = create_agent(verbose=True)
    
    # Example task
    task = """Research the latest developments in AI agents and summarize:
    1. Key recent breakthroughs
    2. Main applications in production
    3. Current challenges the field faces
    Provide a structured summary."""
    
    # Run the agent
    print_section("STARTING RESEARCH TASK")
    result = agent.run(task)
    
    # Display results
    if result['success']:
        print_section("RESEARCH SUMMARY")
        print(result['output'])
        
        print_section("EXECUTION METRICS")
        for key, value in result['metrics'].items():
            print(f"  {key}: {value}")
    else:
        print_section("ERROR", result.get('error', 'Unknown error'))


def batch_research_example():
    """Run multiple research tasks."""
    
    agent = create_agent(verbose=False)
    
    tasks = [
        "What are the main differences between generative AI and traditional machine learning?",
        "List the top 5 programming languages for AI development in 2025",
        "Explain the ReAct pattern in AI agents"
    ]
    
    print_section("BATCH RESEARCH TASKS")
    print(f"Running {len(tasks)} research tasks...\n")
    
    results = agent.run_batch(tasks)
    
    for i, (task, result) in enumerate(zip(tasks, results), 1):
        print_section(f"Task {i}: {task[:50]}...")
        if result['success']:
            print(result['output'][:300] + "...")
        else:
            print(f"Failed: {result.get('error', 'Unknown error')}")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("  RESEARCH AGENT - EXAMPLE USAGE")
    print("="*60)
    
    try:
        research_task_example()
    except Exception as e:
        print(f"\n❌ Error running example: {str(e)}")
        print("\nMake sure you have:")
        print("1. Installed dependencies: pip install -r requirements.txt")
        print("2. Set OPENAI_API_KEY environment variable")
