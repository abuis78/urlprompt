"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'create_json_prompt_1' block
    create_json_prompt_1(container=container)

    return

@phantom.playbook_block()
def create_json_prompt_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("create_json_prompt_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    playbook_input_json_schema = phantom.collect2(container=container, datapath=["playbook_input:json_schema"])

    parameters = []

    # build parameters list for 'create_json_prompt_1' call
    for playbook_input_json_schema_item in playbook_input_json_schema:
        if playbook_input_json_schema_item[0] is not None:
            parameters.append({
                "schema": playbook_input_json_schema_item[0],
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("create json prompt", parameters=parameters, name="create_json_prompt_1", assets=["urlprompt"], callback=schedule_playbook_1)

    return


@phantom.playbook_block()
def schedule_playbook_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("schedule_playbook_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    parameters = []

    parameters.append({
        "playbook": "Format: <repository>/<playbook>",
        "duration_unit": "Minutes",
        "delay_duration": 5,
        "playbook_scope": "all",
        "delay_purpose": "",
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("schedule playbook", parameters=parameters, name="schedule_playbook_1", assets=["runner-1"])

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