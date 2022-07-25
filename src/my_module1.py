import prefect, os
# from dotenv import load_dotenv 

# load_dotenv() 
# my_env_var = os.getenv("MY_ENV_VARIABLE")

def my_function1():
    logger = prefect.context.get("logger")
    logger.info("This is test function #1")
    # logger.info(f"This is my environment variable: {my_env_var}")