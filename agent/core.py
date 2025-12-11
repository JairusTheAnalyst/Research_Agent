"""Core Research Agent implementation."""

from typing import Any, List, Optional, Dict
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from agent.tools import TOOLS
from agent.prompts import SYSTEM_PROMPT, TASK_PROMPT_TEMPLATE
from agent.utils import ExecutionTracker, print_section, print_thinking, print_action, print_result
import config
import time


class ResearchAgent:
    """
    An AI agent that performs research and task automation using the ReAct pattern.
    
    The agent uses reasoning and actions in a loop:
    - Think: Analyze the problem and plan an approach
    - Act: Execute tools to gather information
    - Observe: Process the results
    - Repeat: Continue until the task is complete
    
    Supports multiple LLM providers:
    - OpenAI (GPT-4, GPT-3.5)
    - Google Gemini
    """
    
    def __init__(
        self,
        provider: str = config.LLM_PROVIDER,
        model: Optional[str] = None,
        temperature: float = config.LLM_TEMPERATURE,
        max_iterations: int = config.MAX_ITERATIONS,
        verbose: bool = config.VERBOSE,
        api_key: Optional[str] = None
    ):
        """
        Initialize the Research Agent.
        
        Args:
            provider: LLM provider ("openai" or "gemini")
            model: The LLM model to use (auto-selected if None)
            temperature: Sampling temperature (0-1)
            max_iterations: Maximum number of agent iterations
            verbose: Whether to print detailed execution logs
            api_key: API key (uses env var if not provided)
        """
        self.provider = provider.lower()
        self.temperature = temperature
        self.max_iterations = max_iterations
        self.verbose = verbose
        self.tracker = ExecutionTracker()
        
        # Validate provider
        if self.provider not in ["openai", "gemini"]:
            raise ValueError(f"Unknown provider: {provider}. Use 'openai' or 'gemini'")
        
        # Initialize LLM based on provider
        self.llm = self._initialize_llm(provider, model, api_key)
        self.model = model or self._get_default_model(provider)
        
        # Initialize agent tools
        self.tools = self._prepare_tools()
        
        # Create the agent
        self.agent = None
        self.executor = None
        self._setup_agent()
    
    def _initialize_llm(self, provider: str, model: Optional[str], api_key: Optional[str]):
        """Initialize the LLM based on provider."""
        if provider == "openai":
            from langchain_openai import ChatOpenAI
            return ChatOpenAI(
                model=model or "gpt-4-turbo-preview",
                temperature=self.temperature,
                api_key=api_key or config.OPENAI_API_KEY
            )
        elif provider == "gemini":
            from langchain_google_genai import ChatGoogleGenerativeAI
            return ChatGoogleGenerativeAI(
                model=model or "gemini-pro",
                temperature=self.temperature,
                google_api_key=api_key or config.GEMINI_API_KEY,
                convert_system_message_to_human=True
            )
        else:
            raise ValueError(f"Unknown provider: {provider}")
    
    def _get_default_model(self, provider: str) -> str:
        """Get default model for provider."""
        if provider == "openai":
            return "gpt-4-turbo-preview"
        elif provider == "gemini":
            return "gemini-pro"
        return "unknown"
    
    def _prepare_tools(self) -> List[Tool]:
        """Prepare tools for the agent."""
        return list(TOOLS)
    
    def _setup_agent(self) -> None:
        """Set up the ReAct agent."""
        # Create the ReAct agent
        self.agent = create_react_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=PromptTemplate.from_template(
                SYSTEM_PROMPT + "\n\n" + TASK_PROMPT_TEMPLATE
            )
        )
        
        # Create the executor
        self.executor = AgentExecutor.from_agent_and_tools(
            agent=self.agent,
            tools=self.tools,
            max_iterations=self.max_iterations,
            verbose=self.verbose,
            handle_parsing_errors=True,
            early_stopping_method="generate"
        )
    
    def run(self, task: str) -> Dict[str, Any]:
        """
        Run the agent on a given task.
        
        Args:
            task: The task description
            
        Returns:
            A dictionary containing:
            - 'output': The agent's final answer
            - 'metrics': Execution metrics
            - 'success': Whether the task completed successfully
        """
        if self.verbose:
            print_section("RESEARCH AGENT STARTING", f"Task: {task}\nProvider: {self.provider}")
        
        self.tracker = ExecutionTracker()
        
        try:
            # Prepare the input
            agent_input = {
                "input": task,
                "intermediate_steps": []
            }
            
            # Run the agent
            if self.verbose:
                print_thinking("Analyzing task and planning approach...")
            
            start_time = time.time()
            result = self.executor.invoke(agent_input)
            execution_time = time.time() - start_time
            
            self.tracker.iterations = 1  # Simplified tracking
            
            if self.verbose:
                print_result(f"Task completed in {execution_time:.2f} seconds")
                print_section("FINAL ANSWER", result.get('output', ''))
            
            return {
                "output": result.get('output', ''),
                "metrics": {
                    "execution_time": round(execution_time, 2),
                    "provider": self.provider,
                    "model": self.model,
                    "success": True
                },
                "success": True
            }
            
        except Exception as e:
            error_msg = f"Agent execution failed: {str(e)}"
            if self.verbose:
                print_section("ERROR", error_msg)
            
            return {
                "output": f"Error: {str(e)}",
                "metrics": {},
                "success": False,
                "error": str(e)
            }
    
    def run_batch(self, tasks: List[str]) -> List[Dict[str, Any]]:
        """
        Run the agent on multiple tasks.
        
        Args:
            tasks: List of task descriptions
            
        Returns:
            List of results for each task
        """
        results = []
        for i, task in enumerate(tasks, 1):
            if self.verbose:
                print(f"\n[Task {i}/{len(tasks)}] {task}")
            result = self.run(task)
            results.append(result)
        
        return results
    
    def get_status(self) -> Dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "provider": self.provider,
            "model": self.model,
            "temperature": self.temperature,
            "max_iterations": self.max_iterations,
            "tools_available": len(self.tools),
            "tools": [tool.name for tool in self.tools]
        }


def create_agent(
    provider: str = config.LLM_PROVIDER,
    model: Optional[str] = None,
    verbose: bool = config.VERBOSE,
    **kwargs
) -> ResearchAgent:
    """
    Factory function to create a Research Agent.
    
    Args:
        provider: LLM provider ("openai" or "gemini")
        model: Specific model to use
        verbose: Whether to print detailed logs
        **kwargs: Additional arguments to pass to ResearchAgent
        
    Returns:
        A configured ResearchAgent instance
    """
    return ResearchAgent(provider=provider, model=model, verbose=verbose, **kwargs)
