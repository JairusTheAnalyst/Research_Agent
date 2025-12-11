#!/usr/bin/env python
"""
Main entry point for the Research Agent.

Usage:
    python main.py "Your task here"                 # Uses default provider
    python main.py --provider gemini "Your task"    # Use Gemini
    python main.py --provider openai "Your task"    # Use OpenAI
    python main.py                                  # Interactive mode
"""

import sys
import os
from agent.core import create_agent
from agent.utils import print_section, print_result
import config


def interactive_mode(agent):
    """Run the agent in interactive mode."""
    print_section("INTERACTIVE MODE", "Type 'quit' or 'exit' to stop")
    
    while True:
        try:
            task = input("\n🎯 Enter your task: ").strip()
            
            if task.lower() in ['quit', 'exit', 'q']:
                print_result("Goodbye!")
                break
            
            if not task:
                print("⚠️  Please enter a task")
                continue
            
            print("\n⏳ Processing...")
            result = agent.run(task)
            
            if result['success']:
                print_section("RESULT")
                print(result['output'])
            else:
                print(f"❌ Error: {result.get('error', 'Unknown error')}")
        
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {str(e)}")


def command_line_mode(provider, task):
    """Run the agent with a single task."""
    agent = create_agent(provider=provider, verbose=True)
    result = agent.run(task)
    
    if result['success']:
        print_section("RESULT")
        print(result['output'])
        
        print_section("METRICS")
        for key, value in result['metrics'].items():
            print(f"  {key}: {value}")
        return 0
    else:
        print(f"❌ Error: {result.get('error', 'Unknown error')}")
        return 1


def show_help():
    """Display help message."""
    print("""
Research Agent - AI-Powered Task Automation

Usage:
    python main.py "Your task here"                 # Single task (default provider)
    python main.py --provider gemini "Your task"    # Use Gemini
    python main.py --provider openai "Your task"    # Use OpenAI
    python main.py                                  # Interactive mode
    python main.py --help                           # Show this help

Examples:
    python main.py "Research AI trends in 2025"
    python main.py --provider gemini "Review this code for best practices"
    python main.py --provider openai "Create a project plan for a mobile app"

Providers:
    gemini  - Google's Gemini API (free tier available)
    openai  - OpenAI's GPT models (more powerful)

Interactive Mode:
    Type your task at the prompt and press Enter
    Type 'quit' or 'exit' to stop

Environment Variables:
    GEMINI_API_KEY      - Your Google Gemini API key
    OPENAI_API_KEY      - Your OpenAI API key
    LLM_PROVIDER        - Default provider (default: gemini)
    LLM_TEMPERATURE     - Creativity level 0-1 (default: 0.7)
    MAX_ITERATIONS      - Max agent steps (default: 10)
    VERBOSE             - Show detailed logs (default: True)

For more information, see QUICKSTART.md or README.md
""")


def main():
    """Main entry point."""
    
    # Parse command line arguments
    provider = config.LLM_PROVIDER
    task = None
    
    # Check for help flag
    if len(sys.argv) > 1 and sys.argv[1] in ['--help', '-h', 'help']:
        show_help()
        return 0
    
    # Parse --provider flag
    if len(sys.argv) > 1 and sys.argv[1] == '--provider':
        if len(sys.argv) < 3:
            print("Error: --provider requires an argument (gemini or openai)")
            return 1
        provider = sys.argv[2]
        if len(sys.argv) > 3:
            task = ' '.join(sys.argv[3:])
    elif len(sys.argv) > 1:
        task = ' '.join(sys.argv[1:])
    
    # Check API keys
    if provider == "gemini" and not os.getenv('GEMINI_API_KEY'):
        print("""
❌ Gemini API key not found!

Please set your API key:
    export GEMINI_API_KEY="your-api-key-here"

Or create a .env file with:
    GEMINI_API_KEY=your-api-key-here

Get your free API key at: https://ai.google.dev/
""")
        return 1
    
    if provider == "openai" and not os.getenv('OPENAI_API_KEY'):
        print("""
❌ OpenAI API key not found!

Please set your API key:
    export OPENAI_API_KEY="sk-your-api-key-here"

Or create a .env file with:
    OPENAI_API_KEY=sk-your-api-key-here

Get your API key at: https://platform.openai.com/account/api-keys
""")
        return 1
    
    # Command line mode with task
    if task:
        return command_line_mode(provider, task)
    
    # Interactive mode
    try:
        agent = create_agent(provider=provider, verbose=False)
        status = agent.get_status()
        print_section("RESEARCH AGENT", f"Provider: {status['provider']}\nModel: {status['model']}")
        interactive_mode(agent)
        return 0
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        return 0
    except Exception as e:
        print(f"❌ Fatal error: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
