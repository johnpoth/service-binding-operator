import re

from openshift import Openshift


class ServiceBinding(object):

    openshift = Openshift()

    def create(self, yaml):
        return re.search(r'.*servicebinding.operators.coreos.com/.*(created|unchanged)', self.attempt_to_create(yaml))

    def attempt_to_create(self, yaml):
        return self.openshift.oc_apply(yaml)

    def get_servicebinding_info_by_jsonpath(self, servicebinding_name, namespace, json_path):
        openshift = Openshift()
        return openshift.get_resource_info_by_jsonpath("servicebinding", servicebinding_name, namespace, json_path)
