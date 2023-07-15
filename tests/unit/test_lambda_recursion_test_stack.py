import aws_cdk as core
import aws_cdk.assertions as assertions

from lambda_recursion_test.lambda_recursion_test_stack import LambdaRecursionTestStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lambda_recursion_test/lambda_recursion_test_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LambdaRecursionTestStack(app, "lambda-recursion-test")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
