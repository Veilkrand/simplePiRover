#!/bin/bash

systemctl stop videoServer.service
systemctl disable videoServer.service

systemctl stop robotServer.service
systemctl disable robotServer.service
