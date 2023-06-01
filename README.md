# Data-Engineering-Project-001-Youtube-Ad-Campaign-End-to-End-Project

## Project Name - Youtube Ad Campaign End-to-End Project

## Project Requirements

We have a client that wants to run new ad campaigns online and they have selected their main advertising channel as youtube. They want to understand some of the initial questions that they have, such as: how to categorize videos based on comments and stylistics and what factors affect how popular a youtube video will be. These are the things they want to understand before actually investing money in the youtube campaign. 


## Project Goals

We have data ingestion so we will have data coming from multiple sources then we will design an ETL pipeline to extract transform and load our data easily. We will also build a data lake so that we can easily organize our data and build a data pipeline around it. It should be scalable. So, we will be using AWS Cloud. In the end, we will build a dashboard to easily visualize and understand what is happening in the data. 


## Services and Resources

* **Amazon S3:** Amazon S3 is an object storage service that provides manufacturing scalability, data availability, security, and performance.
* **AWS IAM:** This is nothing but identity and access management which enables us to manage access to AWS services and resources securely.
* **Tableau:** Tableau is a visual analytics platform transforming the way we use data to solve problems—empowering people and organizations to make the most of their data.
* **AWS Glue:** A serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.
* **AWS Lambda:** Lambda is a computing service that allows programmers to run code without creating or managing servers.
* **AWS Athena:** Athena is an interactive query service for S3 in which there is no need to load data it stays in S3.

![ProjectArchitecture](img/youtubeAdCampaignArchitecture.jpg)


### Step 1: Datasets

For Youtube-Ad-Campaign End-to-End Project, the Kaggle - Trending YouTube Video Statistics dataset can be found at https://www.kaggle.com/datasets/datasnaek/youtube-new. 

This dataset includes several months (and counting) of data on daily trending YouTube videos. Data is included for the US, GB, DE, CA, FR, RU, MX, KR, JP, and IN regions (USA, Great Britain, Germany, Canada, France, Russia, Mexico, South Korea, Japan, and India respectively), with up to 200 listed trending videos per day.
Each region’s data is in a separate file. Data includes the video title, channel title, publish time, tags, views, likes and dislikes, description, and comment count.
The data also includes a `category_id` field, which varies between `region`. To retrieve the categories for a specific video, find it in the associated JSON. One such file is included for each of the five regions in the dataset.
Download the dataset with consists of `JSON` files and `CSV` files to your local machine.



### Step 2: Data Lake - Raw Bucket

Write scripts to load datasets from the local environment to S3 raw bucket. Using the AWS CLI and S3 API run the script `ingestion_local_to_raw.sh` to ingest the datasets from the local to raw bucket. 

The results of the initial EDA (Exploratory Data Analysis) are that the JSON files and the CSV files will need preprocessing before moving forward and creating a Glue Data Catalog. It is necessary to run a Glue Crawler to create a Data Catalog in order to analyze the raw dataset with Amazon Athena for ad hoc queries and analysis. 

The preliminary runs for the Glue Crawler run on top of the raw JSON and  raw CSV files shows:    

* The JSON files will need parsing and converting the dataset from JSON to Parquet format. 
* The CSV files need to convert certain column data types from `string` to `bigint` and the necessary conversion from CSV format to Parquet Format.



### Step 3: Data Lake - Cleansed Bucket

Using AWS Glue Studio, create a custom ETL for the preprocessing from CSV to Parquet format. The spark job was customized to partition the dataset by region. The spark job for preprocessing for the CSV file is  `etl_cleansed_csv_to_parquet.py`.

The JSON files will be preprocessed by AWS Lambda Function set to an S3 upload Trigger. The Lambda function `lambda_function.py` will parse the JSON file for the `item` key. Lambda will also transform the JSON file into Apache Parquet format. Create an S3 trigger to call the AWS Lambda function to execute whenever files are uploaded or modified in the raw bucket. 


**Step 4:** Reporting Bucket.
Created an ETL to build reporting layer which is a join of the two cleansed tables.  The `etl_parquet_analytics_version` ETL glue job will run an ETL to join the two cleanse tables 


## Data Analytics

**Step 5 :** Tableau Dashboard
Create a Dashboard by making a Connection from Tableau to Athena to access the reporting layer. In order to keep costs at a minumim, Tableau was used instead of QuickSight.

![ProjectAnalyticsReport](img/youtubeAdCampaignFinalAnalytics.jpg)


<u>Next Steps</u>

* Sentiment analysis in a variety of forms
* Categorising YouTube videos based on their comments and statistics.
* Training ML algorithms like RNNs to generate their own YouTube comments.
* Analysing what factors affect how popular a YouTube video will be.
* Statistical analysis over time