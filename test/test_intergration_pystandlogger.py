import pytest
import boto3

def test_kinesis_connection():
        client = boto3.client("kinesis")
        streams = client.list_streams()
        assert 0 < len(streams)
