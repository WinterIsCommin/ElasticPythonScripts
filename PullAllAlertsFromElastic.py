from elasticsearch import Elasticsearch
# Elasticsearch setup
ELASTIC_URL = 'https://example.com:9200'
INDEX_NAME = 'internal.alerts-security.alerts-default-000001'
AUTH = ('username', 'password')  # If you use Basic Authentication

# Initialize Elasticsearch client
es = Elasticsearch([ELASTIC_URL], basic_auth=AUTH, verify_certs=False)


def fetch_alerts():
    # This is a very basic query to get all documents. Adjust as needed.
    query = {
        "query": {
            "match_all": {}
        }
    }

    try:
        results = es.search(index='*alerts-security*', query={'match_all': {}}, size=5, sort={"signal.original_event.created": {"order": "desc"}})
        return results.get("hits", {}).get("hits", [])
    except Exception as e:
        print(f"Error: {e}")
        return []


if __name__ == "__main__":
    alerts = fetch_alerts()
    for alert in alerts:
        print(alert)
