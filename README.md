# Playeasy GIS Analysis

Converts a downloaded dataset of sports facilities in Michigan into a CSV for GIS analysis.

API endpoint: https://api.playeasy.com/facility-mgmt/api/facilities/search?offset=0&take=1000&api-version=1.1

Request payload:
```
{
	"data": {
		"states": [
			"Michigan"
		],
		"isActive": "true"
	}
}
```

In partnership with Eli Feldman: <elifeld@umich.edu>