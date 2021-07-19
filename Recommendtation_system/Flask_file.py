from flask import Flask, render_template,request

import Recommendation_model
app=Flask(__name__)

@app.route("/", methods=['GET','POST'])
def profile():
      mk=""
      if request.method=="POST":
            item=request.form['Item ID']
            item_pred =Recommendation_model.model(item)
            mk=item_pred
      return render_template("Website.html", recommended_item=mk)

"""@app.route("/submit_page" , methods=['POST'])
def submit():
  if request.method=="POST":
      name = request.form["Item ID"] 
      
  return render_template("submit_page.html",n=name)
  """
if __name__=="__main__":
    app.run(debug=True)