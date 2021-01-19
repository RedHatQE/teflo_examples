# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Red Hat, Inc.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""

    Actual code for the plugin should go here. What the plugin does etc.

    :copyright: (c) 2020 Red Hat, Inc.
    :license: GPLv3, see LICENSE for more details.
"""
{% set var1 = 
'__plugin_name__ = \'newplugin_name\'

__schema_file_path__ = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                        "files/schema.yml"))
__schema_ext_path__ = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                       "files/schema_extensions.py"))' %}
{% set var2 = 
'# creating logger for this plugin to get added to teflo loggers. create_logger is teflo method
        # self.create_logger(name=\'newplugin_name\', data_folder=<data folder name>)
        # OR use teflo logger
        # logger = logging.getLogger(\'teflo\')' %}

from teflo.helpers import schema_validator
{% if cookiecutter.teflo_plugin_type == 'provisioner' %}
from teflo.core import ProvisionerPlugin
from teflo.exceptions import TefloProvisionerError

class {{cookiecutter.plugin_class_name}}(ProvisionerPlugin):
# Give your plugin name property here. This will be the name that will be used in the scenario descriptor file
{{ var1 }}

    def __init__(self, asset):
        # your plugin init method which takes in teflo asset resource object as input

        {{ var2 }}

        pass

    def create(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    def authenticate(self):
        raise NotImplementedError

    def validate(self):
        raise NotImplementedError

{% elif cookiecutter.teflo_plugin_type == 'orchestrator' %}                                   
from teflo.core import OrchestratorPlugin
from teflo.exceptions import TefloOrchestratorError

class {{cookiecutter.plugin_class_name}}(OrchestratorPlugin):
# Give your plugin name property here. This will be the name that will be used in the scenario descriptor file
{{ var1 }}

    def __init__(self, action):
        # your plugin init method which takes in teflo action resource object as input
   
        {{ var2 }}        
  
        pass

    def validate(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

{% elif cookiecutter.teflo_plugin_type == 'executor' %}
from teflo.core import ExecutorPlugin
from teflo.exceptions import TefloExecuteError
class {{cookiecutter.plugin_class_name}}(ExecutorPlugin):
# Give your plugin name property here. This will be the name that will be used in the scenario descriptor file
{{ var1 }}

    def __init__(self, execute):
        # your plugin init method which takes in teflo execute resource object as input
      
        {{ var2 }}

        pass

    def validate(self):
        raise NotImplementedError    

    def run(self):
        raise NotImplementedError

{% elif cookiecutter.teflo_plugin_type == 'importer' %}
from teflo.core import ImporterPlugin
from teflo.exceptions import TefloImporterError
class {{cookiecutter.plugin_class_name}}(ImporterPlugin):
# Give your plugin name property here. This will be the name that will be used in the scenario descriptor file
{{ var1 }}

    def __init__(self, report):
        # your plugin init method which takes in teflo report resource object as input
  
        {{ var2 }}

        pass

    def aggregate_artifacts(self):
        raise NotImplementedError

    def import_artifacts(self):
        raise NotImplementedError

    def cleanup_artifacts(self):
        raise NotImplementedError

{% elif cookiecutter.teflo_plugin_type == 'notification' %}
from teflo.core import NorificationPlugin
from teflo.exceptions import TefloNotifierError
class {{cookiecutter.plugin_class_name}}(NotificationPlugin):
# Give your plugin name property here. This will be the name that will be used in the scenario descriptor file
{{ var1 }}
    def __init__(self, notification):
        # your plugin init method which takes in teflo notification resource object as input
        
        {{ var2 }}

        pass

    def notify(self):
        raise NotImplementedError

    def validate(self):
        raise NotImplementedError

{% else %}
# Did not match any plugin type. delete this folder and rerun
{% endif %}
