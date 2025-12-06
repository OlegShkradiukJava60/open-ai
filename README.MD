# HW#39 Definition
## Update function travelInfoProvider
1. extract Lines 11-19 to one function extractJSON<br>
1.1 extractJson should be universal function taking list of some ordered properties that should be in JSON<br>
1.1.1 For example, extractJSON(text:str, properties: list[ str ])->dict for extracting JSON presenting tool call - extractJSON(text, ["tool", "arguments"]); for extracting JSON containing currency code value - extractJSON(text, ["country", "currency_code"]) (not mandatary to specify all JSON properties)<br>
2. write additional function/s for getting exchange rate from codeFrom (currency code of the country from) to codeTo (currency code of the country to)<br>
2.1 Use the fixer.io API (The most popular currency rates API) with free access key allowing performing request http://data.fixer.io/api/lates?access_key = < API key ><br>
3. fill property exchangeRate with proper value received from function #2

