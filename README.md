# Tech Infra Stack

## Table of Contents

1. [Introduction](#1-introduction)
2. [Code Repository Structure](#2-code-repository-structure)
3. [Developer Guide](#3-developer-guide)
   - [Running Locally](#31-running-locally)
   - [Running Database Services](#32-running-database-services)
   - [Running Queue Services](#33-running-queue-services)
   - [Running Scheduler Services](#34-running-scheduler-services)

## 1. Introduction

This repository contains the common tech infrastructure services for local development.

## 2. Code Repository Structure

The repository is made up of the following folders:


```
tech-infra-stack/               ## Root directory for technology infrastructure stack
  - docker-compose/             ## Contains Docker Compose orchestration files for local deployment
    - database/                 ## Contains Docker Compose files applicable for specific database
    - queue/                    ## Contains Docker Compose files applicable for specific queue
    - scheduler/                ## Contains Docker Compose files applicable for specific scheduler
```

Please create any new content in the appropriate folders.

## 3. Developer Guide

### 3.1 Running Locally

Local deployment can be performed via the use of docker-compose. Setup files are located in `/docker-compose` and consist of the following:

```
/docker-compose/<infra-type>/<service-name>
  - docker-compose-x86.yml   ## docker-compose file for x86 users. 
```

All services in the docker-compose files have been categorized into the following profiles:

### 3.2 Running Database Services

To run the databases services, use the following command:

Add into docker-compose command below to select cache with database or database only
- `--profile cache_database` 
- `--profile database` 

```
[x86 machines]
docker-compose -f docker-compose/database/<service-name>/docker-compose-x86.yml up -d
```
### 3.3 Running queue Services

To run the queue services, use the following command:

```
[x86 machines]
docker-compose -f docker-compose/queue/<service-name>/docker-compose-x86.yml up -d
```

### 3.4 Running scheduler Services

To run the scheduler services, use the following command:

```
[x86 machines]
docker-compose -f docker-compose/scheduler/<service-name>/docker-compose-x86.yml up -d
```