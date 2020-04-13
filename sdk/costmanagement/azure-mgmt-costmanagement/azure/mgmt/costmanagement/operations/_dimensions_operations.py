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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class DimensionsOperations(object):
    """DimensionsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Version of the API to be used with the client request. The current version is 2019-11-01. Constant value: "2019-11-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2019-11-01"

        self.config = config

    def list(
            self, scope, filter=None, expand=None, skiptoken=None, top=None, custom_headers=None, raw=False, **operation_config):
        """Lists the dimensions by the defined scope.

        :param scope: The scope associated with dimension operations. This
         includes '/subscriptions/{subscriptionId}/' for subscription scope,
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}'
         for resourceGroup scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for
         Billing Account scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'
         for Department scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         '/providers/Microsoft.Management/managementGroups/{managementGroupId}'
         for Management Group scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners.
        :type scope: str
        :param filter: May be used to filter dimensions by
         properties/category, properties/usageStart, properties/usageEnd.
         Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
        :type filter: str
        :param expand: May be used to expand the properties/data within a
         dimension category. By default, data is not included when listing
         dimensions.
        :type expand: str
        :param skiptoken: Skiptoken is only used if a previous operation
         returned a partial result. If a previous response contains a nextLink
         element, the value of the nextLink element will include a skiptoken
         parameter that specifies a starting point to use for subsequent calls.
        :type skiptoken: str
        :param top: May be used to limit the number of results to the most
         recent N dimension data.
        :type top: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Dimension
        :rtype:
         ~azure.mgmt.costmanagement.models.DimensionPaged[~azure.mgmt.costmanagement.models.Dimension]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.costmanagement.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'scope': self._serialize.url("scope", scope, 'str', skip_quote=True)
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')
                if skiptoken is not None:
                    query_parameters['$skiptoken'] = self._serialize.query("skiptoken", skiptoken, 'str')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int', maximum=1000, minimum=1)

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.DimensionPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/{scope}/providers/Microsoft.CostManagement/dimensions'}