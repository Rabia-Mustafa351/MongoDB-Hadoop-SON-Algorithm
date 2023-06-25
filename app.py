from flask import Flask , render_template,url_for,request
import os,glob

#f=open('myfile1.txt','r')
#g= f.read()
#g = g.replace('\n', '<br>')
with open(r"myfile1.txt", 'r') as fp:
    x= len(fp.readlines())
print('Total lines:', x) # 84 in this case
# now we will split this int to 
FH=x/2
st1="" # store 1st half
st2="" # store 1st half
# now for last half of the file 
with open('myfile1.txt', 'r') as fp:
    for i in range (x):
        if(i<FH):
            line = fp.readline()
            st1=st1 +line
        elif(i>FH):
            line = fp.readline()
            st2=st2 +line
#print(st2)
st1 = st1.replace('\n', '<br>')
st2= st2.replace('\n', '<br>')
app = Flask(__name__)
#app = Flask(__name__, template_folder='../templates', static_folder='../static')
 
@app.route('/')
def hello_world():
    print("hw")
   # app = Flask(__name__, template_folder='../templates', static_folder='../static')
    return render_template('page-2.html',c1=st1,c2=st2)
if __name__ == '__main__':

    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)
    #
    app.run(debug=True)
    #app.run(port=8091)