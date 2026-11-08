import json
from valhalla import Actor, get_config
print("TESTING")

config = get_config(tile_extract="/home/sasha/valhalla_data/valhalla_tiles.tar", tile_dir="/home/sasha/valhalla_data", verbose=False)
actor = Actor(config)

request = {
	"locations": [
		{"lat": 41.49104, "lon": -71.23516},
		{"lat": 41.26280, "lon": -72.55120},
	],
	"costing": "auto",
	"costing_options": {
		"motor_scooter": {
			"top_speed": 72,
			"use_ferry": 0,
		},
	},
	"units": "miles",
}

route = actor.route(request)
if isinstance(route, str):
	route = json.loads(route)

for m in route["trip"]["legs"][0]["maneuvers"]:
	print(f"{m['instruction']} ({m['length']:.2f} mi)")