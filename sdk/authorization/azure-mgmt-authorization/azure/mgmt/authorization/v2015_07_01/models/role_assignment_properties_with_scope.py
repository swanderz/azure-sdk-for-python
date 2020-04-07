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


class RoleAssignmentPropertiesWithScope(Model):
    """Role assignment properties with scope.

    :param scope: The role assignment scope.
    :type scope: str
    :param role_definition_id: The role definition ID.
    :type role_definition_id: str
    :param principal_id: The principal ID.
    :type principal_id: str
    """

    _attribute_map = {
        'scope': {'key': 'scope', 'type': 'str'},
        'role_definition_id': {'key': 'roleDefinitionId', 'type': 'str'},
        'principal_id': {'key': 'principalId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RoleAssignmentPropertiesWithScope, self).__init__(**kwargs)
        self.scope = kwargs.get('scope', None)
        self.role_definition_id = kwargs.get('role_definition_id', None)
        self.principal_id = kwargs.get('principal_id', None)