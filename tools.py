import json
import requests
from system_rules import INNER_SYSTEM_CONTENT
URL = "https://data.fixer.io/api/latest"
ACCSESS_KEY = "b2d71961ebe71a300a02e73d03b6ebc8"
def getExchangeRate(codeFrom:str, codeTo:str)->float:
    resp = requests.get(URL, params={"access_key":ACCSESS_KEY})
    resp.raise_for_status()
    rates = resp.json()["rates"]
    rateFrom = rates[codeFrom]
    rateTo = rates[codeTo]
    return round(rateTo / rateFrom, 2)
    
    
def travelInfoProvider(countryFrom: str, countryTo: str, codeFrom: str):
    from chat_request import chatRequest, extractJSON
    messages: list[dict] = [
        {"role":"system", "content": INNER_SYSTEM_CONTENT},
        {"role":"user", "content": f"currency of {countryTo}"}
    ]
    resp = chatRequest(messages)
    res =  extractJSON(resp, ["country", "currency_name","currency_code"])
    error = None
    try:
        exchangeRate = getExchangeRate(codeFrom, res["currency_code"])
    except Exception as e:
        error = str(e)     
      
    
    return json.dumps({"error":error} if error else {"countryFrom": countryFrom, "countryTo":countryTo,\
        "codeFrom":codeFrom, "codeTo": res["currency_code"], "currencyName": res["currency_name"],"exchangeRate":exchangeRate})
 
TOOLS:dict = {
    "travelInfoProvider": travelInfoProvider
}