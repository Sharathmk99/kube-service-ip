
from KubeClient import KubeClient
from MonitorNodes import MonitorNodes
import os

if __name__ == '__main__':
    service_name = os.environ["KUBESERVICEIP_SERVICENAME"]
    namespace_name = os.environ["KUBESERVICEIP_NAMESPACE"]
    kube_client = KubeClient()
    client = kube_client.get_kube_client()
    monitor_nodes = MonitorNodes(client, service_name, namespace_name)
    kube_nodes = monitor_nodes.get_nodes()
    print("Current Nodes %s" % kube_nodes)
    monitor_nodes.monitor_nodes()
