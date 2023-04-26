"""River Simulation."""
__author__ = "730578942"


from exercises.ex09.river import River


my_river: River = River(10, 100)


my_river.view_river()

my_river.one_river_week()