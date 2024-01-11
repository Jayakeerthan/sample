from typing import TextIO
import pandas as pd

from langchain_experimental.agents import create_csv_agent, create_pandas_dataframe_agent
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler  

Ollama(base_url='http://172.17.226.116:11434',
model="orca-mini:3b",temperature=0.8,top_k=40,top_p=0.9,repeat_penalty=1.1,repeat_last_n=64,tfs_z=1,
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))


def get_answer_csv(file: TextIO, query: str) -> str:
    """
    Returns the answer to the given query by querying a CSV file.

    Args:
    - file (str): the file path to the CSV file to query.
    - query (str): the question to ask the agent.

    Returns:
    - answer (str): the answer to the query from the CSV file.
    """


    
    agent = create_csv_agent(Ollama(temperature=0), file, verbose=False)

    answer = agent.run(query)
    return answer                                        