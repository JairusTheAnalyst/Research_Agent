"""Example: Content Planning and Strategy

This example demonstrates the agent creating content plans and strategies.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.core import create_agent
from agent.utils import print_section


def content_planning_example():
    """Run a content planning task."""
    
    agent = create_agent(verbose=True)
    
    task = """Create a comprehensive content strategy for a technology blog focused on AI and machine learning.

Please provide:
1. Target audience analysis
2. Content pillars (5-7 main topics)
3. Content calendar for the next 3 months
4. SEO strategy and keyword recommendations
5. Distribution channels and tactics
6. Engagement metrics to track
7. Content format mix recommendations

Format the output as a structured plan."""
    
    print_section("CONTENT PLANNING TASK")
    result = agent.run(task)
    
    if result['success']:
        print_section("CONTENT STRATEGY")
        print(result['output'])
    else:
        print_section("ERROR", result.get('error', 'Unknown error'))


def project_planning_example():
    """Run a project planning task."""
    
    agent = create_agent(verbose=True)
    
    task = """Plan a 6-month software development project for building a mobile app with these requirements:
- iOS and Android support
- User authentication and profiles
- Real-time notifications
- Cloud database backend
- Payment integration
- Analytics tracking

Provide:
1. Project phases and timeline
2. Resource requirements (team composition)
3. Technology stack recommendations
4. Risk assessment and mitigation
5. Milestone definitions
6. Quality assurance strategy
7. Deployment plan"""
    
    print_section("PROJECT PLANNING TASK")
    result = agent.run(task)
    
    if result['success']:
        print_section("PROJECT PLAN")
        print(result['output'])
    else:
        print_section("ERROR", result.get('error', 'Unknown error'))


if __name__ == "__main__":
    print("\n" + "="*60)
    print("  CONTENT PLANNING EXAMPLE")
    print("="*60)
    
    try:
        content_planning_example()
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
