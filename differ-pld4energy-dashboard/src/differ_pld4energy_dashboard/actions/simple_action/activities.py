from temporalio import activity

from differ_pld4energy_dashboard.actions.simple_action.models import SimpleWorkflowInput


@activity.defn
async def greet(data: SimpleWorkflowInput) -> str:
    return f'hello {data.name} - created by user {data.user_id} for upload {data.upload_id}'
