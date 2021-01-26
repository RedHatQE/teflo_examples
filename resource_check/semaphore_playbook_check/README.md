# User Guide

## Installation

To utilize this example you must install teflo.
```bash
pip intall teflo
```


## Usage
Copy this directory to the workspace where Teflo is installed. This example is meant to show how to use Teflo's 
resource check can be used to check the status of systems/services that are monitored by Semaphore as well as 
system/services not monitored by Semaphore. You will need to update the teflo.cfg with the api url of the system
which maintains the services and system status

```bash
resource_check_endpoint=http:/abc.com/api/v1
```

Below is the contents of this resource check example directory
```bash
├── ansible.cfg
├── teflo.cfg
├── cbn_vars.yml
├── custom_res_checks
│   ├── ans_vars.yml
│   └── non_semaphore_check.yml
├── notification_templates
│   └── resource_check_failure.tmpl
├── README.md
└── validate.yml
```

The key file is the [validate.yml](validate.yml) which is a Teflo scenario descriptor file (later on 
it might be referred to as SDF). This defines two sections, **resource_check** and **notifications**. 

### Resource Check 
The **resource_check** section defines what Teflo should check for.  
 
 * The *monitored_services* key takes a list services/systems being monitored by a status page like semaphore
   User will have to edit the teflo.cfg to add the url for the monitoring tool (Teflo supports statuspage.io and semaphore)
 
 * The *playbook* key takes a path to a playbook, [non_semaphore_check.yml](custom_res_checks/non_semaphore_check.yml), 
   that defines a simple uri check for services/systems NOT being monitored by semaphore
   
### Notification
The **notification** section describes what and who Teflo should notify a particular trigger or state. This
is optional. This was included as a nice way to alert you of in case any of the validation failed. It uses
a [notification template](notification_templates/resource_check_failure.tmpl) which extracts the services 
being checked in the scenario descriptor file and injects them into the template. 

## Running Example
You may have noticed in the SDF the use of Jinja2 templating logic. This is intentional. The idea 
being that you shouldn't have to configure or change much in the SDF unless there is a specific parameter
you want to add or more Jinja2 logic. Everything should be driven from two variable files

* [ans_vars.yml](custom_res_checks/ans_vars.yml) which defines a list of service/system urls that the
  playbook should loop and validate connectivity to as part of resource check. 
  
* [cbn_vars.yml](cbn_vars.yml) which defines a list inputs that drive the execution
  of the SDF. Below is a table with the variables
  
 <table class="tg">
   <tr>
     <th class="tg-7un6">Key</th>
     <th class="tg-14gg">Description</th>
     <th class="tg-14gg">Type</th>
     <th class="tg-14gg">Required</th>
   </tr>
   <tr>
     <td class="tg-8m83">semaphore_services</td>
     <td class="tg-8m83">comma separated list of service monitored in semaphore</td>
     <td class="tg-8m83">String</td>
     <td class="tg-8m83">True</td>
   </tr>
   <tr>
     <td class="tg-14gg">enable_notification</td>
     <td class="tg-14gg">Whether the email notification should be enabled or not.</td>
     <td class="tg-14gg">String</td>
     <td class="tg-14gg">False</td>
   </tr>
   <tr>
     <td class="tg-8m83">to_address</td>
     <td class="tg-8m83"> a comma separated list of destination email addresses to send a notification. </td>
     <td class="tg-8m83">String</td>
     <td class="tg-8m83">False</td>
   </tr>
   <tr>
     <td class="tg-14gg">from_address</td>
     <td class="tg-14gg">an email address noting who the notification is from.</td>
     <td class="tg-14gg">String</td>
     <td class="tg-14gg">False</td>
   </tr>
   </table>

Once you've updated the variable files appropriately you can execute the resource check using the following 
command:

```bash
teflo validate -s validate.yml --vars-data cbn_vars.yml
```

If you need more logging output you can run the following:

```bash
teflo validate -s validate.yml --vars-data cbn_vars.yml --log-level debug
```



 

