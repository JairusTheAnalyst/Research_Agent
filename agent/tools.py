"""Tool definitions for the Research Agent."""

from typing import Any
from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
import json


@tool
def web_search(query: str, max_results: int = 5) -> str:
    """
    Search the web for information about a given query.
    
    Args:
        query: The search query string
        max_results: Maximum number of results to return
        
    Returns:
        A formatted string with search results
    """
    try:
        # Using DuckDuckGo search (no API key needed)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        search_url = f"https://api.duckduckgo.com/?q={query}&format=json&no_html=1"
        response = requests.get(search_url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            results = response.json()
            
            # Extract abstract results
            abstracts = results.get('AbstractText', '')
            related = results.get('RelatedTopics', [])[:max_results]
            
            output = f"Search Results for '{query}':\n\n"
            if abstracts:
                output += f"Summary: {abstracts}\n\n"
            
            if related:
                output += "Related Information:\n"
                for item in related:
                    if 'Text' in item:
                        output += f"- {item['Text']}\n"
            
            return output if output.strip() else "No results found."
        else:
            return f"Search failed with status code {response.status_code}"
            
    except Exception as e:
        return f"Error during search: {str(e)}"


@tool
def analyze_text(text: str, analysis_type: str = "summary") -> str:
    """
    Analyze text content (summarize, extract key points, or analyze sentiment).
    
    Args:
        text: The text to analyze
        analysis_type: Type of analysis - 'summary', 'keypoints', or 'sentiment'
        
    Returns:
        Analysis results
    """
    if not text or len(text.strip()) == 0:
        return "Error: Empty text provided"
    
    # Simple text analysis (in production, use NLP library)
    lines = text.split('\n')
    word_count = len(text.split())
    sentence_count = len([s for s in text.split('.') if s.strip()])
    
    result = f"Text Analysis ({analysis_type}):\n"
    result += f"- Words: {word_count}\n"
    result += f"- Sentences: {sentence_count}\n"
    result += f"- Lines: {len(lines)}\n"
    
    if analysis_type == "keypoints":
        # Extract first sentence from each paragraph
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        result += f"\nKey Points ({len(paragraphs)} paragraphs):\n"
        for i, para in enumerate(paragraphs[:5], 1):
            first_sentence = para.split('.')[0] + '.'
            result += f"{i}. {first_sentence}\n"
    
    return result


@tool
def read_file(file_path: str) -> str:
    """
    Read the contents of a file.
    
    Args:
        file_path: Path to the file to read
        
    Returns:
        File contents or error message
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return f"File Contents ({file_path}):\n{content}"
    except FileNotFoundError:
        return f"Error: File not found - {file_path}"
    except Exception as e:
        return f"Error reading file: {str(e)}"


@tool
def list_files(directory: str = ".") -> str:
    """
    List files in a directory.
    
    Args:
        directory: Directory path to list
        
    Returns:
        List of files and directories
    """
    import os
    
    try:
        items = os.listdir(directory)
        output = f"Files in {directory}:\n"
        
        for item in sorted(items)[:20]:  # Limit to 20 items
            full_path = os.path.join(directory, item)
            if os.path.isdir(full_path):
                output += f"📁 {item}/\n"
            else:
                output += f"📄 {item}\n"
        
        if len(items) > 20:
            output += f"... and {len(items) - 20} more items"
        
        return output
    except Exception as e:
        return f"Error listing directory: {str(e)}"


@tool
def calculate(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    
    Args:
        expression: Mathematical expression to evaluate
        
    Returns:
        The result of the calculation
    """
    try:
        # Only allow safe mathematical operations
        allowed_names = {
            'abs': abs, 'round': round, 'sum': sum,
            'min': min, 'max': max,
            'pow': pow
        }
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return f"Result of '{expression}': {result}"
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"


@tool
def code_review(code: str, language: str = "python") -> str:
    """
    Analyze code for potential issues and improvements.
    
    Args:
        code: Code snippet to review
        language: Programming language
        
    Returns:
        Code review feedback
    """
    feedback = f"Code Review ({language}):\n\n"
    
    lines = code.split('\n')
    feedback += f"Lines of code: {len(lines)}\n"
    
    # Simple heuristic checks
    issues = []
    
    # Check for common issues
    for i, line in enumerate(lines, 1):
        if len(line) > 100:
            issues.append(f"Line {i}: Long line detected ({len(line)} chars)")
        if line.strip().startswith('#') and len(line.strip()) > 2:
            pass  # Comment, usually ok
        if 'TODO' in line or 'FIXME' in line:
            issues.append(f"Line {i}: TODO/FIXME found - {line.strip()}")
    
    if issues:
        feedback += "\nPotential Issues:\n"
        for issue in issues[:5]:
            feedback += f"- {issue}\n"
    else:
        feedback += "\nNo major issues detected.\n"
    
    feedback += "\nSuggestions:\n"
    feedback += "- Add type hints for better clarity\n"
    feedback += "- Include docstrings for functions\n"
    feedback += "- Add error handling where needed\n"
    
    return feedback


# Tool registry for easy access
TOOLS = [
    web_search,
    analyze_text,
    read_file,
    list_files,
    calculate,
    code_review,
]
