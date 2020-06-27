from google.cloud import language_v1
from google.cloud.language_v1 import enums


def extract_entities(text):
    client = language_v1.LanguageServiceClient()
    type_ = enums.Document.Type.PLAIN_TEXT
    language = "en"
    document = {
        "content":text,
        "language":language,
        "type":type_
    }
    encoding_type=enums.EncodingType.UTF32

    response = client.analyze_entities(document,encoding_type=encoding_type)

    return response.entities

if __name__ == '__main__':
    text = """
    You have 2+ years experience in a data engineering role, creating complex SQL statements.
    With similar experience in custom ETL design, implementation and maintenance.
    You have minimum two years experience working with Spark or other distributed systems also, schema design and dimensional data modelling.
    Strong proficiency in at least one major language such as Python, Scala, or Java.
    Possess strong communication skills, and can effectively partner with analysts, product managers, engineers from across the business (Finance, Sales, Marketing, etc.)
    As a Data Engineer on the Business Intelligence team, you will live the Twilio Magic values:
    BE AN OWNER & BE BOLD: Work directly with the business (primarily analysts, engineers and product managers) to define the datasets they need to run the business, both internal to Twilio, and from external 3rd party systems.
    DRAW THE OWL: Build and launch robust real-time data processing pipelines and integrations, while simultaneously optimizing for performance and stakeholder requirements.
    WRITE IT DOWN: Ensure uptime and performance of data warehouse.
    EMPOWER OTHERS: Interact extensively across all functional teams within Twilio
    For the right candidate, this is fun work, creating and operating a massive data warehouse based on cutting-edge technologies like Kafka, Spark, Presto, and Redshift. The Business Intelligence team builds data ingestion, integration and transformation services using distributed frameworks that allow us to process and analyze large sets of data. In turn, we empower the business to make data-driven decisions at scale.
    Twilio is a company that is empowering the world’s developers with modern communication in order to build better applications. 
    Twilio is truly unique; we are a company committed to your growth, your learning, your development, and your entire employee experience. 
    We only win when our employees succeed and we're dedicated to helping you develop your strengths. 
    We invest in weeks dedicated to tackling hard problems and creating your own ideas. We have a cultural foundation built on diversity, inclusion and innovation and we want you and your ideas to thrive at Twilio.
    """
    entity_list = []
    for entity in extract_entities(text):
        if entity not in entity_list:
            if not str(entity.name).isnumeric():
                entity_list.append(str(entity.name).upper())

    print(entity_list)

