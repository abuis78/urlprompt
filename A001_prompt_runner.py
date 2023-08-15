"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'filter_get_prompt_artifact' block
    filter_get_prompt_artifact(container=container)

    return

@phantom.playbook_block()
def filter_get_prompt_artifact(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("filter_get_prompt_artifact() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["artifact:*.name", "==", "URL Prompt"]
        ],
        name="filter_get_prompt_artifact:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        check_the_status_of_the_prompt(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def check_the_status_of_the_prompt(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("check_the_status_of_the_prompt() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    filtered_artifact_0_data_filter_get_prompt_artifact = phantom.collect2(container=container, datapath=["filtered-data:filter_get_prompt_artifact:condition_1:artifact:*.cef.prompt_id","filtered-data:filter_get_prompt_artifact:condition_1:artifact:*.id"])

    parameters = []

    # build parameters list for 'check_the_status_of_the_prompt' call
    for filtered_artifact_0_item_filter_get_prompt_artifact in filtered_artifact_0_data_filter_get_prompt_artifact:
        if filtered_artifact_0_item_filter_get_prompt_artifact[0] is not None:
            parameters.append({
                "id": filtered_artifact_0_item_filter_get_prompt_artifact[0],
                "context": {'artifact_id': filtered_artifact_0_item_filter_get_prompt_artifact[1]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("check status", parameters=parameters, name="check_the_status_of_the_prompt", assets=["urlprompt"], callback=decission_check_status)

    return


@phantom.playbook_block()
def decission_check_status(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decission_check_status() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["check_the_status_of_the_prompt:action_result.data.*.status", "==", "pending"]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        filter_runner_artifact(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'elif' condition 2
    found_match_2 = phantom.decision(
        container=container,
        conditions=[
            ["check_the_status_of_the_prompt:action_result.data.*.status", "==", "complete"]
        ],
        delimiter=None)

    # call connected blocks if condition 2 matched
    if found_match_2:
        build_json_from_the_response(action=action, success=success, container=container, results=results, handle=handle)
        return

    return


@phantom.playbook_block()
def filter_runner_artifact(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("filter_runner_artifact() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["artifact:*.name", "==", "scheduled playbook"]
        ],
        name="filter_runner_artifact:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        ste_runner_artifact_to_label_pending(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def ste_runner_artifact_to_label_pending(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("ste_runner_artifact_to_label_pending() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    filtered_artifact_0_data_filter_runner_artifact = phantom.collect2(container=container, datapath=["filtered-data:filter_runner_artifact:condition_1:artifact:*.id","filtered-data:filter_runner_artifact:condition_1:artifact:*.id"])

    parameters = []

    # build parameters list for 'ste_runner_artifact_to_label_pending' call
    for filtered_artifact_0_item_filter_runner_artifact in filtered_artifact_0_data_filter_runner_artifact:
        if filtered_artifact_0_item_filter_runner_artifact[0] is not None:
            parameters.append({
                "artifact_id": filtered_artifact_0_item_filter_runner_artifact[0],
                "label": "pending",
                "context": {'artifact_id': filtered_artifact_0_item_filter_runner_artifact[1]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("update artifact", parameters=parameters, name="ste_runner_artifact_to_label_pending", assets=["phantom"])

    return


@phantom.playbook_block()
def build_json_from_the_response(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("build_json_from_the_response() called")

    check_the_status_of_the_prompt_result_data = phantom.collect2(container=container, datapath=["check_the_status_of_the_prompt:action_result.data"], action_results=results)

    check_the_status_of_the_prompt_result_item_0 = [item[0] for item in check_the_status_of_the_prompt_result_data]

    build_json_from_the_response__response_json = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    
    
    response = check_the_status_of_the_prompt_result_item_0[0]
    response_data = response[0]["response"]
    stringified_data = {key: str(value) for key, value in response_data.items()}
    
    
    
    build_json_from_the_response__response_json = { "cef": stringified_data }
    
    
    phantom.debug(build_json_from_the_response__response_json)

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="build_json_from_the_response:response_json", value=json.dumps(build_json_from_the_response__response_json))

    artifact_create_2(container=container)

    return


@phantom.playbook_block()
def artifact_create_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("artifact_create_2() called")

    id_value = container.get("id", None)
    build_json_from_the_response__response_json = json.loads(_ if (_ := phantom.get_run_data(key="build_json_from_the_response:response_json")) != "" else "null")  # pylint: disable=used-before-assignment

    parameters = []

    parameters.append({
        "container": id_value,
        "name": "Prompt answer",
        "label": None,
        "severity": None,
        "cef_field": None,
        "cef_value": None,
        "cef_data_type": None,
        "tags": None,
        "run_automation": False,
        "input_json": build_json_from_the_response__response_json,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/artifact_create", parameters=parameters, name="artifact_create_2")

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