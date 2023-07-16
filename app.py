#!/usr/bin/env python3
import os

import aws_cdk as cdk

from lambda_recursion_test.lambda_recursion_test_stack import LambdaRecursionTestStack

app = cdk.App()
LambdaRecursionTestStack(app, "LambdaRecursionTestStack")

app.synth()
