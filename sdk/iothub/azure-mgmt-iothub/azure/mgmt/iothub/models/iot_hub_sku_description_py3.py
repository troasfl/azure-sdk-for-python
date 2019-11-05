# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IotHubSkuDescription(Model):
    """SKU properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar resource_type: The type of the resource.
    :vartype resource_type: str
    :param sku: Required. The type of the resource.
    :type sku: ~azure.mgmt.iothub.models.IotHubSkuInfo
    :param capacity: Required. IotHub capacity
    :type capacity: ~azure.mgmt.iothub.models.IotHubCapacity
    """

    _validation = {
        'resource_type': {'readonly': True},
        'sku': {'required': True},
        'capacity': {'required': True},
    }

    _attribute_map = {
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'IotHubSkuInfo'},
        'capacity': {'key': 'capacity', 'type': 'IotHubCapacity'},
    }

    def __init__(self, *, sku, capacity, **kwargs) -> None:
        super(IotHubSkuDescription, self).__init__(**kwargs)
        self.resource_type = None
        self.sku = sku
        self.capacity = capacity