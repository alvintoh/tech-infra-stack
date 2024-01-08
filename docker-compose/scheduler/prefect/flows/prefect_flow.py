from prefect import flow, task
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule

@task(name="Task 1")
def task1():
    print("Task 1")
    return "Result from Task 1"

@task(name="Task 2")
def task2():
    print("Task 2")
    return "Result from Task 2"

@task(name="Task 3")
def task3(result1, result2):
    print("Task 3")
    print(f"Received: {result1} and {result2}")
    return "Result from Task 3"

# Define your flow
@flow(flow_run_name="flow_run_name_test", name="Example Flow Task")
def flowtask():
    result1 = task1()
    result2 = task2()
    result3 = task3(result1, result2)

# Create a new deployment using configuration defaults for an imported flow
deployment = Deployment.build_from_flow(
    flow=flowtask,
    name="flow_run_name_test",
    schedule=(CronSchedule(cron="* * * * *", timezone="America/Chicago")),
    version="1",
    tags=["demo"],
)
deployment.apply()