from kubernetes import client, config
import os


class KubeClient:

    def __init__(self, google_app_credentials=None):
        if google_app_credentials:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = google_app_credentials
            config.load_kube_config()
        else:
            config.load_incluster_config()

    @classmethod
    def get_kube_client(self):
        v1 = client.CoreV1Api()
        return v1
