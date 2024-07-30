from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import ECR, ECS
from diagrams.gcp.compute import Run
from diagrams.gcp.devtools import ContainerRegistry
from diagrams.onprem.ci import GithubActions
from diagrams.onprem.client import Client
from diagrams.onprem.vcs import Github

with Diagram(filename='dist/sample', show=False):
    with Cluster('ex) Git'):
        github = Github('GitHub')
        github_actions = GithubActions('GitHub Actions')
        github >> github_actions

    with Cluster('ex) AWS'):
        ecr = ECR('ECR')
        ecs = ECS('ECS')
        github_actions >> Edge(label='Push Image') >> ecr
        github_actions >> Edge(label='Deploy') >> ecs
        ecr >> Edge(label='Use Image') >> ecs

    with Cluster('ex) GCP'):
        artifact_registry = ContainerRegistry('Artifact Registry')
        cloud_run = Run('Cloud Run')
        github_actions >> Edge(label='Push Image') >> artifact_registry
        github_actions >> Edge(label='Deploy') >> cloud_run
        artifact_registry >> Edge(label='Use Image') >> cloud_run

    Client() >> Edge(label='Push Remote') >> github
