```json
{
    "agents/letta_agent.py": {
        "content": "
import logging
from typing import Dict, List
from langfuse import LangGraph, StateGraph
from letta import LettaAgent, MemoryManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LettaAgentImpl(LettaAgent):
    def __init__(self, non_stationary_drift_index: int, stochastic_regime_switch: bool):
        """
        Initialize the Letta agent with non-stationary drift index and stochastic regime switch.

        Args:
        - non_stationary_drift_index (int): The index of non-stationary drift.
        - stochastic_regime_switch (bool): Whether to enable stochastic regime switch.
        """
        super().__init__()
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch
        self.memory_manager = MemoryManager()

    def manage_context_window(self, context_window: List[str]) -> None:
        """
        Manage the context window of the agent.

        Args:
        - context_window (List[str]): The context window to manage.
        """
        try:
            self.memory_manager.update_context_window(context_window)
            logger.info('Context window updated successfully')
        except Exception as e:
            logger.error(f'Error updating context window: {e}')

    def update_long_term_memory(self, new_memory: Dict[str, str]) -> None:
        """
        Update the long-term memory of the agent.

        Args:
        - new_memory (Dict[str, str]): The new memory to update.
        """
        try:
            self.memory_manager.update_long_term_memory(new_memory)
            logger.info('Long-term memory updated successfully')
        except Exception as e:
            logger.error(f'Error updating long-term memory: {e}')

    def run_experiment(self, experiment_input: str) -> str:
        """
        Run an experiment using the agent.

        Args:
        - experiment_input (str): The input for the experiment.

        Returns:
        - str: The result of the experiment.
        """
        try:
            lang_graph = LangGraph()
            state_graph = StateGraph(lang_graph)
            result = state_graph.run_experiment(experiment_input)
            logger.info(f'Experiment result: {result}')
            return result
        except Exception as e:
            logger.error(f'Error running experiment: {e}')
            return None

if __name__ == '__main__':
    # Simulation of the 'Rocket Science' problem
    letta_agent = LettaAgentImpl(non_stationary_drift_index=10, stochastic_regime_switch=True)
    context_window = ['launch', 'rocket', 'science']
    letta_agent.manage_context_window(context_window)
    new_memory = {'rocket': 'science'}
    letta_agent.update_long_term_memory(new_memory)
    experiment_input = 'launch rocket'
    result = letta_agent.run_experiment(experiment_input)
    print(f'Result: {result}')
",
        "commit_message": "feat: implement specialized letta_agent logic"
    }
}
```