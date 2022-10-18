# lets us understand how get req work
from flask import Flask,request, jsonify

app = Flask(__name__)
@app.route("/testfun")
# if method is not mentioned then it will take GET by default
def test():
    get_name=request.args.get("get_name") # here it is loking for a name
    mobile_number=request.args.get("mobile")
    mail_id=request.args.get("mail_id")
    return ("hi how are you {} {} {}").format(get_name,mobile_number,mail_id)


# passing the data through unsecure mode i.e through url it self
# like this ---> http://127.0.0.1:8000/testfun?get_name=prikshit
# second time ---->http://127.0.0.1:8000/testfun?get_name=prikshit%20sharma%20&mobile=927362736523&mail_id=prikshit@gamil.com

if __name__ =='__main__':
    app.run(port=8000)