from django.shortcuts import render
import pandas as pd 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import urllib, base64
import io
pd.set_option('display.max_colwidth',60)

# Create your views here.
def home(request):
    a=pd.read_csv('E:\\gps-django\\trafgraph\\traffic\\data.csv')
    data_html = a.to_html()
    plt.plot(a['Bus'],a['Jambu Savari Dimne'])
    plt.plot(a['Bus'],a['Royal Layout'])
    plt.plot(a['Bus'],a['Platinum Lifestyle'])
    plt.plot(a['Bus'],a['Arya Hamsa Apartment'])
    plt.plot(a['Bus'],a['Lal Bahadur Shastri Nagar'])
    plt.plot(a['Bus'],a['Kembathalli'])
    plt.plot(a['Bus'],a['Load Line'])
    plt.title('Graph showing load at different times')
    plt.xlabel('Time')
    plt.ylabel('Percentage')
    plt.legend(['Jambu Savari Dimne', 'Royal Layout','Platinum Lifestyle','Arya Hamsa Apartment','Lal Bahadur Shastri Nagar ','Kembathalli','Load Line'], loc='upper left')
    plt.rcParams["figure.figsize"]=10,10
    plt.rc('xtick', labelsize=20) 
    plt.rc('ytick', labelsize=20)
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format="png")
    buf.seek(0)
    string= base64.b64encode(buf.read())
    uri=urllib.parse.quote(string)

    return render(request,'traffic/graphh.html',{'data':uri,'dat':data_html})
