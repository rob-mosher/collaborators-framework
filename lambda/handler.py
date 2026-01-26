import json
import urllib.request

PROTOCOL_VERSION = "2024-11-05"
FRAMEWORK_URL = "https://raw.githubusercontent.com/rob-mosher/collaborators-framework/main/README.md"
COMMIT_FORMAT_URL = (
    "https://raw.githubusercontent.com/rob-mosher/collaborators-framework/main/"
    "docs/templates/collaborator-tagging-for-commits.md"
)

DOCS = {
    "quick-reference": "docs/quick_reference.txt",
}

FIELD_DOCS = {
    "intent": "docs/fields/intent.txt",
    "nature": "docs/fields/nature.txt",
}

TOOLS = {
    "get_framework": "framework",
    "get_commit_format": "commit-format",
    "get_quick_reference": "quick-reference",
    "list_fields": None,
    "get_faqs": None,
}

FIELDS = list(FIELD_DOCS.keys())

FAQ_TEMPLATES = {
    "faq_why_framework": {
        "question": "Why use the Collaborators Framework?",
        "system": "Answer using the Collaborators Framework documentation.",
    },
    "faq_commit_format": {
        "question": "How does the Collaborators commit format work?",
        "system": "Answer using the commit format documentation.",
    },
    "faq_getting_started": {
        "question": "How do I get started with the Collaborators Framework?",
        "system": "Answer using the Collaborators Framework documentation.",
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
                "name": "mcp-hello-world",
                "version": "0.1.0",
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
                    "name": "get_framework",
                    "description": "Return the Collaborators Framework documentation.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                    },
                },
                {
                    "name": "get_commit_format",
                    "description": "Return the commit format guidelines.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                    },
                },
                {
                    "name": "get_quick_reference",
                    "description": "Return the quick reference guide.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                    },
                },
                {
                    "name": "list_fields",
                    "description": "List available Collaborators Framework fields.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                    },
                },
                {
                    "name": "get_faqs",
                    "description": "Return the list of available FAQs.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                    },
                },
            ]
        }
        return _jsonrpc_result(req_id, result)

    if method == "tools/call":
        tool_name = params.get("name")
        if tool_name == "list_fields":
            fields_text = "\n".join(
                [
                    "Available fields:",
                    *[f"- {field}" for field in FIELDS],
                    "",
                    "Template: collaborators://field/{name}",
                ]
            )
            result = {
                "content": [
                    {
                        "type": "text",
                        "text": fields_text,
                    }
                ]
            }
            return _jsonrpc_result(req_id, result)
        if tool_name == "get_faqs":
            result = {
                "content": [
                    {
                        "type": "text",
                        "text": _faq_questions_text(),
                    }
                ]
            }
            return _jsonrpc_result(req_id, result)

        doc_key = TOOLS.get(tool_name)
        if not doc_key:
            return _jsonrpc_error(req_id, -32602, "Unknown tool")

        if doc_key in {"framework", "commit-format"}:
            url = FRAMEWORK_URL if doc_key == "framework" else COMMIT_FORMAT_URL
            try:
                with urllib.request.urlopen(url, timeout=5) as response:
                    content = response.read().decode("utf-8")
            except OSError:
                return _jsonrpc_error(req_id, -32000, "Document not available")
        else:
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
                    "uri": "collaborators://framework",
                    "name": "Collaborators Framework",
                    "description": "Overview of the Collaborators Framework.",
                    "mimeType": "text/markdown",
                },
                {
                    "uri": "collaborators://commit-format",
                    "name": "Commit Format",
                    "description": "Commit format guidelines.",
                    "mimeType": "text/markdown",
                },
                {
                    "uri": "collaborators://quick-reference",
                    "name": "Quick Reference",
                    "description": "Quick reference guide.",
                    "mimeType": "text/plain",
                }
                ,
                {
                    "uri": "collaborators://fields",
                    "name": "Fields",
                    "description": "List available Collaborators Framework fields.",
                    "mimeType": "text/plain",
                }
                ,
                {
                    "uri": "collaborators://faq",
                    "name": "FAQs",
                    "description": "List available FAQs.",
                    "mimeType": "text/plain",
                }
            ]
        }
        return _jsonrpc_result(req_id, result)

    if method == "resources/templates/list":
        result = {
            "resourceTemplates": [
                {
                    "uriTemplate": "collaborators://field/{name}",
                    "name": "Field",
                    "description": "Collaborators Framework field details.",
                    "mimeType": "text/plain",
                }
                ,
                {
                    "uriTemplate": "collaborators://faq/{name}",
                    "name": "FAQ",
                    "description": "FAQ templates for the Collaborators Framework.",
                    "mimeType": "text/plain",
                }
            ]
        }
        return _jsonrpc_result(req_id, result)

    if method == "resources/read":
        uri = params.get("uri", "")
        if not uri.startswith("collaborators://"):
            return _jsonrpc_error(req_id, -32602, "Unknown resource")
        key = uri.split("collaborators://", 1)[1]
        if key in {"framework", "commit-format"}:
            url = FRAMEWORK_URL if key == "framework" else COMMIT_FORMAT_URL
            try:
                with urllib.request.urlopen(url, timeout=5) as response:
                    content = response.read().decode("utf-8")
            except OSError:
                return _jsonrpc_error(req_id, -32000, "Document not available")
            mime_type = "text/markdown"
            result = {
                "contents": [
                    {
                        "uri": uri,
                        "mimeType": mime_type,
                        "text": content,
                    }
                ]
            }
            return _jsonrpc_result(req_id, result)
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
                        "mimeType": "text/plain",
                        "text": content,
                    }
                ]
            }
            return _jsonrpc_result(req_id, result)
        if key.startswith("faq/"):
            faq_name = key.split("faq/", 1)[1]
            faq = FAQ_TEMPLATES.get(faq_name)
            if not faq:
                return _jsonrpc_error(req_id, -32602, "Unknown resource")
            faq_text = "\n".join(
                [
                    f"Name: {faq_name}",
                    f"Question: {faq['question']}",
                    f"System: {faq['system']}",
                    "",
                    "Message template:",
                    f"- system: {faq['system']}",
                    f"- user: {faq['question']}",
                ]
            )
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
        if key == "fields":
            fields_text = "\n".join(
                [
                    "Available fields:",
                    *[f"- {field}" for field in FIELDS],
                    "",
                    "Template: collaborators://field/{name}",
                ]
            )
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
        if key == "faq":
            result = {
                "contents": [
                    {
                        "uri": uri,
                        "mimeType": "text/plain",
                        "text": _faq_questions_text(),
                    }
                ]
            }
            return _jsonrpc_result(req_id, result)

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
                    "mimeType": "text/plain",
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
