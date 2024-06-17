import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker



def app():
    comps = pd.read_csv('/Users/ansaha/streamlit-practice/data/comps.csv')
# Create a bar graph with grouped bars
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=comps['Unnamed: 0'],
            y=comps['CNAME'],
            name='CNAME',
            marker_color='blue',
            text=comps['CNAME'],
            textposition='auto'
    )
)

    fig.add_trace(
        go.Bar(
            x=comps['Unnamed: 0'],
            y=comps['Comps'],
            name='Comps',
            marker_color='orange',
            text=comps['Comps'],
            textposition='auto'
    )
)

    fig.update_layout(
        barmode='group',
        title_text='Comps, LTM1',
        xaxis=dict(
            title='Groups'
        ),
        yaxis=dict(
            title='Values'
        ),
        legend=dict(
            x=0.01, y=0.99,
            traceorder='normal',
            font=dict(size=12)
    )
)

    ev_ebitda = pd.read_csv('/Users/ansaha/streamlit-practice/data/ev_ebitda.csv')
    rows_to_drop = list(range(5, 10)) + list(range(11, len(ev_ebitda)))
    ev_ebitda = ev_ebitda.drop(ev_ebitda.index[rows_to_drop])

    new_ev_ebitda = ev_ebitda.iloc[0:6, 1:]
    new_ev_ebitda.iloc[:, 0] = new_ev_ebitda.iloc[:, 0].astype(str)
    new_ev_ebitda.iloc[:, 0] = pd.to_datetime(new_ev_ebitda.iloc[:, 0], format='%m/%d/%Y')
    new_ev_ebitda['CNAME_EV/EBITDA'] = pd.to_numeric(new_ev_ebitda['CNAME_EV/EBITDA'])

    fig2 = px.line(new_ev_ebitda, x=new_ev_ebitda.columns[0], y='CNAME_EV/EBITDA', markers=True, labels={
                  new_ev_ebitda.columns[0]: "Time Scale", 
                  'CNAME_EV/EBITDA': "Growth (x)"
              })
    fig2.update_xaxes(
        ticklabelmode="instant",
        tickformat="%d/%m/%Y")
    fig2.update_yaxes(
        range=[0, 15],  
        tickvals=list(range(0, 16, 2)),  
        ticktext=[f'{i}x' for i in range(0, 16, 2)]  
    )
    fig2.update_layout(
        title="EV/EBITDA",
        paper_bgcolor=None,  
        plot_bgcolor=None  
    )
    fig2.update_traces(mode='lines+markers+text', textposition='top center', text=new_ev_ebitda['CNAME_EV/EBITDA'])

    # Show the plot
    with st.expander("CNAME Values", expanded=True):
        container1 = st.container()
        with container1:
            st.plotly_chart(fig, use_container_width=True)

    with st.expander("Comps Values", expanded=True):
        container2 = st.container()
        with container2:
            st.plotly_chart(fig2, use_container_width=True)
    

