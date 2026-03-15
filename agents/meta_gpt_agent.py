```json
{
    "agents/meta_gpt_agent.py": {
        "content": "
import logging
from typing import Dict, List
from langfuse import LangGraph
from letta import MemGPT

class MetaGPTAgent:
    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initialize the MetaGPTAgent with non-stationary drift index and stochastic regime switch.

        Args:
        - non_stationary_drift_index (float): The index of non-stationary drift.
        - stochastic_regime_switch (bool): Whether to enable stochastic regime switch.
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch
        self.lang_graph = LangGraph()
        self.mem_gpt = MemGPT()
        logging.basicConfig(level=logging.INFO)

    def manage_context_window(self, context_window_size: int) -> None:
        """
        Manage the context window size for the MetaGPTAgent.

        Args:
        - context_window_size (int): The size of the context window.

        Returns:
        - None
        """
        try:
            self.mem_gpt.update_context_window(context_window_size)
            logging.info(f'Context window size updated to {context_window_size}')
        except Exception as e:
            logging.error(f'Error updating context window size: {e}')

    def update_long_term_memory(self, memory_update: Dict[str, str]) -> None:
        """
        Update the long-term memory of the MetaGPTAgent.

        Args:
        - memory_update (Dict[str, str]): The update to the long-term memory.

        Returns:
        - None
        """
        try:
            self.mem_gpt.update_long_term_memory(memory_update)
            logging.info(f'Long-term memory updated: {memory_update}')
        except Exception as e:
            logging.error(f'Error updating long-term memory: {e}')

    def generate_state_graph(self, state_graph_input: List[str]) -> str:
        """
        Generate the state graph for the MetaGPTAgent.

        Args:
        - state_graph_input (List[str]): The input to the state graph.

        Returns:
        - str: The generated state graph.
        """
        try:
            state_graph = self.lang_graph.generate_state_graph(state_graph_input)
            logging.info(f'State graph generated: {state_graph}')
            return state_graph
        except Exception as e:
            logging.error(f'Error generating state graph: {e}')
            return ''

    def simulate_rocket_science(self, rocket_science_input: Dict[str, str]) -> str:
        """
        Simulate the rocket science problem.

        Args:
        - rocket_science_input (Dict[str, str]): The input to the rocket science simulation.

        Returns:
        - str: The result of the rocket science simulation.
        """
        try:
            result = self.mem_gpt.simulate_rocket_science(rocket_science_input)
            logging.info(f'Rocket science simulation result: {result}')
            return result
        except Exception as e:
            logging.error(f'Error simulating rocket science: {e}')
            return ''

if __name__ == '__main__':
    meta_gpt_agent = MetaGPTAgent(non_stationary_drift_index=0.5, stochastic_regime_switch=True)
    meta_gpt_agent.manage_context_window(context_window_size=1024)
    meta_gpt_agent.update_long_term_memory(memory_update={'key': 'value'})
    state_graph = meta_gpt_agent.generate_state_graph(state_graph_input=['input1', 'input2'])
    rocket_science_result = meta_gpt_agent.simulate_rocket_science(rocket_science_input={'input1': 'value1', 'input2': 'value2'})
    print(f'State graph: {state_graph}')
    print(f'Rocket science result: {rocket_science_result}'
        ",
        "commit_message": "feat: implement specialized meta_gpt_agent logic"
    }
}
```