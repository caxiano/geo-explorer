"""Servidor MCP mínimo, compatível com transporte JSON-RPC por stdin/stdout."""

import json
import sys

from .core import challenge, certificate, trail


def handle(request: dict) -> dict:
    method = request.get("method")
    request_id = request.get("id")
    if method == "initialize":
        result = {"protocolVersion": "2024-11-05", "capabilities": {"tools": {}}, "serverInfo": {"name": "geo-explorer", "version": "1.0.0"}}
    elif method == "tools/list":
        result = {"tools": [
            {"name": "trilha", "description": "Consulta uma trilha.", "inputSchema": {"type": "object", "properties": {"tecnologia": {"type": "string"}, "nivel": {"type": "string"}}, "required": ["tecnologia", "nivel"]}},
            {"name": "desafio", "description": "Gera um desafio.", "inputSchema": {"type": "object", "properties": {"tecnologia": {"type": "string"}, "nivel": {"type": "string"}}, "required": ["tecnologia", "nivel"]}},
            {"name": "certificado", "description": "Gera um certificado fictício.", "inputSchema": {"type": "object", "properties": {"nome": {"type": "string"}, "tecnologia": {"type": "string"}, "nivel": {"type": "string"}}, "required": ["nome", "tecnologia", "nivel"]}}
        ]}
    elif method == "tools/call":
        name = request["params"]["name"]
        args = request["params"].get("arguments", {})
        output = {"trilha": trail, "desafio": challenge, "certificado": certificate}[name](**args)
        result = {"content": [{"type": "text", "text": output}]}
    else:
        return {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32601, "message": "Método não encontrado"}}
    return {"jsonrpc": "2.0", "id": request_id, "result": result}


def main() -> None:
    for line in sys.stdin:
        try:
            print(json.dumps(handle(json.loads(line)), ensure_ascii=False), flush=True)
        except Exception as error:
            print(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(error)}}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
