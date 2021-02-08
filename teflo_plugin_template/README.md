# Cookiecutter Template for Teflo Plugins

This is a template that user can use to get an empty directory 
structure that can be used to develop a teflo plugin
This helps in reducing copy pasting from other plugin directories

## How to use
To use this template to create your plugin folder:
1. install cookiecutter 
```bash
pip install cookiecutter
```
2. Clone the teflo_examples repo
``` bash
git clone git@github.com:RedHatQE/teflo_examples.git
```
3. Go to the space where you want your plugin folder to be created
   then run the command
``` bash
cookiecutter <path to the cloned teflo_examples repo>/teflo_plugin_template 
```
4. When you run this you will be prompted to provide values for the variables in the
   cookiecutter json file, Below are the variables and their description.
   User should provide the values it needs, else the default values will be taken

<table class="tg">
  <tr>
    <th class="tg-7un6">Variable</th>
    <th class="tg-14gg">Description</th>
    <th class="tg-14gg">Default Value</th>
  </tr>
  <tr>
    <td class="tg-8m83">teflo_plugin_type</td>
    <td class="tg-8m83">type of teflo plugin to be created (provisioner or orchestrator or executor or importer or notification)</td>
    <td class="tg-8m83">provisioner</td>
  </tr>
  <tr>
    <td class="tg-8m83">directory_name</td>
    <td class="tg-8m83">name to be give to the plugin repo directory</td>
    <td class="tg-8m83">teflo_provisionerX_plugin</td>
  </tr>
  <tr>
    <td class="tg-8m83">plugin_name</td>
    <td class="tg-8m83">name of the python file where your actual plugin code will reside</td>
    <td class="tg-8m83">provx_plugin</td>
  </tr>
  <tr>
    <td class="tg-8m83">plugin_class_name</td>
    <td class="tg-8m83">the name of the class within the python file</td>
    <td class="tg-8m83">ProvXProvisionerPlugin</td>
  </tr>
  <tr>
    <td class="tg-8m83">test_class_name</td>
    <td class="tg-8m83">name to be given to the unit test file under tests folder. This is auto generated if left blank</td>
    <td class="tg-8m83">test_provx_plugin</td>
  </tr>
  <tr>
    <td class="tg-8m83">plugin_description</td>
    <td class="tg-8m83">Plugins description that goes into the setup.py</td>
    <td class="tg-8m83">teflo provisioner plugin</td>
  </tr>
  <tr>
    <td class="tg-8m83">jenkins_ci_job_link</td>
    <td class="tg-8m83">jenkins ci job link once you have created that. This gets updated in the jenkins/Jenkinsfile</td>
    <td class="tg-8m83">your ci job link</td>
  </tr>
  <tr>
    <td class="tg-8m83">plugin_url</td>
    <td class="tg-8m83">plugin url needed to start the ci job. This gets updated in the jenkins/Jenkinsfile</td>
    <td class="tg-8m83">plugin url on gitlab/github</td>
  </tr>
  <tr>
    <td class="tg-8m83">authors</td>
    <td class="tg-8m83">The value that gets updated in the AUTHORS file</td>
    <td class="tg-8m83">CCIT tools dev team <ci-ops-qe@redhat.com></td>
  </tr>
</table>

**Note**

Here the variables **jenkins_ci_job_link** and **plugin_url** can be left default, and then these values can be updated
in the jenkins/Jenkinsfile once user has the CI job url and repo url ready.
These variables are meant to be more as a place holder for users to know where they can update 
later

**Note**
Read [here](https://cookiecutter.readthedocs.io/en/1.7.2/index.html) about cookiecutter package

###  Example
``` bash
$ cookiecutter <path to the teflo_examples dir>/teflo_plugin_template/
teflo_plugin_type [provisioner]: importer
directory_name [teflo_provisionerX_plugin]: teflo_datarouter_plugin
plugin_name [provx_plugin]: datarouter_plugin
plugin_class_name [ProvXProvisionerPlugin]: DataRouterImporterPlugin
test_class_name [test_datarouter_plugin]: 
plugin_description [teflo provisioner plugin]: teflo plugin for data router
jenkins_ci_job_link [<your ci job link>]: 
plugin_url [<plugin url on gitlab/github>]: 
authors [CCIT tools dev team <ci-ops-qe@redhat.com>]:
```
The above command will create a folder named teflo_datarouter_plugin
with all the necessary base files there.
User can then edit them as needed and upload the plugin on github/gitlab

Following is the plugin directory structure that will be created 
``` bash
$ cd teflo_datarouter_plugin/
$ ls
AUTHORS  CHANGES.md  docs  jenkins  LICENSE  Makefile  MANIFEST.in  README.md  setup.cfg  setup.py  teflo_datarouter_plugin  test-requirements.txt  tests  tox.ini
$ tree
.
├── AUTHORS
├── CHANGES.md
├── docs
│   ├── contribute.md
│   └── user.md
├── jenkins
│   └── Jenkinsfile
├── LICENSE
├── Makefile
├── MANIFEST.in
├── README.md
├── setup.cfg
├── setup.py
├── teflo_datarouter_plugin
│   ├── datarouter_plugin.py
│   ├── files
│   │   ├── schema_extensions.py
│   │   └── schema.yml
│   └── __init__.py
├── test-requirements.txt
├── tests
│   ├── functional
│   │   └── test_datarouter_plugin.py
│   └── pytest.ini
└── tox.ini
```

