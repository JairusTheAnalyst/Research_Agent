"""Example: Code Analysis and Review

This example demonstrates the agent reviewing code and providing
feedback and improvement suggestions.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.core import create_agent
from agent.utils import print_section


SAMPLE_CODE = """
def calculate_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total / len(numbers)

def process_data(raw_data):
    result = []
    # TODO: Add error handling
    for item in raw_data:
        processed = item.strip().upper()
        result.append(processed)
    return result

class DataProcessor:
    def __init__(self):
        self.data = []
    
    def add(self, item):
        self.data.append(item)
    
    def process(self):
        # FIXME: This is inefficient for large datasets
        return [x * 2 for x in self.data if isinstance(x, int)]
"""


def code_review_example():
    """Run a code review task."""
    
    agent = create_agent(verbose=True)
    
    task = f"""Please review the following Python code and provide:
1. Code quality assessment
2. Potential bugs or issues
3. Performance concerns
4. Refactoring suggestions
5. Best practices recommendations

Code to review:
```python
{SAMPLE_CODE}
```

Provide detailed, actionable feedback."""
    
    print_section("CODE REVIEW TASK")
    result = agent.run(task)
    
    if result['success']:
        print_section("CODE REVIEW FEEDBACK")
        print(result['output'])
    else:
        print_section("ERROR", result.get('error', 'Unknown error'))


def architecture_design_example():
    """Run an architecture design task."""
    
    agent = create_agent(verbose=True)
    
    task = """Design the architecture for a web-based task management system that:
1. Allows users to create, edit, and delete tasks
2. Supports task priorities and due dates
3. Enables task sharing between team members
4. Provides analytics and reporting
5. Must handle 10,000+ concurrent users

Please provide:
- System architecture diagram (described in text)
- Key components and their responsibilities
- Technology stack recommendations
- Database schema overview
- Scalability considerations"""
    
    print_section("ARCHITECTURE DESIGN TASK")
    result = agent.run(task)
    
    if result['success']:
        print_section("ARCHITECTURE DESIGN")
        print(result['output'])
    else:
        print_section("ERROR", result.get('error', 'Unknown error'))


if __name__ == "__main__":
    print("\n" + "="*60)
    print("  CODE ANALYSIS EXAMPLE")
    print("="*60)
    
    try:
        code_review_example()
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
