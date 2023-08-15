"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'create_a_json_prompt' block
    create_a_json_prompt(container=container)

    return

@phantom.playbook_block()
def create_a_json_prompt(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("create_a_json_prompt() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    playbook_input_json_schema = phantom.collect2(container=container, datapath=["playbook_input:json_schema"])

    parameters = []

    # build parameters list for 'create_a_json_prompt' call
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

    phantom.act("create json prompt", parameters=parameters, name="create_a_json_prompt", assets=["urlprompt"], callback=json_for_artifact_create)

    return


@phantom.playbook_block()
def schedule_runner_to_check_if_user_replays(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("schedule_runner_to_check_if_user_replays() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    parameters = []

    parameters.append({
        "playbook": "urlprompt/A001_prompt_runner",
        "duration_unit": "Minutes",
        "delay_duration": 2,
        "playbook_scope": "all",
        "delay_purpose": "prompt: check if the user has already replied",
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("schedule playbook", parameters=parameters, name="schedule_runner_to_check_if_user_replays", assets=["runner-1"])

    return


@phantom.playbook_block()
def add_prompt_artifact(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_prompt_artifact() called")

    id_value = container.get("id", None)
    json_for_artifact_create = phantom.get_format_data(name="json_for_artifact_create")

    parameters = []

    parameters.append({
        "container": id_value,
        "name": "URL Prompt",
        "label": "prompt",
        "severity": None,
        "cef_field": None,
        "cef_value": None,
        "cef_data_type": None,
        "tags": "waiting_for_replay",
        "run_automation": False,
        "input_json": json_for_artifact_create,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/artifact_create", parameters=parameters, name="add_prompt_artifact", callback=format_email_boday)

    return


@phantom.playbook_block()
def json_for_artifact_create(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("json_for_artifact_create() called")

    template = """{{ \"cef\": {{ \"prompt_id\": \"{0}\", \"web_url\": \"{1}\"\n}}\n}}\n"""

    # parameter list for template variable replacement
    parameters = [
        "create_a_json_prompt:action_result.data.*.id",
        "create_a_json_prompt:action_result.data.*.web_url"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="json_for_artifact_create")

    add_prompt_artifact(container=container)

    return


@phantom.playbook_block()
def format_email_boday(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_email_boday() called")

    template = """Guess what? We've got a special question just for YOU! Dive into this mystery by clicking on the magic link below:\n\n>> {0} <<\n\nYour adventure awaits. Can't wait to see your answer!\n\nWarm regards and much anticipation,\n\n\n"""

    # parameter list for template variable replacement
    parameters = [
        "create_a_json_prompt:action_result.data.*.web_url"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_email_boday")

    send_email_to_user(container=container)

    return


@phantom.playbook_block()
def send_email_to_user(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("send_email_to_user() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    format_email_boday = phantom.get_format_data(name="format_email_boday")

    parameters = []

    if format_email_boday is not None:
        parameters.append({
            "from": "soc@soarrookies.com",
            "to": "abuis@splunk.com",
            "subject": "[Urgent request] The SOC needs a feedback from you. ",
            "body": format_email_boday,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("send email", parameters=parameters, name="send_email_to_user", assets=["smtp"], callback=schedule_runner_to_check_if_user_replays)

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