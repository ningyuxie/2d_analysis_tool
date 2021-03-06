#!usr/bin/python3.4
#-*-coding:utf-8-*

import sys
import os
sys.path.append("lib")
import file_manager as fm
import data_visualizer as dv

rcg = fm.read_file("logs/20140709193255-HELIOS2014_3-vs-WrightEagle_0.rcg")
rcl = fm.read_file("logs/20140709193255-HELIOS2014_3-vs-WrightEagle_0.rcl")
path = "20140709193255-HELIOS2014_3-vs-WrightEagle_0/"

teams = fm.find_teams(rcg)
#print teams

ball_data = fm.get_ball_data(rcg)
#print ball_data

kick_data = fm.get_kick_data(rcl, ball_data)
#print kick_data

#passes = fm.get_passes(kick_data)
#print passes

#dribbles = fm.get_dribbles(kick_data)
#print dribbles

kick_chains = fm.get_kick_chains(kick_data)
#print kick_chains

success_kick_chains = fm.get_success_kick_chains(kick_chains)
#print success_kick_chains
#print success_kick_chains

#faults = fm.get_faults(rcl, ball_data, teams)
#print faults

#offsides = fm.get_offsides(rcl, ball_data, teams)
#print offsides

corner_kicks = fm.get_corner_kicks(rcl, ball_data, teams)
#print corner_kicks

#kick_in = fm.get_kick_in(rcl, ball_data, teams)
#print kick_in

#goal_kicks = fm.get_goal_kicks(rcl, ball_data, teams)
#print goal_kicks

#ball_possession = fm.ball_possession(kick_chains, teams)
#print teams[0] + " : " + str(ball_possession[0]) + "%"
#print teams[1] + " : " + str(ball_possession[1]) + "%"

success_corner_kicks = fm.get_success_corner_kicks(success_kick_chains)
#print success_corner_kicks

#if os.path.isdir("save/" + path) is False:
	#os.mkdir("save/" + path)

#dv.plot_ball_pos(ball_data, teams, path)
#dv.scatter_kick_pos(kick_data, teams, ball_possession, path)
#dv.plot_kick_chains(kick_chains, teams, path)
#dv.plot_kick_chains(success_kick_chains, teams, path)
#dv.plot_faults(faults, teams, path, "faults")
#dv.plot_faults(offsides, teams, path, "offsides")
#dv.plot_faults(kick_in, teams, path, "kick_in")
#dv.plot_faults(goal_kicks, teams, path , "goal_kick")
dv.plot_kick_chains(success_corner_kicks, teams, "")
