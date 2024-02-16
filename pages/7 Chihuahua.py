# @Email:  contact@pythonandvba.com
# @Website:  https://pythonandvba.com
# @YouTube:  https://youtube.com/c/CodingIsFun
# @Project:  Sales Dashboard w/ Streamlit



import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit




# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="CENSO-2020-PEA-Chihuahua", page_icon=":bar_chart:", layout="wide")

st.title("POBLACIÓN ECONÓMICAMENTE ACTIVA (PEA)")
st.subheader("")
st.subheader("")

df = pd.read_csv('Glosario.csv', )
st.dataframe(df)




# ---- READ EXCEL ----
@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
        io="Chihuahua.xlsx",
        engine="openpyxl",
        sheet_name="Chihuahua",
        skiprows=3,
        usecols="B:Q",
        nrows=67,
    )
    # Add 'hour' column to dataframe
    ###df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df

df = get_data_from_excel()

# ---- SIDEBAR ----
st.sidebar.header("Por favor seleccione un filtro:")
entidad = st.sidebar.multiselect(
    "Seleccione una entidad:",
    options=df["Entidad"].unique(),
    default=df["Entidad"].unique()
)

municipio = st.sidebar.multiselect(
    "Seleccione un municipio:",
    options=df["Municipio"].unique(),
    default=df["Municipio"].unique(),
)


df_selection = df.query(
    "Entidad == @entidad & Municipio ==@municipio"
)

# Check if the dataframe is empty:
if df_selection.empty:
    st.warning("¡No hay datos disponibles según la configuración de filtro actual!")
    st.stop() # This will halt the app from further execution.

# ---- MAINPAGE ----

st.subheader("")
st.subheader("")

st.title(":bar_chart: Chihuahua")
st.markdown("##")

# TOP KPI's
t1 = int(df_selection["PEA"].sum())
t2 = int(df_selection["PEA_F"].sum())
t3 = int(df_selection["PEA_M"].sum())
t4 = int(df_selection["PE_INAC"].sum())
t5 = int(df_selection["PE_INAC_F"].sum())
t6 = int(df_selection["PE_INAC_M"].sum())
t7 = int(df_selection["POCUPADA"].sum())
t8 = int(df_selection["POCUPADA_F"].sum())
t9 = int(df_selection["POCUPADA_M"].sum())
t10 = int(df_selection["PDESOCUP"].sum())
t11 = int(df_selection["PDESOCUP_F"].sum())
t12 = int(df_selection["PDESOCUP_M"].sum())






#average_rating = round(df_selection["Rating"].mean(), 1)
#star_rating = ":star:" * int(round(average_rating, 0))
#average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("PEA TOTAL:")
    st.subheader(f"{t1:,}")
with middle_column:
    st.subheader("PEA_Mujer:")
    st.subheader(f"{t2:,}")
with right_column:
    st.subheader("PEA_Hombre:")
    st.subheader(f"{t3:,}")  
    
    
        
with left_column:
    st.subheader("")
    st.subheader("")
    st.subheader("POCUPADA:")
    st.subheader(f"{t7:,}")
with middle_column:
    st.subheader("")
    st.subheader("")
    st.subheader("POCUPADA_Mujer:")
    st.subheader(f"{t8:,}")
with right_column:
    st.subheader("")
    st.subheader("")
    st.subheader("POCUPADA_Hombre:")
    st.subheader(f"{t9:,}")    



with left_column:
    st.subheader("")
    st.subheader("")
    st.subheader("PDESOCUP:")
    st.subheader(f"{t10:,}")
with middle_column:
    st.subheader("")
    st.subheader("")
    st.subheader("PDESOCUP_Mujer:")
    st.subheader(f"{t11:,}")
with right_column:
    st.subheader("")
    st.subheader("")
    st.subheader("PDESOCUP_Hombre:")
    st.subheader(f"{t12:,}")  



with left_column:
    st.subheader("")
    st.subheader("")
    st.subheader("")
    st.subheader("PE_INAC:")
    st.subheader(f"{t4:,}")
with middle_column:
    st.subheader("")
    st.subheader("")
    st.subheader("")
    st.subheader("PE_INAC_Mujer:")
    st.subheader(f"{t5:,}")
with right_column:
    st.subheader("")
    st.subheader("")
    st.subheader("")
    st.subheader("PE_INAC_Hombre:")
    st.subheader(f"{t6:,}")         
    

st.markdown("""---""")

#HASTA AQUI FUNCIONA
###############################################################################################


#GRÁFICAS 1 Y 2



f1 = df_selection.groupby(by=["Municipio"])[["PEA"]].sum().sort_values(by="PEA")
fig1 = px.bar(
    f1,
    x="PEA",
    y=f1.index,
    orientation="h",
    title="<b>Población económicamente activa</b>",
    color_discrete_sequence=["#621132"] * len(f1),
    template="plotly_white",
)
fig1.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


f2 = df_selection.groupby(by=["Municipio"])[["PEA_F"]].sum().sort_values(by="PEA_F")
fig2 = px.bar(
    f2,
    x="PEA_F",
    y=f2.index,
    orientation="h",
    title="<b>Población económicamente activa-FEMENINA</b>",
    color_discrete_sequence=["#621132"] * len(f2),
    template="plotly_white",
)
fig2.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig1, use_container_width=True)
right_column.plotly_chart(fig2, use_container_width=True)


#AQUI TERMINA LAS PRIMERAS 2 GRÁFICAS Y FUNCIONA
############################################################################################
st.subheader("")
st.subheader("")
st.subheader("")
st.subheader("")
############################################################################################
#GRÁFICAS 3 Y 4

f3 = df_selection.groupby(by=["Municipio"])[["PEA_M"]].sum().sort_values(by="PEA_M")
fig3 = px.bar(
    f3,
    x="PEA_M",
    y=f3.index,
    orientation="h",
    title="<b>Población económicamente activa-MASCULINA</b>",
    color_discrete_sequence=["#621132"] * len(f3),
    template="plotly_white",
)
fig3.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


f4 = df_selection.groupby(by=["Municipio"])[["PE_INAC"]].sum().sort_values(by="PE_INAC")
fig4 = px.bar(
    f4,
    x="PE_INAC",
    y=f4.index,
    orientation="h",
    title="<b>Población económicamente-INACTIVA</b>",
    color_discrete_sequence=["#621132"] * len(f4),
    template="plotly_white",
)
fig4.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig3, use_container_width=True)
right_column.plotly_chart(fig4, use_container_width=True)
############################################################################################

############################################################################################
#GRÁFICAS 5 Y 6

f5 = df_selection.groupby(by=["Municipio"])[["PE_INAC_F"]].sum().sort_values(by="PE_INAC_F")
fig5 = px.bar(
    f5,
    x="PE_INAC_F",
    y=f5.index,
    orientation="h",
    title="<b>Población económicamente INACTIVA-FEMENINA</b>",
    color_discrete_sequence=["#621132"] * len(f5),
    template="plotly_white",
)
fig5.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


f6 = df_selection.groupby(by=["Municipio"])[["PE_INAC_M"]].sum().sort_values(by="PE_INAC_M")
fig6 = px.bar(
    f6,
    x="PE_INAC_M",
    y=f6.index,
    orientation="h",
    title="<b>Población económicamente INACTIVA-MASCULINA</b>",
    color_discrete_sequence=["#621132"] * len(f6),
    template="plotly_white",
)
fig4.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig5, use_container_width=True)
right_column.plotly_chart(fig6, use_container_width=True)
############################################################################################


############################################################################################
#GRÁFICAS 7 Y 8

f7 = df_selection.groupby(by=["Municipio"])[["POCUPADA"]].sum().sort_values(by="POCUPADA")
fig7 = px.bar(
    f7,
    x="POCUPADA",
    y=f7.index,
    orientation="h",
    title="<b>Población Ocupada</b>",
    color_discrete_sequence=["#621132"] * len(f7),
    template="plotly_white",
)
fig5.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


f8 = df_selection.groupby(by=["Municipio"])[["POCUPADA_F"]].sum().sort_values(by="POCUPADA_F")
fig8 = px.bar(
    f8,
    x="POCUPADA_F",
    y=f8.index,
    orientation="h",
    title="<b>Población Ocupada-FEMENINA</b>",
    color_discrete_sequence=["#621132"] * len(f8),
    template="plotly_white",
)
fig4.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig7, use_container_width=True)
right_column.plotly_chart(fig8, use_container_width=True)
############################################################################################

############################################################################################
#GRÁFICAS 9 Y 10

f9 = df_selection.groupby(by=["Municipio"])[["POCUPADA_M"]].sum().sort_values(by="POCUPADA_M")
fig9 = px.bar(
    f9,
    x="POCUPADA_M",
    y=f9.index,
    orientation="h",
    title="<b>Población Ocupada-MASCULINA</b>",
    color_discrete_sequence=["#621132"] * len(f9),
    template="plotly_white",
)
fig9.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


f10 = df_selection.groupby(by=["Municipio"])[["PDESOCUP"]].sum().sort_values(by="PDESOCUP")
fig10 = px.bar(
    f10,
    x="PDESOCUP",
    y=f10.index,
    orientation="h",
    title="<b>Población Desocupada</b>",
    color_discrete_sequence=["#621132"] * len(f10),
    template="plotly_white",
)
fig4.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig9, use_container_width=True)
right_column.plotly_chart(fig10, use_container_width=True)
############################################################################################

############################################################################################
#GRÁFICAS 11 Y 12

f11 = df_selection.groupby(by=["Municipio"])[["PDESOCUP_F"]].sum().sort_values(by="PDESOCUP_F")
fig11 = px.bar(
    f11,
    x="PDESOCUP_F",
    y=f11.index,
    orientation="h",
    title="<b>Población Desocupada-FEMENINA</b>",
    color_discrete_sequence=["#621132"] * len(f11),
    template="plotly_white",
)
fig11.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


f12 = df_selection.groupby(by=["Municipio"])[["PDESOCUP_M"]].sum().sort_values(by="PDESOCUP_M")
fig12 = px.bar(
    f12,
    x="PDESOCUP_M",
    y=f12.index,
    orientation="h",
    title="<b>Población Desocupada-MASCULINA</b>",
    color_discrete_sequence=["#621132"] * len(f12),
    template="plotly_white",
)
fig4.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig11, use_container_width=True)
right_column.plotly_chart(fig12, use_container_width=True)
############################################################################################




# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

