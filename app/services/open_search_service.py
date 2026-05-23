from opensearchpy import OpenSearch
from app.services.config import Config


class OpenSearchService:

    def __init__(self, config: Config = None):
        self.config = config or Config()

        self.client = OpenSearch(
            hosts=[
                {
                    "host": self.config.opensearch_host,
                    "port": self.config.opensearch_port
                }
            ],
            http_auth=(
                self.config.opensearch_user,
                self.config.opensearch_password
            ),
            use_ssl=True,
            verify_certs=False,
            ssl_assert_hostname=False,
            ssl_show_warn=False
        )

    def get_client(self):
        return self.client