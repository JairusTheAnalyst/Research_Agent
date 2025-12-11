"""Utility functions for the Research Agent."""

import json
import time
from typing import Any, Dict, List


def format_tool_output(tool_name: str, output: str) -> str:
    """Format tool output for agent consumption."""
    return f"\n[Tool: {tool_name}]\n{output}\n"


def parse_json_output(text: str) -> Dict[str, Any]:
    """Attempt to parse JSON from text."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {}


def truncate_text(text: str, max_length: int = 500) -> str:
    """Truncate text to max length, adding ellipsis if needed."""
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text


def format_markdown(title: str, content: str, level: int = 2) -> str:
    """Format content as markdown."""
    header = "#" * level
    return f"{header} {title}\n\n{content}"


class ExecutionTracker:
    """Track agent execution metrics."""
    
    def __init__(self):
        self.start_time = time.time()
        self.tool_calls = []
        self.iterations = 0
    
    def log_tool_call(self, tool_name: str, duration: float):
        """Log a tool call."""
        self.tool_calls.append({
            "tool": tool_name,
            "duration": duration,
            "timestamp": time.time()
        })
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get execution metrics."""
        total_time = time.time() - self.start_time
        return {
            "total_time": round(total_time, 2),
            "iterations": self.iterations,
            "tool_calls": len(self.tool_calls),
            "tools_used": list(set(call["tool"] for call in self.tool_calls)),
            "average_tool_time": round(sum(c["duration"] for c in self.tool_calls) / len(self.tool_calls), 2) if self.tool_calls else 0
        }


def print_section(title: str, content: str = ""):
    """Print a formatted section."""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)
    if content:
        print(content)


def print_thinking(message: str):
    """Print agent thinking process."""
    print(f"\n🤔 {message}")


def print_action(message: str):
    """Print agent action."""
    print(f"\n⚡ {message}")


def print_result(message: str):
    """Print result."""
    print(f"\n✅ {message}")
