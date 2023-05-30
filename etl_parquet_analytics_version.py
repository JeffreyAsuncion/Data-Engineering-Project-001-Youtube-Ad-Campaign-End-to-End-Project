import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node cleaned_raw_statistics
cleaned_raw_statistics_node1684420425305 = (
    glueContext.create_dynamic_frame.from_catalog(
        database="db_youtube_ad_campaign100_cleaned",
        table_name="raw_statistics",
        transformation_ctx="cleaned_raw_statistics_node1684420425305",
    )
)

# Script generated for node cleaned_statistics_reference_data
cleaned_statistics_reference_data_node1684420264948 = (
    glueContext.create_dynamic_frame.from_catalog(
        database="db_youtube_ad_campaign100_cleaned",
        table_name="cleaned_statistics_reference_data",
        transformation_ctx="cleaned_statistics_reference_data_node1684420264948",
    )
)

# Script generated for node Join
Join_node1684420902861 = Join.apply(
    frame1=cleaned_raw_statistics_node1684420425305,
    frame2=cleaned_statistics_reference_data_node1684420264948,
    keys1=["category_id"],
    keys2=["id"],
    transformation_ctx="Join_node1684420902861",
)

# Script generated for node S3 - analytics layer
S3analyticslayer_node1684422448474 = glueContext.getSink(
    path="s3://de-youtube-ad-campaign100-analytics-useast1-dev",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["region", "category_id"],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="S3analyticslayer_node1684422448474",
)
S3analyticslayer_node1684422448474.setCatalogInfo(
    catalogDatabase="db_youtube_ad_campaign100_analytics",
    catalogTableName="final_analytics",
)
S3analyticslayer_node1684422448474.setFormat("glueparquet")
S3analyticslayer_node1684422448474.writeFrame(Join_node1684420902861)
job.commit()
