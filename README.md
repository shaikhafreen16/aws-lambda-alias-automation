# aws-lambda-alias-automation
Automates the management of AWS Lambda function versions and aliases (DEV and PROD). Publishes new versions and updates aliases to point to the latest or new versions. Handles API throttling gracefully with retries.


Usage:
- Suitable for environments where Lambda functions are frequently updated and need version and alias management.
- Requires AWS credentials with Lambda permissions.

This tool simplifies Lambda versioning and alias updates, making it easier to manage deployment and staging environments.
