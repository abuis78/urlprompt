"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'json_prompt_combined_prompt' block
    json_prompt_combined_prompt(container=container)

    return

@phantom.playbook_block()
def playbook_i001_url_prompt_json_create_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_i001_url_prompt_json_create_1() called")

    inputs = {
        "json_schema": [],
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "urlprompt/I001_url_prompt_json_create", returns the playbook_run_id
    playbook_run_id = phantom.playbook("urlprompt/I001_url_prompt_json_create", container=container, name="playbook_i001_url_prompt_json_create_1", callback=playbook_i001_url_prompt_json_create_1_callback, inputs=inputs)

    return


@phantom.playbook_block()
def playbook_i001_url_prompt_json_create_1_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_i001_url_prompt_json_create_1_callback() called")

    
    # Downstream End block cannot be called directly, since execution will call on_finish automatically.
    # Using placeholder callback function so child playbook is run synchronously.


    return


@phantom.playbook_block()
def json_prompt_combined_prompt(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("json_prompt_combined_prompt() called")

    template = """{\n    \"schema\": {\n        \"title\": \"Tell me something about yourself!\",\n        \"type\": \"object\",\n        \"required\": [\"height\", \"eyecolor\", \"birthyear\"],\n        \"properties\": {\n            \"height\": {\"type\": \"integer\", \"title\": \"Height in cm\"},\n            \"birthyear\": {\"type\": \"integer\", \"title\": \"Birthyear (YYYY)\"},\n            \"eyecolor\": {\n            \"type\": \"number\",\n            \"enum\": [1, 2, 3, 4, 5],\n            \"enumNames\": [\"blue\", \"grey\", \"green\", \"brown\", \"other\"]\n            }\n        }\n    }\n}"""

    # parameter list for template variable replacement
    parameters = []

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="json_prompt_combined_prompt")

    playbook_i001_url_prompt_json_create_1(container=container)

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    return