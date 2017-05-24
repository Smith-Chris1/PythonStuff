wget --quiet \
  --method GET \
  --header 'authorization: Basic Y2hyaXMuc21pdGhAc3R1ZGllc3dlZWtseS5jb206TW92aWVzIzEy' \
  --header 'cache-control: no-cache' \
  --header 'postman-token: bf2841ab-03bb-58a0-ebca-4bd087351752' \
  --output-document \
  - http://studiesweekly.go.easyprojects.net/rest/v1/projects | jq -r 'Name'