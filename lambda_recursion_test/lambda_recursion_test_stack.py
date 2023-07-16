from aws_cdk import (
    CfnOutput,
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as lambda_,
    aws_lambda_event_sources as event_sources,
    aws_logs as logs,
)
from constructs import Construct


class LambdaRecursionTestStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Dead Letter Queue
        dlq = sqs.Queue(
            self,
            "RecursionTestDLQ",
        )

        # SQS queue
        queue = sqs.Queue(
            self,
            "RecursionTestSQSQueue",
            dead_letter_queue=sqs.DeadLetterQueue(max_receive_count=1, queue=dlq),
        )

        # Lambda function
        lambda_function = lambda_.Function(
            scope=self,
            id="RecursionTestLambdaFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="index.event_handler",
            code=lambda_.Code.from_asset("src/lambda"),
            timeout=Duration.seconds(10),
            memory_size=128,
            environment={"SQS_QUEUE_URL": queue.queue_url},
            dead_letter_queue=dlq,
        )
        # Add permission for Lambda function to send messages to SQS Queueu
        queue.grant_send_messages(lambda_function)
        # Create SQS event source
        sqs_event_source = event_sources.SqsEventSource(queue)
        # Add event source to Lambda function
        lambda_function.add_event_source(sqs_event_source)

        # Log group for Lambda function
        logs.LogGroup(
            self,
            "LambdaLogGroup",
            log_group_name=f"/aws/lambda/{lambda_function.function_name}",
            retention=logs.RetentionDays.ONE_DAY,
        )

        # Output
        CfnOutput(self, "SQSQueue", value=queue.queue_arn)
        CfnOutput(self, "LambdaFunction", value=lambda_function.function_arn)
