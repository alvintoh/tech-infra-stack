from dagster import repository
from schedules.schedules import my_job, my_schedule


@repository
def deploy_docker_repository():
    return [my_job, my_schedule]
