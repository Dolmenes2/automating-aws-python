# coding: utf-8
event = {u'Records': [{u'eventVersion': u'2.1', u'eventTime': u'2019-06-10T13:50:48.122Z', u'requestParameters': {u'sourceIPAddress': u'86.131.109.207'}, u's3': {u'configurationId': u'e74cf466-f406-451d-9a09-e4c9fd434b06', u'object': {u'eTag': u'1f387fba463c68fd1c053cab2f0860b7', u'sequencer': u'005CFE5FFEDD729D30', u'key': u'Pexels+Videos+1936639S.mp4', u'size': 5166528}, u'bucket': {u'arn': u'arn:aws:s3:::dolmenes2videolyzervideos1234', u'name': u'dolmenes2videolyzervideos1234', u'ownerIdentity': {u'principalId': u'A1C4BWDOJF8XA'}}, u's3SchemaVersion': u'1.0'}, u'responseElements': {u'x-amz-id-2': u'3dYk1arNUcR0+mnhCsVX4lGtvDpmrv0dL+o+esM4WtfOJqAThWbbCxskRsSh1ngqq8q5kYViW38=', u'x-amz-request-id': u'A8D0CD4FB63E72EA'}, u'awsRegion': u'us-east-1', u'eventName': u'ObjectCreated:Put', u'userIdentity': {u'principalId': u'AWS:AIDAVV442ZXPH5MDPV4H3'}, u'eventSource': u'aws:s3'}]}
event
type(event)
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']
event['Records']
len(event['Records'])
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
