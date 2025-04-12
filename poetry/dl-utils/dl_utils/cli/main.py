import click


@click.group()
def cli():
    """dl-utils: A CLI for AWS Data Lake operations using S3, EMR, and Athena."""
    pass

@cli.command()
@click.option('--bucket', required=True, help='Name of the S3 bucket to list contents from.')
def list_s3(bucket):
    """List objects in the specified S3 bucket."""
    import boto3
    s3 = boto3.client('s3')
    try:
        response = s3.list_objects_v2(Bucket=bucket)
        contents = response.get('Contents', [])
        if not contents:
            click.echo("Bucket is empty or inaccessible.")
            return
        for obj in contents:
            click.echo(obj['Key'])
    except Exception as e:
        click.echo(f"Error listing bucket contents: {e}")

@cli.command()
@click.option('--query', required=True, help='Athena SQL query to execute.')
@click.option('--database', required=True, help='Athena database name.')
@click.option('--output', required=True, help='S3 location to store query results.')
def run_athena_query(query, database, output):
    """Run a query on Athena."""
    import boto3
    client = boto3.client('athena')
    try:
        response = client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={'Database': database},
            ResultConfiguration={'OutputLocation': output}
        )
        click.echo(f"Query submitted. Execution ID: {response['QueryExecutionId']}")
    except Exception as e:
        click.echo(f"Failed to execute query: {e}")

@cli.command()
@click.option('--cluster-id', required=True, help='EMR cluster ID to run the step on.')
@click.option('--script-path', required=True, help='S3 path to the script to execute.')
def run_emr_step(cluster_id, script_path):
    """Add and run a step on an EMR cluster."""
    import boto3
    client = boto3.client('emr')
    try:
        step = {
            'Name': 'Run script',
            'ActionOnFailure': 'CONTINUE',
            'HadoopJarStep': {
                'Jar': 'command-runner.jar',
                'Args': ['spark-submit', script_path]
            }
        }
        response = client.add_job_flow_steps(JobFlowId=cluster_id, Steps=[step])
        step_id = response['StepIds'][0]
        click.echo(f"Step added. Step ID: {step_id}")
    except Exception as e:
        click.echo(f"Failed to add EMR step: {e}")
