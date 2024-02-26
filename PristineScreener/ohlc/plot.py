import plotly.graph_objects as go

def createChart(complete_data, ticker, now, htmlLocation, timeframe):
    #Only use small portion of data to make chart more clear
    complete_data = complete_data[0:40]
    #Set Plotly candlestick chart parameters
    candlestick = go.Candlestick(
                                x=complete_data.index,
                                open=complete_data['Open'],
                                high=complete_data['High'],
                                low=complete_data['Low'],
                                close=complete_data['Close']
                                )
    #Configure simple moving average2
    sma_20 = go.Scatter(x=complete_data.index,
                     y=complete_data["SMA_20"],
                     name="SMA"
                    )
    sma_50 = go.Scatter(x=complete_data.index,
                     y=complete_data["SMA_50"],
                     name="SMA"
                    )

    fig = go.Figure(data=[candlestick, sma_20, sma_50])

    fig.update_layout(xaxis_rangeslider_visible=False, 
                      width=1000, height=800,
                      showlegend=False)

    if timeframe == "1h":
        fig.update_xaxes(rangebreaks=[dict(bounds=[16, 9.5], pattern="hour"),
                              dict(bounds=['sat', 'mon'])])       
    else:
        fig.update_xaxes(
            rangebreaks=[
                dict(bounds=["sat", "mon"]) # hide weekends
            ]
        )   

    fig.update_layout(
        plot_bgcolor='#34495e',
        paper_bgcolor='rgba(0,0,0,0)',
        title_font_color="white",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )
    
    #Save to html location
    image = htmlLocation+"/{}.png".format(ticker.strip())
    #If 1h screen, define hourly folder
    if timeframe == "1h":
        image = htmlLocation+"/hourly/{}.png".format(ticker.strip())
    fig.write_image(image)
    #fig.show()
