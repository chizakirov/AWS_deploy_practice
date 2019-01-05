from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball_leagues": League.objects.filter(name__contains = "Baseball"),
		"women_leagues": League.objects.filter(name__contains = "Women"),
		"not_fb_leagues":League.objects.exclude(name = "Football"),
		"t_teams": Team.objects.filter(team_name__startswith="T"),
		"cooper_player":Player.objects.filter(last_name = "Cooper").exclude(first_name = "Joshua")
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")