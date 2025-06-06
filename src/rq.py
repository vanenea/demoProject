import json
from datetime import date
from dateutil.relativedelta import relativedelta
import requests as req

def post():
    today = date.today()
    data = {
        "asc":False,
        "orderBy":"create_time",
        "pageCurrent":1,
        "pageSize":1000,
        "project":"mwwechat",
        "codeBranch":"",
        "commitMessage":"",
        "squadId":"",
        "committer":"",
        "reviewViewer":"",
        "reviewResult":"未评审",
        "problemType":"",
        "beginDate": f"{(today + relativedelta(months=-1)).strftime('%Y%m%d')}",
        "endDate":f"{today.strftime('%Y%m%d')}"
    }
    print(json.dumps(data, ensure_ascii=False))
    response = req.post('https://com/agile/v1/code-review/list', json=data)
    print(response.text)
    result = response.json()
    if result.get("errorCode") == "000000":
        codeList = result.get("codeList", []) # []为默认值
        for code in codeList:
            code = {k: v for k, v in code.items() if v is not None}
            code["updateUser"] = ""
            code["reviewResult"] = "通过"
            print(json.dumps(code, ensure_ascii=False))
            rs = req.post("https://com/agile/v1/code-review", json=code, headers={"Content-Type": "application/json"})
            print(rs.text)

if __name__ == '__main__':
    post()