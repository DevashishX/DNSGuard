#!/usr/bin/bash

gzip -c /home/ec2-user/DNSGuard/DNSGuard.log.1 > /tmp/DNSGuard_log.gz

# --debug
aws s3 cp /tmp/DNSGuard_log.gz s3://administrator-niramay-s3-asia-pacific-mumbai/logs/DNSGuard_`date +%Y-%m-%d_%H:%M:%S`.log.gz --profile administrator-niramay
