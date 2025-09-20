from flask import Flask, jsonify, request
import api_checklive
app = Flask(__name__)

@app.get("/")
def ping():
    return jsonify(ok=True)

@app.get("/checklive.php")

def check_username():
    account = request.args.get("account", "")
    api_key = request.args.get("api_key", "")
    if api_key != "nguyentuananh":
        return {"error": "api_key khong hợp lệ"}
    username = account.split("|")[0]
    status = api_checklive.Check(username=username).checking()
    print(status)


    if status == None:
        response = {
            "status": "fail",
            "data": {
                "username": username,
                "status": "None"
            },
            "message": "Check live completed failed."
            }
        

    elif status == True:
        response = {
            "status": "success",
            "data": {
                "username": username,
                "status": "live"
            },
            "message": "Check live completed successfully."
            }
    else:
        response = {
            "status": "success",
            "data": {
                "username": username,
                "status": "die"
            },
            "message": "Check live completed successfully."
            }
    return jsonify(response)

    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


#   cloudflared tunnel --url http://127.0.0.1:8080
