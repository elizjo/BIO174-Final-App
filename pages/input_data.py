from .mlp_model import prediction

def input_page(st, **state):
    st.header("Is it an Intrinsically Disordered Protein?")
    with st.form("my_form"):
        st.write("Input Protein Characteristics")
        seq_len = st.slider("Sequence Length", min_value=1, max_value=34350)
        st.write("Note: for better results, ensure that as sequence length increases, molecular weight also generally increases")
        
        mole_w = st.slider("Molecular Weight", min_value=75, max_value=3815983)
    
        gravy = st.slider("average hydrophobicity and hydrophilicity (GRAVY Score)", min_value=-4.5, max_value=4.5)
        st.write("^Note: negative scores = more likely to be hydrophilic, positive scores = more likely to be hydrophobic")
        instab = st.slider("Instability Index", min_value=-86, max_value=525)
        aromat = st.slider("Aromaticity", min_value=0.0, max_value=1.0)
        st.write("My guess:")
        checkbox_val = st.checkbox("Disordered")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Predict!")
        
        if submitted:
            outcome = prediction(seq_len, mole_w, gravy, instab, aromat)
            st.write(f"The model predicts: {outcome}")
            if checkbox_val & (outcome == "Disordered"):
                st.write("Your guess matched the model prediction!") 
            else:
                st.write("Your guess disagrees with the model prediction!") 

    