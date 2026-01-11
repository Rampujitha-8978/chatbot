
from google import genai
from flask import Flask, app,request,render_template
client=genai.Client(api_key="")
app=Flask(__name__)

@app.route('/')

def home():

    return render_template('index.html')

@app.route("/chat",methods=["POST"])

def chat():

    prompt=request.json["message"]

    response=client.models.generate_content(

        models="gemini-2.5-flash",

        contents=prompt

    )

    return jsonify({"reply":response.text})


app.run(port=8000)
