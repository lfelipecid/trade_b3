import plotly.graph_objs as go
from plotly.subplots import make_subplots


class PlotData:

    df = None

    def fig_candlestick(self, fixrange=False):
        df = self.df

        # Create Subplot
        fig = make_subplots(
            rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, subplot_titles=('OHLC', 'Volume'),
            row_width=[0.2, 0.7]
        )

        """ 1st Row """
        # OHLC Chart

        fig.add_trace(go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            name='OHLC',

            # Color
            increasing={
                'line': {
                    'color': 'green',
                    'width': 1,
                },
                'fillcolor': 'green'
            },
            decreasing={
                'line': {
                    'color': 'red',
                    'width': 1,
                },
                'fillcolor': 'red'
            },

        ), col=1, row=1)

        """ 2nd Row """
        fig.add_trace(go.Bar(
            x=df.index,
            y=df['Volume'],
            showlegend=False), row=2, col=1)

        fig.update_layout(
            margin={
                'l': 0,
                'r': 0,
                't': 0,
                'b': 0,
            },
            plot_bgcolor='white',
            dragmode='pan',
            # Mode Bar
            modebar={
                'activecolor': 'black',
                'orientation': 'h',
                'add': ['drawline', 'drawcircle', 'drawrect', 'eraseshape'],
                'remove': ['hoverClosestCartesian', 'hoverCompareCartesian', 'zoom2d', 'select2d', 'lasso2d',
                           'resetScale2d', 'toggleSpikelines', 'toImage: sendDataToCloud'],
            }
        )

        fig.update_xaxes(
            rangeslider_visible=False,
            title_font={'size': 20},
            showline=True,
            linewidth=2,
            linecolor='gray',
            gridcolor='whitesmoke',
            tickformat='%d/%m\n%Y',

            # Remove VOID SPACES
            # rangebreaks=[
            #     dict(bounds=["sat", "mon"]),
            # ],

            # range=[plot_date[-zoom_range], new_dt]

        )

        fig.update_yaxes(
            fixedrange=fixrange,
            # type='log',
        )

        fig.update(layout_xaxis_rangeslider_visible=False)

        return fig

    @staticmethod
    def fig_show(fig):
        config = {
            'scrollZoom': True,
            'displayModeBar': True,
            'displaylogo': False,
        }
        fig.show(config=config)