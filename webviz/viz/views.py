from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objects as go
from .models import TMDB
from django.http import Http404


# Create your views here.
def home(request):
    movies = TMDB.objects.all()
    x = []
    y = []
    for item in movies:
        x.append(item.title)
        y.append(item.popularity)

    # plot_div = plot([Bar(x=x, y=y,
    #                     mode='lines', name='test',
    #                     opacity=0.8, marker_color='green')],
    #            output_type='div')
    fig = go.Figure()
    bar_chart = go.Bar(x=x, y=y)
    fig.add_trace(bar_chart)
    plot_div = plot(fig, output_type='div')
    return render(request, "index.html", context={'plot_div': plot_div})

    # return render(request, 'index_ori.html', {'movies': movies}, context={'plot_div': plot_div})


def movie_detail(request, viz_id):
    try:
        movie = TMDB.objects.get(id=viz_id)

    except TMDB.DoesNotExist:
        raise Http404('Movie not found!')

    return render(request, 'movie_detail.html', {'movie': movie})

