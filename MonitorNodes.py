from kubernetes import watch
from kubernetes.client.rest import ApiException


class MonitorNodes():

    def __init__(self, kube_client, service_name, namespace):
        self.kube_client = kube_client
        self.service_name = service_name
        self.namespace = namespace

    def get_nodes(self):
        nodes_list = []
        nodes = self.kube_client.list_node()
        for node in nodes.items:
            for address in node.status.addresses:
                if address.type == "InternalIP":
                    nodes_list.append(address.address)
        return nodes_list

    def monitor_nodes(self):
        node_watch = watch.Watch()
        for event in node_watch.stream(self.kube_client.list_node, _request_timeout=60):
            if event["type"] == "ADDED":
                print("Event: %s" % event['type'])
                for address in event['object'].status.addresses:
                    if address.type == "InternalIP":
                        print("Event: %s %s" % (event['type'], address.address))
                        external_ips = self.get_nodes()
                        try:
                            print("Updating IP address with %s" % external_ips)
                            api_response = self.kube_client.patch_namespaced_service(self.service_name, self.namespace,
                                                                       {"spec": {"externalIPs": external_ips}})
                            print("Service External IP update success")
                        except ApiException as e:
                            print("Exception when calling CoreV1Api->create_namespaced_service: %s\n" % e)
                    elif address.type == "REMOVED":
                        print("Event: %s %s" % (event['type'], address.address))
