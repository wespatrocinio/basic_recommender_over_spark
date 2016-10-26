# basic_recommender_over_spark

A very simple recommender running over Spark developed just for evaluation of data science architecture and  development skills.

## Environment & stack requirements

This application requires the following stack and environment settings:

- Spark 2.0.0+
- All Python & Spark environment settings already set up
- Dataset file encoded as `UTF-8`
- Dataset in a valid JSON format

## Deploy instructions

As the proposal of this application is a proof of knowledge / concept, the deployment process is too simple as the application architecture. Thus, the deployment process is:

### Option 1

1. Download the zip file
2. Unzip the file into the directory of you preference
3. Configure the `src/settings.py` file with `DATA_SOURCE_PATH` pointing to your JSON file

### Option 2

1. Clone the repository from GitHub (https://github.com/wespatrocinio/basic_recommender_over_spark.git)
2. Follow the steps 2 and 3 from Option 1

## Running instruction

For running this application, execute the command from the `/src` directory:

```
spark-submit main.py
```
