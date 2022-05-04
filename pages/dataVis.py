import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def data_page(st, **state):
    st.header("Composition of Training Dataset of 250k+ Proteins")
    #Data Set
    catagory =['Disordered', 'Normal']
    
    values = [16316,240481]

    #The plot
    fig = go.Figure(
        go.Pie(
        hole = 0.2,
        labels = catagory,
        values = values,
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    st.plotly_chart(fig)
    
    corData = pd.read_csv("data,model/5varCor.csv")
    heatMap = px.imshow(corData, x=['sequence len', 'molecular weight', 'GRAVY Score', 'instability index', 'aromaticity', 'label'], y=['sequence len', 'molecular weight', 'GRAVY Score', 'instability index', 'aromaticity', 'label'])
    heatMap.update_layout(
            title= "2D Correlation Matrix with Protein Features & Label")
    st.plotly_chart(heatMap)
    
    @st.cache
    def load_data(nrows):
        dataA = pd.read_csv("data,model/all_charA.csv")
        dataB = pd.read_csv("data,model/all_charB.csv")
        data = pd.concat([dataA, dataB])
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        # data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        return data

    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Loading data...')
    # Load 10,000 rows of data into the dataframe.
    data = load_data(10)
    # Notify the reader that the data was successfully loaded.
    
    data_load_state.text("Done! (using st.cache)")
    char_selection = st.selectbox('Characteristic of Interest',
                                ['Sequence Length', 'Molecular Weight', "Average Hydrophobicity and Hydrophilicity (GRAVY)", 'Instability Index', 'Aromaticity'])

        
    @st.cache(allow_output_mutation=True)
    def histogramDisplay(data, query):
        name_dict = {"seq_len": 'Sequence Length', "molecular_weight": 'Molecular Weight', "hydrophobicity": "Average Hydrophobicity and Hydrophilicity (GRAVY)", "instability_index" : "Instability Index", "aromaticity": 'Aromaticity'}
        fig = px.histogram(data, x= data[query], color= data["label"],
                    hover_data=data.columns)
        fig.update_layout(
            title= f"Distribution of {name_dict[query]} of Proteins",
            xaxis_title= name_dict[query],
            yaxis_title="Number of Proteins")
        return fig

    if "Sequence Length" in char_selection:
        # display graph
        query = "seq_len"
        
    if "Molecular Weight" in char_selection:
        # display graph
        query = "molecular_weight"

    if "Average Hydrophobicity and Hydrophilicity (GRAVY)" in char_selection:
         # display graph
        query = "hydrophobicity"
        st.caption('Negative GRAVY Score => more hydrophilic, Positive GRAVY Score => more hydrophobic')

    if "Instability Index" in char_selection:
        # display graph
        query = "instability_index"
        
    if "Aromaticity" in char_selection:
        # display graph
        query = "aromaticity"
        
    figSeq = histogramDisplay(data, query)
        
    st.plotly_chart(figSeq)
    st.caption('1 = Disordered, 0 = Normal')