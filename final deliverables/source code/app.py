from flask import Flask,rendor_template
app=Flask(__name__)
@app.route('/')
def bank():
   return rendor_template('chatbot.html')
if __name__=='__main__':
    app.run(debug= True)
