import prefect

def my_function2():
    logger = prefect.context.get("logger")
    logger.info("This is test function #2")