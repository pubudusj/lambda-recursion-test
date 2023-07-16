#!/usr/bin/env python3
import os

import aws_cdk as cdk

from lambda_recursion_test.lambda_recursion_test_stack import LambdaRecursionTestStack

personal_env = cdk.Environment(account="987919146615", region="eu-central-1")

app = cdk.App()
LambdaRecursionTestStack(app, "LambdaRecursionTestStack", env=personal_env)

app.synth()
