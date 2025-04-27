import plotly.express as px
import geopandas as gpd
from plotly.offline import plot


def plot_map(df):
    if len(df) < 2:
        return "Bouna bağlanılamadı"

    fig = px.scatter_map(df,
                         lat="Enlem",
                         lon="Boylam",
                         hover_name="Yer",
                         size="ML",
                         zoom=5,
                         color="ML",
                         color_continuous_scale=px.colors.sequential.Viridis,
                         map_style="carto-positron",
                         )
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0)

    )
    fig.update_coloraxes(showscale=False)
    return plot(fig, output_type='div', config={'displayModeBar': False})
