#from typing import Text
from flask import *
import qrcode
from PIL import ImageOps
#import os


app = Flask(__name__)  

@app.route('/')  
def home():  
   return render_template("index.html")  

def color_change(image,color):
    qr=qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )
    qr.add_data(image)
    #qr.add_data("two")
    qr.make()
    img=qr.make_image(fill_color=color,back_color="white")
    #img.save("static/qrcode.jpg")
    bimg = ImageOps.expand(img, border=10, fill=color)
    bimg.save("static/qrcode.jpg")

#@app.route("/",methods = ["GET","POST"])  
#def print_data():  
   #if request.method == "POST":  
      #result = request.form  
      #print(result.items)
      #return render_template("result_data.html", result = result)  
@app.route("/RESULT")
def download_file():
    p="static\\qrcode.jpg"
    return send_file(p,as_attachment=True)


@app.route("/TEXT")
def text():
    return render_template("text.html")

@app.route("/TEXT",methods=["GET","POST"])
def show_text():
    if request.method=="POST":
        text=request.form.get("text")
        color=request.form.get("color")
        color_change(text,color)
        #img = qrcode.make(text)
        #img.save("static/t.jpg")
        #i=Image.open("t.png")
        #i.show()
        #print(i)
        #qr=ImageQt(a)
        #pix = QPixmap.fromImage(qr)
        #print(img)
        #print(text)
    return render_template("result.html")

#@app.route("/TEXT")
#def same_page():
    #render_template("result.html")




@app.route("/URL")
def url():
    return render_template("url.html")

@app.route("/URL",methods=["GET","POST"])
def show_url():
    if request.method=="POST":
        url=request.form.get("url")
        color=request.form.get("color")
        color_change(url,color)
        #img = qrcode.make(url)
        #img.save("static/t.jpg")
        #print(url)
        return render_template("result.html")

@app.route("/DETAILS")
def details():
    return render_template("details.html")

@app.route("/DETAILS",methods=["GET","POST"])
def show_details():
    if request.method=="POST":
        name=request.form.get("name")
        address=request.form.get("address")
        email=request.form.get("email")
        phone=request.form.get("phone")
        mobile=request.form.get("mobile")
        fax=request.form.get("fax")
        postcode=request.form.get("postcode")
        city=request.form.get("city")
        state=request.form.get("state")
        country=request.form.get("country")
        website=request.form.get("website")
        color=request.form.get("color")

        
        qr=qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=1
        )
        qr.add_data("NAME : " +name+ "\n")
        qr.add_data("ADDRESS : " +address+ "\n")
        qr.add_data("EMAIL : " +email+ "\n")
        qr.add_data("CONTACT : " +phone+ "\n")
        qr.add_data("MOBILE : " +mobile+ "\n")
        qr.add_data("FAX : " +fax+ "\n")
        qr.add_data("POSTAL CODE : " +postcode+ "\n")
        qr.add_data("CITY : " +city+ "\n")
        qr.add_data("STATE : " +state+ "\n")
        qr.add_data("COUNTRY : " +country+ "\n")
        qr.add_data("WEBSITE: " +website+ "\n")
        #qr.add_data("two")
        qr.make()
        img=qr.make_image(fill_color=color,back_color="white")
        #img.save("static/qrcode.jpg")
        bimg = ImageOps.expand(img, border=10, fill=color)
        bimg.save("static/qrcode.jpg")
        #img.save("static/t.jpg")
        #print(name,address,email,phone,mobile,fax,postcode,city,state,country,website)
        return render_template("result.html")

@app.route("/CONTACT")
def contact():
    return render_template("contact.html")

@app.route("/CONTACT",methods=["GET","POST"])
def show_contact():
    if request.method=="POST":
        contact=request.form.get("contact")
        color=request.form.get("color")
        color_change(contact,color)
        #img = qrcode.make(contact)
        #img.save("static/t.jpg")
        #print(contact)
        return render_template("result.html")

@app.route("/MESSAGE")
def message():
    return render_template("message.html")

@app.route("/MESSAGE",methods=["GET","POST"])
def show_message():
    if request.method=="POST":
        number=request.form.get("number")
        message=request.form.get("message")
        color=request.form.get("color")

        qr=qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
        )
        qr.add_data("NUMBER : " +number+ "\n")
        qr.add_data("MESSAGE : " +message)
        qr.make()
        img=qr.make_image(fill_color=color,back_color="white")
        #img.save("static/qrcode.jpg")
        
        #if isinstance(10, int) or isinstance(10, tuple):
        bimg = ImageOps.expand(img, border=10, fill=color)
        bimg.save("static/qrcode.jpg")
        #img.save("static/t.jpg")
        #color_change(text,color)
        #img = qrcode.make(number)
        #img.add_data(message)
        #img.save("static/t.jpg")                                                      
        #print(number,message)
        return render_template("result.html")

   
if __name__ == "__main__":  
   app.run(debug = True)