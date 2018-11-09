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


class StorageInsightStatus(Model):
    """The status of the storage insight.

    All required parameters must be populated in order to send to Azure.

    :param state: Required. The state of the storage insight connection to the
     workspace. Possible values include: 'OK', 'ERROR'
    :type state: str or ~azure.mgmt.loganalytics.models.StorageInsightState
    :param description: Description of the state of the storage insight.
    :type description: str
    """

    _validation = {
        'state': {'required': True},
    }

    _attribute_map = {
        'state': {'key': 'state', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StorageInsightStatus, self).__init__(**kwargs)
        self.state = kwargs.get('state', None)
        self.description = kwargs.get('description', None)
