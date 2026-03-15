```json
{
    "utils/agent_utils.py": {
        "content": "
import logging
from typing import Dict, List
from langfuse import StateGraph
from letta import MemoryManager

logging.basicConfig(level=logging.INFO)

def manage_non_stationary_drift_index(
    drift_index: List[float], 
    stochastic_regime_switch: bool = False
) -> Dict[str, float]:
    """
    Manage non-stationary drift index for stateful AI agents.

    Args:
    - drift_index (List[float]): List of drift index values.
    - stochastic_regime_switch (bool): Whether to apply stochastic regime switch. Defaults to False.

    Returns:
    - Dict[str, float]: Managed drift index dictionary.
    """
    try:
        logging.info('Managing non-stationary drift index...')
        managed_drift_index = {}
        for i, value in enumerate(drift_index):
            if stochastic_regime_switch:
                # Apply stochastic regime switch
                value = value * (1 + (i % 2))
            managed_drift_index[f'drift_{i}'] = value
        return managed_drift_index
    except Exception as e:
        logging.error(f'Error managing drift index: {e}')
        return {}

def update_agent_context_window(
    agent_state: Dict[str, str], 
    context_window_size: int = 10
) -> Dict[str, str]:
    """
    Update agent context window using Letta memory management.

    Args:
    - agent_state (Dict[str, str]): Current agent state.
    - context_window_size (int): Size of the context window. Defaults to 10.

    Returns:
    - Dict[str, str]: Updated agent state.
    """
    try:
        logging.info('Updating agent context window...')
        memory_manager = MemoryManager()
        updated_agent_state = memory_manager.update_context_window(agent_state, context_window_size)
        return updated_agent_state
    except Exception as e:
        logging.error(f'Error updating context window: {e}')
        return {}

def visualize_state_graph(
    state_graph: StateGraph
) -> None:
    """
    Visualize state graph using Langfuse.

    Args:
    - state_graph (StateGraph): State graph to visualize.
    """
    try:
        logging.info('Visualizing state graph...')
        state_graph.visualize()
    except Exception as e:
        logging.error(f'Error visualizing state graph: {e}')

if __name__ == '__main__':
    # Simulate 'Rocket Science' problem
    drift_index = [0.1, 0.2, 0.3, 0.4, 0.5]
    stochastic_regime_switch = True
    managed_drift_index = manage_non_stationary_drift_index(drift_index, stochastic_regime_switch)
    logging.info(f'Managed drift index: {managed_drift_index}')

    agent_state = {'context': 'initial context'}
    context_window_size = 10
    updated_agent_state = update_agent_context_window(agent_state, context_window_size)
    logging.info(f'Updated agent state: {updated_agent_state}')

    state_graph = StateGraph()
    visualize_state_graph(state_graph)
",
        "commit_message": "feat: implement specialized agent_utils logic"
    }
}
```