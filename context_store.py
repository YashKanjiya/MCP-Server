session_context = {}

def get_context(session_id: str):
    return session_context.get(session_id, [])

def update_context(session_id: str, context):
    session_context[session_id] = context
