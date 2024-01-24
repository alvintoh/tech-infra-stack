from dagster import FilesystemIOManager, graph, op, repository, schedule
from dagster_docker import docker_executor


@op
def task_1():
    # Your logic for task 1 goes here
    return "output of task 1"

@op
def task_2():
    # Your logic for task 2 goes here
    return "output of task 2"

@op
def task_3(task_1_output, task_2_output):
    # Your logic for task 3 goes here
    # You can use task_1_output and task_2_output in this function
    return f"output of task 3 with inputs: {task_1_output}, {task_2_output}"

@graph
def my_graph():
    task_3_output = task_3(task_1(), task_2())
    # You can use task_3_output here if needed

# Specify the job definition
my_job = my_graph.to_job(name="test")


#my_step_isolated_job = my_graph.to_job(
#    name="my_step_isolated_job",
#    executor_def=docker_executor,
#    resource_defs={"io_manager": FilesystemIOManager(base_dir="/tmp/io_manager_storage")},
#)

# Specify the schedule definition
@schedule(cron_schedule="* * * * *", job=my_job, execution_timezone="US/Central")
def my_schedule(_context):
    return {}