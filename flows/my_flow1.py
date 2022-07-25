import prefect
from prefect import task, Flow, Parameter
import sys, os
# sys.path.append(os.getcwd()) # this is needed to locate src/ and flows/
from src.my_module1 import my_function1 # import any functions from module dependencies located in src/
from flows.config_flows import get_flow_storage, RUN_CONFIG # import flow config shared by all flows

@task
def say_hi(name):
    logger = prefect.context.get("logger")
    logger.info("Hello, {}!".format(name))
    my_function1() # call function from module 

FLOW_NAME = "hello world"
STORAGE = get_flow_storage(flow_file="my_flow1.py") # flow filename 

with Flow(FLOW_NAME, storage=STORAGE, run_config=RUN_CONFIG,) as flow:
    name = Parameter('name') # set parameter in Prefect Cloud UI
    say_hi(name) # call task
