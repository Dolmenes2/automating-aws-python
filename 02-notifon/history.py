# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
ec2.SecurityGroup()
ec2.SecurityGroup(all)
sg=ec2.SecurityGroup(all)
sg
security_group_iterator = ec2.security_groups.all()
security_group_iterator
list(ec2.SecurityGroup)
list(security_group_iterator)
ec2.SecurityGroup('sg-826753ed')
list(ec2.SecurityGroup('sg-826753ed'))
ec2.SecurityGroup
sg-82=ec2.SecurityGroup('sg-826753ed')
sg82 = ec2.SecurityGroup('sg-826753ed')
sg82
list(sg82)
list(ec2.security_groups.all())
instance_iterator = ec2.instances.all()
instance_iterator
class Pet(object):
   def my_method(self):
      print("I am a Cat")
cat = Pet()
cat.my_method()
cat
security_group_iterator
list(ec2.SecurityGroup)
list(ec2.Instance)
ec2.Instance[0]
instance_iterator = ec2.instances.all()
instance_iterator
security_group = ec2.SecurityGroup('sg-826753ed')
response = security_group.authorize_ingress(CidrIp='myIP/32', FromPort=22, IpProtocol='tcp', ToPort=22)
security_group = ec2.SecurityGroup('sg-826753ed')
response = security_group.authorize_ingress(CidrIp='86.139.142.27/32', FromPort=22, IpProtocol='tcp', ToPort=22)
security_group.name
security_group.description
security_group.ip_permissions
security_group.group_name
security_group.group_id
security_group
security_group = ec2.SecurityGroup('sg-826753ed')
response = security_group.authorize_ingress(IpPermissions=[{'IpRanges':[{CidrIp:'86.139.142.27/32'}], 'FromPort'=22, 'IpProtocol'='tcp', 'ToPort'=22)}]
security_group = ec2.SecurityGroup('sg-826753ed')
response = security_group.authorize_ingress(IpPermissions=[{'IpRanges':[{CidrIp:'86.139.142.27/32'}], 'FromPort'=53, 'IpProtocol'='tcp', 'ToPort'=53}])
security_group = ec2.SecurityGroup('sg-826753ed')
response = security_group.authorize_ingress(IpPermissions=[{'IpRanges':[{CidrIp:'86.139.142.27/32'}], 'FromPort':53, 'IpProtocol':'tcp', 'ToPort':53}])
security_group = ec2.SecurityGroup('sg-826753ed')
response = security_group.authorize_ingress(IpPermissions=[{'IpRanges':[{'CidrIp':'86.139.142.27/32'}], 'FromPort':53, 'IpProtocol':'tcp', 'ToPort':53}])
security_group.ip_permissions
