def landing_page(st, **state):
    #links to all Databases
    st.markdown( '''
        # Using Neural Nets to Classify Intrinsically Disordered Proteins 
        Intrinsically disordered proteins (IDPs) and intrinsically disordered regions (IDRs) have unstable
        secondary and tertiary structures for sequences greater than 30 amino acids—a result of the rich polar and
        proline, and depleted hydrophobic residues in sequence compositions. Despite diverging from the
        structure-function paradigm, they participate in critical biological functions such as signaling, regulation
        and control. In the past 20 years, there have been various efforts to elucidate the relationship between
        amino acid sequences and IDP function.
        ## Goal: Classify IDPs from their Primary Sequence
        Three objectives met to build this tool: 
        + curate a training dataset 
        + select appropriate neural net (Multi-layer Perceptron (MLP) Classifier)
        + validating the neural network
        
        ## Data Sources
        Amino acid sequence information was extracted from the following protein databases:
        #### disordered proteins
        + [DisProt](https://disprot.org/)
        + [MobiDB](https://mobidb.bio.unipd.it/)
        #### normal proteins
        + [RSCB RDB](https://www.rcsb.org/)
        
        ## Neural Net Model Selected: Multi-layer Perceptron (MLP) Classifier 
        + supervised learning algorithm
        + [general information](https://scikit-learn.org/stable/modules/neural_networks_supervised.html)
        + [MLP Classifier Sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html)
        + [Hyperparameter Tuning w/ GridSearchCV](https://panjeh.medium.com/scikit-learn-hyperparameter-optimization-for-mlpclassifier-4d670413042b)
        
        ## Tools Used
        + BioPython (Protein Analysis Module)
        + Scikit learn
        + Plotly
        + Numpy & Pandas
        
        ## Feature Selection
        + Extracted Amino Acid Sequences
        + Evaluated AA Sequences using BioPython ([Bio.SeqUtils.ProtParam](https://biopython.org/docs/1.76/api/Bio.SeqUtils.ProtParam.html)) Package
        1. sequence length
            + len(AA)
        2. molecular weight
            + used molecular_weight()
        3. hydrophobicity/ hydrophilicity
            + used gravy()
            + Calculate the gravy according to Kyte and Doolittle
            + Hydrophobicity score (arbitrary unit) below 0 are more likely globular (hydrophilic protein),
            + above 0 are more likely membranous (hydrophobic)
        4. aromaticity
            + Calculates the aromaticity value of a protein according to Lobry, 1994. 
            + relative frequency of Phe+Trp+Tyr
        5. instability_index
            + Calculate the instability index according to Guruprasad et al 1990.
            + Any value above 40 means the protein is unstable (has a short half life)
        
        ## Verifying the Model
        [roc_auc_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html)
        + Computes Area Under the Receiver Operating Characteristic Curve (ROC AUC) from prediction scores.
        
        ## Recap
        + selecting data is extremely important (more than the model)
        + unbalanced datasets need extra attn on selecting testing data
        + guidance on feature selection
        + circular problem of improving model v. finding more representative data
        
        
        ''')