from flows.my_flow1 import flow as flow1 # rename flow from my_flow1.py as flow1 
from flows.my_flow2 import flow as flow2 # rename flow from my_flow2.py as flow2 and so on... 

flow1.register(project_name="hello-world") # register flow1
flow2.register(project_name="hello-world") # register flow2