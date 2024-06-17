import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from plotly.subplots import make_subplots



def app():
    comps = pd.read_csv('/Users/ansaha/streamlit-practice/data/comps.csv')
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

    #EV_EBIDTA_GRAPH_1
    ev_ebitda = pd.read_csv('/Users/ansaha/streamlit-practice/data/ev_ebitda.csv')
    ev_ebitda = ev_ebitda.drop(index=ev_ebitda.index[list(range(5, 10)) + list(range(11, len(ev_ebitda)))]).iloc[0:6, 1:]
    ev_ebitda.iloc[:, 0] = pd.to_datetime(ev_ebitda.iloc[:, 0].astype(str), format='%m/%d/%Y')
    ev_ebitda['CNAME_EV/EBITDA'] = pd.to_numeric(ev_ebitda['CNAME_EV/EBITDA'])

    new_ev_ebitda = ev_ebitda

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
    #EV_EBIDTA_GRAPH_2
    fig3 = px.line(new_ev_ebitda, x = new_ev_ebitda.columns[0], y='CNAME_EBITDA', markers=True, 
                labels={
                  new_ev_ebitda.columns[0]: "Time Scale", 
                  'CNAME_EV/EBITDA': "Growth ($)"
                })
    fig3.update_xaxes(
        ticklabelmode="period",
        tickformat="%d/%m/%Y")
    fig3.update_yaxes(
        range=[0, 60],  
        tickvals=list(range(0, 60, 10)),  
        ticktext=[f'${i}' for i in range(0, 60, 10)]  
    )
    fig3.update_layout(
        title="EBITDA, $G"
    )
    fig3.update_traces(mode='lines+markers', textposition='top center', text=new_ev_ebitda['CNAME_EV/EBITDA'])
    fig3.show()
#Cum_PRICE_Graphs
    price_returns = pd.read_csv('/Users/ansaha/streamlit-practice/data/cum_price_returns.csv')
    price_returns = (
        price_returns.set_axis(['Cum Price Returns', 'DVN', 'DJUSEN', 'WTI'], axis = 1).iloc[2:].reset_index(drop=True)
    )
    price_returns['Cum Price Returns'] = pd.to_datetime(price_returns['Cum Price Returns'], format='%m/%d/%Y')
    price_returns[['DVN', 'DJUSEN', 'WTI']] = price_returns[['DVN', 'DJUSEN', 'WTI']].apply(pd.to_numeric)

    fig4 = make_subplots()

    fig4.add_trace(
        go.Scatter(
            x=price_returns['Cum Price Returns'],
            y=price_returns['DVN'],
            name='DVN',
            line=dict(color='black')
        ),
        secondary_y=False,
    )
    fig4.add_trace(
        go.Scatter(
            x=price_returns['Cum Price Returns'],
            y=price_returns['DJUSEN'],
            name='DJUSEN',
            line=dict(color='red')
        ),
        secondary_y=False,
    )
    fig4.add_trace(
        go.Scatter(
            x=price_returns['Cum Price Returns'],
            y=price_returns['WTI'],
            name='WTI',
            line=dict(color='grey')
        ),
        secondary_y=False,
    )
    fig4.update_yaxes(
        title_text='Price',
        titlefont=dict(color='grey'),
        tickfont=dict(color='grey'),
        range=[-1, 4],
        dtick=.5
    )
    fig4.update_layout(
        title_text='Price Performance'
    )

    #Exchange Ratio
    exchange_ratio = pd.read_csv('/Users/ansaha/streamlit-practice/data/exchange_ratio.csv')
    exchange_ratio.iloc[:, 0] = pd.to_datetime(exchange_ratio.iloc[:, 0], format='%m/%d/%Y')
    exchange_ratio['WTI'] = exchange_ratio['WTI'].str.replace('$', '')
    exchange_ratio['CNAME'] = exchange_ratio['CNAME'].str.replace('$', '')
    exchange_ratio[['WTI', 'CNAME']] = exchange_ratio[['WTI', 'CNAME']].apply(pd.to_numeric)


    fig5 = go.Figure()

    fig5.add_trace(
        go.Scatter( x=exchange_ratio.iloc[:, 0], y=exchange_ratio['WTI'], name='WTI', yaxis='y1', line=dict(color='red')
        )
    )
    fig5.add_trace(
        go.Scatter( x=exchange_ratio.iloc[:, 0], y=exchange_ratio['CNAME'], name='CNAME', yaxis='y2', line=dict(color='blue')
        )
    )

    fig5.update_layout(
        title='Market Cap',
        xaxis=dict(
            title='Years'
        ), yaxis=dict( title='WTI in $', titlefont=dict(color='red'), tickfont=dict(color='red'), tickformat='$', range=[0, 150], dtick=50 ),
        yaxis2=dict( title='CNAME in $', titlefont=dict(color='blue'), tickfont=dict(color='blue'), overlaying='y', side='right', range=[0, 400], tickformat='$',  
        ),
        legend=dict( x=0.05, y=0.95, traceorder='normal', font=dict(size=12), bgcolor='rgba(255, 255, 255, 0.5)'
        )
    )

    #Debt_Ratio
    debt_ratio= pd.read_csv('/Users/ansaha/streamlit-practice/data/debt_ratio.csv')
    rows_to_drop = list(range(5, 10)) + list(range(11, len(debt_ratio)))
    debt_ratio = debt_ratio.drop(debt_ratio.index[rows_to_drop])
    new_debt_ratio = debt_ratio.iloc[:,1:]
    new_debt_ratio['CNAME_Debt_Ratio'] = new_debt_ratio['CNAME_Debt_Ratio'].str.replace('%', '')
    new_debt_ratio['CNAME_Debt_Ratio'] = pd.to_numeric(new_debt_ratio['CNAME_Debt_Ratio'])

    fig6 = px.line(new_debt_ratio, x=new_debt_ratio.columns[0], y='CNAME_Debt_Ratio', markers=True, labels={
                  new_debt_ratio.columns[0]: "Time Scale", 
                  'CNAME_Debt_Ratio': "Ratio Change (%)"
              })
    fig6.update_xaxes(
        ticklabelmode="period",
        tickformat="%d/%m/%Y")
    fig6.update_yaxes(
        range=[0, 60],  
        tickvals=list(range(0, 60, 10)),  
        ticktext=[f'{i}%' for i in range(0, 60, 10)]  
    )
    fig6.update_layout(
        title="Debt Ratio",
        paper_bgcolor= None,  
        plot_bgcolor=None  
    )
    fig6.update_traces(mode='lines+markers+text', textposition='top center', text=new_debt_ratio['CNAME_Debt_Ratio'])

    fig7 = px.line(new_debt_ratio, x=new_debt_ratio.columns[0], y='CNAME_FCF', markers=True, labels={
                  new_debt_ratio.columns[0]: "Time Scale", 
                  'CNAME_FCF': "Dollar Change ($)"
              })
    fig7.update_xaxes(
        ticklabelmode="period",
        tickformat="%d/%m/%Y")
    fig7.update_yaxes(
        range=[0, 45],  
        tickvals=list(range(0, 45, 5)),  
        ticktext=[f'{i}$' for i in range(0, 45, 5)]  
    )
    fig7.update_layout(
        title="FCF",
        paper_bgcolor=None,  
        plot_bgcolor=None  
    )
    fig7.update_traces(mode='lines+markers+text', textposition='top center', text=new_debt_ratio['CNAME_FCF'])


    capital_structure = pd.read_csv('/Users/ansaha/streamlit-practice/data/capital_structure.csv')
    fig8 = go.Figure()

    max_y = capital_structure[['Start', 'Value', 'Total']].values.max()

    fig8.add_trace(go.Bar(
        x=capital_structure['Unnamed: 0'],
        y=capital_structure['Start'],
        name='Start',
        marker=dict(
                color=None,
                line=dict(color='white', width=2)  # Set border color to white and width to 2
            )
    ))

    fig8.add_trace(go.Bar(
        x=capital_structure['Unnamed: 0'],
        y=capital_structure['Value'],
        name='Value',
        marker_color='orange',
        text=capital_structure['Value'],
        textposition='auto'
    ))

    fig8.update_layout(
        title='Stacked Bar Chart with Total Column',
        xaxis_title='Categories',
        yaxis_title='Values',
        barmode='stack',
        plot_bgcolor=None, 
        paper_bgcolor=None
    )
    fig8.update_yaxes(
        range=[0, 60], 
        linecolor='black'
    )
    fig8.update_xaxes(
        linecolor='black', 
    )


    fig8.show()



    figures = [fig, fig2, fig3, fig4, fig5, fig6, fig7, fig8]


    num_columns = 2 
    columns = st.columns(num_columns)

    for i, fig in enumerate(figures):
        with columns[i % num_columns]:
            st.plotly_chart(fig, use_container_width=True)  
