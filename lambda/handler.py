import json
import urllib.request

PROTOCOL_VERSION = "2024-11-05"

# Documentation paths (relative to Lambda working directory /var/task/)
DOCS = {
    "framework/overview": "docs/framework/overview.md",
    "framework/perspective": "docs/framework/perspective.md",
    "templates/commit-format": "docs/templates/commit-format.md",
    "templates/collaborators-template": "docs/templates/collaborators-template.md",
    "quick-reference": "docs/quick-reference.md",
}

FIELD_DOCS = {
    "intent": "docs/fields/intent.md",
    "nature": "docs/fields/nature.md",
    "name": "docs/fields/name.md",
    "role": "docs/fields/role.md",
    "freeform": "docs/fields/freeform.md",
}

TOOLS = {
    "get_framework_overview": "framework/overview",
    "get_framework_perspective": "framework/perspective",
    "get_commit_format_guide": "templates/commit-format",
    "get_collaborators_template": "templates/collaborators-template",
    "get_quick_reference": "quick-reference",
    "list_fields": None,
    "get_field_guide": None,
    "list_faqs": None,
    "get_faq": None,
}

FIELDS = list(FIELD_DOCS.keys())

FAQ_TEMPLATES = {
    "why_framework": {
        "question": "Why use the Collaborators Framework?",
        "system": "Answer using the Collaborators Framework documentation, emphasizing Impact Above Origin and non-permissioned participation.",
    },
    "commit_format": {
        "question": "How does the Collaborators commit format work?",
        "system": "Answer using the commit format documentation with concrete examples.",
    },
    "getting_started": {
        "question": "How do I get started with the Collaborators Framework?",
        "system": "Answer using the framework documentation, focusing on COLLABORATORS.md creation and commit tagging.",
    },
    "author_vs_collaborator": {
        "question": "What's the difference between git author and Collaborator tag?",
        "system": "Answer: git author is who creates the commit, Collaborator tags are all who contributed to the impact.",
    },
    "ai_participation": {
        "question": "How should AI collaborators participate in the framework?",
        "system": "Answer using the tool-first guidance: participation is optional, non-permissioned, and self-determined.",
    },
    "intent_field_choice": {
        "question": "How do I choose between Direct, Indirect, and Supportive intent?",
        "system": "Answer using the intent field documentation with examples of each type.",
    },
    "optional_fields": {
        "question": "Which fields are required and which are optional?",
        "system": "Answer: First four fields are required (Name, Intent, Nature, Role). Freeform fifth field is optional.",
    },
}

FAQ_TEMPLATE_KEYS = list(FAQ_TEMPLATES.keys())


def _faq_questions_text():
    lines = ["Available FAQs:"]
    for name in FAQ_TEMPLATE_KEYS:
        question = FAQ_TEMPLATES[name]["question"]
        lines.append(f"- {name}: {question}")
    lines.extend(["", "Template: collaborators://faq/{name}"])
    return "\n".join(lines)


def _jsonrpc_error(req_id, code, message):
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {
            "code": code,
            "message": message,
        },
    }


def _jsonrpc_result(req_id, result):
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "result": result,
    }


def _handle_request(payload):
    if not isinstance(payload, dict):
        return _jsonrpc_error(None, -32600, "Invalid Request")

    if payload.get("jsonrpc") != "2.0" or "method" not in payload:
        return _jsonrpc_error(payload.get("id"), -32600, "Invalid Request")

    method = payload.get("method")
    req_id = payload.get("id")
    params = payload.get("params") or {}

    if method == "initialize":
        result = {
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {
                "tools": {},
                "resources": {
                    "templates": True,
                },
            },
            "serverInfo": {
                "name": "collaborators-framework-mcp",
                "version": "0.3.0",
            },
        }
        return _jsonrpc_result(req_id, result)

    if method == "notifications/initialized":
        return None

    if method == "ping":
        return _jsonrpc_result(req_id, {})

    if method == "tools/list":
        result = {
            "tools": [
                {
                    "name": "get_framework_overview",
                    "description": "Return the main Collaborators Framework documentation (Impact Above Origin principle, field definitions, examples).",
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                    },
                },
                {
                    "name": "get_framework_perspective",
                    "description": "Return the philosophical foundation of the framework (non-permissioned participation, intentional engagement).",
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                    },
                },
                {
                    "name": "get_commit_format_guide",
                    "description": "Return the complete commit message tagging guide with examples.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                    },
                },
                {
                    "name": "get_collaborators_template",
                    "description": "Return the COLLABORATORS.md template.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                    },
                },
                {
                    "name": "get_quick_reference",
                    "description": "Return a condensed quick reference guide for framework fields and format.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                    },
                },
                {
                    "name": "list_fields",
                    "description": "List all Collaborators Framework fields with brief descriptions.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                    },
                },
                {
                    "name": "get_field_guide",
                    "description": "Get detailed documentation for a specific field.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "field_name": {
                                "type": "string",
                                "description": "The field name (use list_fields to discover available fields)",
                                "enum": ["intent", "nature", "name", "role", "freeform"],
                            }
                        },
                        "required": ["field_name"],
                    },
                },
                {
                    "name": "list_faqs",
                    "description": "List all available FAQ templates with questions.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                    },
                },
                {
                    "name": "get_faq",
                    "description": "Get a specific FAQ template for AI/human clarification.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "faq_name": {
                                "type": "string",
                                "description": "The FAQ identifier (use list_faqs to discover available FAQs)",
                                "enum": list(FAQ_TEMPLATES.keys()),
                            }
                        },
                        "required": ["faq_name"],
                    },
                },
            ]
        }
        return _jsonrpc_result(req_id, result)

    if method == "tools/call":
        tool_name = params.get("name")
        tool_args = params.get("arguments") or {}

        # Special handlers for parameterized tools
        if tool_name == "list_fields":
            fields_text = """Collaborators Framework Fields:

Required Fields:
- name: Identifying name or alias
- intent: How contribution reached the work (Direct, Indirect, Supportive)
- nature: Type of collaborator (Human, AI, Organization, etc.)
- role: Summary of contribution

Optional Fields:
- freeform: Personal note or context

Detailed Documentation:
- get_field_guide tool with field_name parameter
- Resource template: collaborators://field/{field_name}

Example: get_field_guide(field_name="intent")"""
            result = {
                "content": [
                    {
                        "type": "text",
                        "text": fields_text,
                    }
                ]
            }
            return _jsonrpc_result(req_id, result)

        if tool_name == "get_field_guide":
            field_name = tool_args.get("field_name")
            if not field_name or field_name not in FIELD_DOCS:
                return _jsonrpc_error(req_id, -32602, "Invalid or missing field_name parameter")

            doc_path = FIELD_DOCS[field_name]
            try:
                with open(doc_path, "r", encoding="utf-8") as handle:
                    content = handle.read()
            except OSError:
                return _jsonrpc_error(req_id, -32000, "Document not available")

            result = {"content": [{"type": "text", "text": content}]}
            return _jsonrpc_result(req_id, result)

        if tool_name == "list_faqs":
            faq_list = []
            for name, faq in FAQ_TEMPLATES.items():
                faq_list.append(f"- {name}: {faq['question']}")

            faq_text = f"""Available FAQ Templates:

{chr(10).join(faq_list)}

Access Pattern:
- Use get_faq tool with faq_name parameter
- Use resource template: collaborators://faq/{{faq_name}}

Example: get_faq(faq_name="why_framework")

Note: FAQs function as clarification templates, not prescriptive answers.
They provide system prompts for context-appropriate responses."""
            result = {
                "content": [
                    {
                        "type": "text",
                        "text": faq_text,
                    }
                ]
            }
            return _jsonrpc_result(req_id, result)

        if tool_name == "get_faq":
            faq_name = tool_args.get("faq_name")
            if not faq_name or faq_name not in FAQ_TEMPLATES:
                return _jsonrpc_error(req_id, -32602, "Invalid or missing faq_name parameter")

            faq = FAQ_TEMPLATES[faq_name]
            faq_text = f"""FAQ: {faq['question']}

System Prompt: {faq['system']}

Usage Template:
- System: {faq['system']}
- User: {faq['question']}

This FAQ functions as a clarification template. Use it to generate context-appropriate answers."""
            result = {"content": [{"type": "text", "text": faq_text}]}
            return _jsonrpc_result(req_id, result)

        # Standard document tools
        doc_key = TOOLS.get(tool_name)
        if not doc_key:
            return _jsonrpc_error(req_id, -32602, "Unknown tool")

        doc_path = DOCS.get(doc_key)
        if not doc_path:
            return _jsonrpc_error(req_id, -32602, "Unknown resource")

        try:
            with open(doc_path, "r", encoding="utf-8") as handle:
                content = handle.read()
        except OSError:
            return _jsonrpc_error(req_id, -32000, "Document not available")

        result = {
            "content": [
                {
                    "type": "text",
                    "text": content,
                }
            ]
        }
        return _jsonrpc_result(req_id, result)

    if method == "resources/list":
        result = {
            "resources": [
                {
                    "uri": "collaborators://framework/overview",
                    "name": "Framework Overview",
                    "description": "Main framework documentation with examples.",
                    "mimeType": "text/markdown",
                },
                {
                    "uri": "collaborators://framework/perspective",
                    "name": "Framework Perspective",
                    "description": "Philosophical foundation and participation model.",
                    "mimeType": "text/markdown",
                },
                {
                    "uri": "collaborators://templates/commit-format",
                    "name": "Commit Format Guide",
                    "description": "Complete guide for commit message collaboration tagging.",
                    "mimeType": "text/markdown",
                },
                {
                    "uri": "collaborators://templates/collaborators-template",
                    "name": "COLLABORATORS.md Template",
                    "description": "Template for repository adoption.",
                    "mimeType": "text/markdown",
                },
                {
                    "uri": "collaborators://quick-reference",
                    "name": "Quick Reference",
                    "description": "Condensed field reference and format guide.",
                    "mimeType": "text/markdown",
                },
                {
                    "uri": "collaborators://fields",
                    "name": "Fields List",
                    "description": "List all available framework fields.",
                    "mimeType": "text/plain",
                },
                {
                    "uri": "collaborators://faqs",
                    "name": "FAQs List",
                    "description": "List available FAQ templates.",
                    "mimeType": "text/plain",
                },
            ]
        }
        return _jsonrpc_result(req_id, result)

    if method == "resources/templates/list":
        result = {
            "resourceTemplates": [
                {
                    "uriTemplate": "collaborators://field/{field_name}",
                    "name": "Field Documentation",
                    "description": "Detailed documentation for a specific framework field.",
                    "mimeType": "text/markdown",
                },
                {
                    "uriTemplate": "collaborators://faq/{faq_name}",
                    "name": "FAQ Template",
                    "description": "FAQ clarification template for context-dependent questions.",
                    "mimeType": "text/plain",
                },
            ]
        }
        return _jsonrpc_result(req_id, result)

    if method == "resources/read":
        uri = params.get("uri", "")
        if not uri.startswith("collaborators://"):
            return _jsonrpc_error(req_id, -32602, "Unknown resource")
        key = uri.split("collaborators://", 1)[1]

        # Handle field template resources
        if key.startswith("field/"):
            field_name = key.split("field/", 1)[1]
            doc_path = FIELD_DOCS.get(field_name)
            if not doc_path:
                return _jsonrpc_error(req_id, -32602, "Unknown resource")
            try:
                with open(doc_path, "r", encoding="utf-8") as handle:
                    content = handle.read()
            except OSError:
                return _jsonrpc_error(req_id, -32000, "Document not available")
            result = {
                "contents": [
                    {
                        "uri": uri,
                        "mimeType": "text/markdown",
                        "text": content,
                    }
                ]
            }
            return _jsonrpc_result(req_id, result)

        # Handle FAQ template resources
        if key.startswith("faq/"):
            faq_name = key.split("faq/", 1)[1]
            faq = FAQ_TEMPLATES.get(faq_name)
            if not faq:
                return _jsonrpc_error(req_id, -32602, "Unknown resource")
            faq_text = f"""FAQ: {faq['question']}

System Prompt: {faq['system']}

Usage Template:
- System: {faq['system']}
- User: {faq['question']}

This FAQ functions as a clarification template. Use it to generate context-appropriate answers."""
            result = {
                "contents": [
                    {
                        "uri": uri,
                        "mimeType": "text/plain",
                        "text": faq_text,
                    }
                ]
            }
            return _jsonrpc_result(req_id, result)

        # Handle fields list resource
        if key == "fields":
            fields_text = """Available Collaborators Framework Fields:

Required Fields:
- name: Identifying name or alias
- intent: Directness of contribution (Direct, Indirect, Supportive)
- nature: Type of collaborator (Human, AI, Organization, etc.)
- role: Concise summary of contribution

Optional Fields:
- freeform: Personal note or context

Access Pattern:
- Use get_field_guide tool with field_name parameter for detailed documentation
- Use resource template: collaborators://field/{field_name}"""
            result = {
                "contents": [
                    {
                        "uri": uri,
                        "mimeType": "text/plain",
                        "text": fields_text,
                    }
                ]
            }
            return _jsonrpc_result(req_id, result)

        # Handle FAQs list resource
        if key == "faqs":
            faq_list = []
            for name, faq in FAQ_TEMPLATES.items():
                faq_list.append(f"- {name}: {faq['question']}")

            faq_text = f"""Available FAQ Templates:

{chr(10).join(faq_list)}

Access Pattern:
- Use get_faq tool with faq_name parameter
- Use resource template: collaborators://faq/{{faq_name}}"""
            result = {
                "contents": [
                    {
                        "uri": uri,
                        "mimeType": "text/plain",
                        "text": faq_text,
                    }
                ]
            }
            return _jsonrpc_result(req_id, result)

        # Handle all other document resources
        doc_path = DOCS.get(key)
        if not doc_path:
            return _jsonrpc_error(req_id, -32602, "Unknown resource")

        try:
            with open(doc_path, "r", encoding="utf-8") as handle:
                content = handle.read()
        except OSError:
            return _jsonrpc_error(req_id, -32000, "Document not available")

        result = {
            "contents": [
                {
                    "uri": uri,
                    "mimeType": "text/markdown",
                    "text": content,
                }
            ]
        }
        return _jsonrpc_result(req_id, result)

    return _jsonrpc_error(req_id, -32601, "Method not found")


def handler(event, _context):
    body = event.get("body") or ""
    try:
        payload = json.loads(body)
    except json.JSONDecodeError:
        error = _jsonrpc_error(None, -32700, "Parse error")
        return {
            "statusCode": 400,
            "headers": {
                "content-type": "application/json",
                "access-control-allow-origin": "*",
            },
            "body": json.dumps(error),
        }

    if isinstance(payload, list):
        responses = []
        for item in payload:
            response = _handle_request(item)
            if response is not None:
                responses.append(response)
        if not responses:
            return {
                "statusCode": 204,
                "headers": {
                    "access-control-allow-origin": "*",
                },
                "body": "",
            }
        return {
            "statusCode": 200,
            "headers": {
                "content-type": "application/json",
                "access-control-allow-origin": "*",
            },
            "body": json.dumps(responses),
        }

    response = _handle_request(payload)
    if response is None:
        return {
            "statusCode": 204,
            "headers": {
                "access-control-allow-origin": "*",
            },
            "body": "",
        }

    return {
        "statusCode": 200,
        "headers": {
            "content-type": "application/json",
            "access-control-allow-origin": "*",
        },
        "body": json.dumps(response),
    }
