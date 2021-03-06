#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from oslo_policy import policy

from neutron.conf.policies import base


rules = [
    policy.RuleDefault(
        'get_auto_allocated_topology',
        base.RULE_ADMIN_OR_OWNER,
        description=("Access rule for getting a project's "
                     "auto-allocated topology")),
    policy.RuleDefault(
        'delete_auto_allocated_topology',
        base.RULE_ADMIN_OR_OWNER,
        description=("Access rule for deleting a project's "
                     "auto-allocated topology")),
]


def list_rules():
    return rules
