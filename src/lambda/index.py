import json
import os
import boto3

client = boto3.client("sqs")


def event_handler(event, _context):
    """Handles SQS events."""
    for record in event["Records"]:
        sqs_queue = os.environ.get("SQS_QUEUE_URL", "")

        client.send_message(
            QueueUrl=sqs_queue,
            MessageBody=json.dumps({"hello": "world"}),
        )
