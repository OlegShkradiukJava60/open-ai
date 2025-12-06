import json
import re
import requests

from tools import TOOLS


URL:str =  "http://localhost:11434/api/chat"
MODEL_NAME: str = "phi3"
def chatRequest(messages:dict)-> str:
    payload = {
        "model":MODEL_NAME,
        "messages": messages,
        "stream": False,
        "options":{"temperature":0.0}
    }
    resp = requests.post(URL, json=payload)
    resp.raise_for_status()
    data = resp.json()
    return data["message"]["content"]
def extractJSON(text: str, properties: list[str]) -> dict | None:
    propsInRe = '.' + '.'.join(f"*{w}" for w in properties)
    regex:str = fr"\{{{propsInRe}.*\}}"
    match: re.Match = re.search(regex, text, re.DOTALL)
    res = None
    if match:
        try:
            res = json.loads(match.group())
        except Exception:
            pass    
    return res        
def callTool(toolData: dict) -> str:
    res: str = ""
    method = TOOLS.get(toolData.get("tool"))
    
    if method:
        arguments = toolData.get("arguments", {})
        res = method(**arguments)
    return res    
def processLLM(text: str) -> dict:
    res: dict = {"role":"assistant", "content":text}
    toolData: dict | None = extractJSON(text, ["tool", "arguments"])
    if toolData:
        toolRes = callTool(toolData)
        if toolRes:
            res = {"role":"tool", "content": json.dumps({"result":toolRes})}
    return res        
             