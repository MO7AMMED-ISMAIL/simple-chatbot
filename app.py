from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_cors import cross_origin
import random

app = Flask(__name__)
CORS(app)
CORS(app, resources={
    r'/api/*': {
    'origins': 'http://localhost:8080',
    'methods': ['GET', 'POST'],
    'headers': ['Content-Type', 'Authorization']
    }
})

# Create a list of responses
responses = {
    "مرحبا": ["مرحبا", "كيف يمكنني مساعدتك؟"],
    "ما هي خدماتكم؟": ["نحن نوفر خدمات تصميم المواقع وتطوير البرمجيات", "يمكننا أيضاً تقديم خدمات الدعم الفني"],
    "كم تكلفة خدماتكم؟": ["تعتمد التكلفة على نوع الخدمة المطلوبة", "يمكنك التواصل مع فريق المبيعات للحصول على عرض أسعار"],
    "شكرا": ["لا شكر على واجب", "نحن دائماً هنا لمساعدتك"],
    "ما هو الوقت الحالي؟": ["اسق انا مجرد ذكاء اصطناعي لا  يمكنني معرفه الوقت ", "ليس لدي علم"],
    "ما هي افضل لغات البرمجه؟": ['هناك العديد من اللغات البرمجه ولكن افضل لغه البرمجه في الوقت الحالي بايثون', 'C# ,c++ , php , js , python'],
}

# Define a function to generate a response
def generate_response(message):
    if message in responses:
        return random.choice(responses[message])
    else:
        return "آسف، لم أفهم ماذا تعني"

# Define a route for the chatbot
@app.route("/res" , methods=['POST'])
@cross_origin()
def chatbot():
    data = request.json
    message = data.get('mess')
    response = generate_response(message)
    return jsonify({"res": response})

if __name__ == "__main__":
    app.run(debug=True)