import streamlit as st
from core.analyzer import analyze_dataset, plot_histograms, correlation_matrix
from agents.ai_agent import generate_code
from core.analyzer import analyze_dataset
from core.code_executor import run_code
from utils.clean_code import clean_ai_code

st.title("AI Dataset Analyzer")

uploaded_file = st.file_uploader("Upload a CSV dataset", type=["csv"])

if uploaded_file:
    df, results = analyze_dataset(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Shape")
    st.write(f"Rows: {results['shape'][0]}, Columns: {results['shape'][1]}")

    st.subheader("Missing Values")
    st.write(results["missing_values"])

    st.subheader("Correlation Matrix")
    corr_fig = correlation_matrix(df)

    if corr_fig:
        st.pyplot(corr_fig)

    st.subheader("Column Distributions")

    histograms = plot_histograms(df)

    for fig in histograms:
        st.pyplot(fig)
    
    st.subheader("Ask Questions About Your Dataset")

st.subheader("AI Data Analysis")

question = st.text_input("Ask a data analysis question")

if question:

    code = generate_code(question, df.columns)
    code = clean_ai_code(code)
    
    with st.expander("Show AI Generated Code"):
        st.code(code, language="python")

    result = run_code(code, df)
    
    if isinstance(result, dict):
        if "plt" in result:
            st.pyplot(result["plt"])
            
    st.subheader("Execution Result")
    st.write(result)