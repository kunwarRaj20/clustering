import streamlit as st
import pandas as pd
import joblib
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(page_title="Customer Segmentation Web App", layout="centered")

with st.container():
    st.title("Customer Segmentation")
    st.write("Segement customer based on various factors")

with open('app.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


cs = joblib.load('customer_segmentation_cluster.pkl')


def segment_customers(input_data):
    
    prediction=cs.predict(pd.DataFrame(input_data, columns=['Income','Kidhome','Teenhome','Age','Partner','Education']))
    pred_1 = 0
    if prediction == 0:
            pred_1 = 'Cluster 0'
    elif prediction == 1:
            pred_1 = 'Cluster 1'
    elif prediction == 2:
            pred_1 = 'Cluster 2'
    elif prediction == 3:
            pred_1 = 'Cluster 3'
    elif prediction == 4:
            pred_1 = 'Cluster 4'
    elif prediction == 5:
            pred_1 = 'Cluster 5'

    return pred_1

def main():
    
    Income = st.number_input("Type In The Household Income", min_value=10000, max_value=300000, value=10000, step=20000)
    Kidhome = st.radio ( "What is the number Of kids in the household?", ('0', '1','2') )
    Teenhome = st.radio ( "What is the number of teens in the household?", ('0', '1','2') )
    Age = st.slider ( "Please select your age", 18, 85 )
    Partner = st.radio ( "Are you living with a partner?", ('Yes', 'No') )
    Education = st.radio ( "What is your educantion level?", ("Undergraduate", "Graduate", "Postgraduate") )
    
    result = ""

    if st.button("Segment Customer"):
        print(Income)
        result=segment_customers([[Income,Kidhome,Teenhome,Age,Partner,Education]])
        st.success(result)

    if st.button("Reset"):
        streamlit_js_eval(js_expressions="parent.window.location.reload()")


if __name__ == '__main__':
        main ()