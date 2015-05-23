#!/bin/bash

kill `ps -ef |grep wechat_ |awk '$3==1 {print $2}'`
