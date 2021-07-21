from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from com_in_ineuron_ai_utils.utils import decodeImage
from predict import dogcat
from PIL import Image
from matplotlib import pyplot as plt
from com_in_ineuron_ai_utils import utils
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')
application = Flask(__name__)
CORS(application)




#@cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = dogcat(self.filename)



@application.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')
    

@application.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.files['file']
    if image.filename != '':
        image.save("inputImage.jpg")
  #  decodeImage(image, clApp.filename)
    result = clApp.classifier.predictiondogcat()
    img = Image.fromarray(result, 'RGB')
    plt.imshow(img)
    img.save("output.jpg")
    s=utils.encodeImageIntoBase64("output.jpg")
    s=str(s, 'UTF-8')
   # import base64
 #   with open("output.jpg", "rb") as img_file:
    #    my_string = base64.b64encode(img_file.read())
    #result=my_string
    return render_template("result.html",result=s)
  #  return render_template("result.html",user_image=img)

  #  image = request.json['image']
   # decodeImage(image, clApp.filename)
   # result = clApp.classifier.predictiondogcat()
   # return jsonify(result)
clApp = ClientApp()
#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    application.run()

 #   app.run(host='0.0.0.0', port=8000, debug=True)

    #app.run(host='0.0.0.0', port=port)
