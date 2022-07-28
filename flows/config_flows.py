import os
from prefect.storage import GitHub
from prefect.run_configs import ECSRun

#flow config shared by all flows
ECS_CLUSTER_NAME="hello-world-Cluster" # existing cluster name
PREFECT_API_KEY=os.environ.get("PREFECT_API_KEY") # from github secrets
RUN_CONFIG = ECSRun(
    task_definition_arn="hello-world-TaskDefinition:4", # existing task definition name and revision
    labels=["prod"],
    run_task_kwargs=dict(cluster=f"{ECS_CLUSTER_NAME}", launchType="FARGATE",),
    env={"PREFECT__CLOUD__AGENT__LABELS":['prod'], "PREFECT__CLOUD__AGENT__LEVEL": "INFO",
        "PREFECT__CLOUD__API":"https://api.prefect.io", "PREFECT__CLOUD__USE_LOCAL_SECRETS":"False",
        "PREFECT__CLOUD__API_KEY":f"{PREFECT_API_KEY}"},
)
def get_flow_storage(flow_file):
    STORAGE = GitHub(
        repo="eidos-ai/prefect-aws-boilerplate", 
        path=f"flows/{flow_file}", # flows/my_flow.py
        # ref="my-branch", # branch name
        access_token_secret="GITHUB_ACCESS_TOKEN", # github token with (at least) read-only access from prefect cloud secrets
    )  
    return STORAGE