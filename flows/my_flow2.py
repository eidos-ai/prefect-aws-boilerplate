import prefect
from prefect import task, Flow 
from src.my_module2 import my_function2 # import any functions from module dependencies located in src/
from flows.config_flows import get_flow_storage, RUN_CONFIG # import flow config shared by all flows

@task
def say_bye():
    logger = prefect.context.get("logger")
    logger.info("Goodbye from Prefect") 
    my_function2() # call function from module 

FLOW_NAME = "goodbye world"
STORAGE = get_flow_storage(flow_file="my_flow2.py") # flow filename 

with Flow(FLOW_NAME, storage=STORAGE, run_config=RUN_CONFIG,) as flow:
    say_bye() # call task
