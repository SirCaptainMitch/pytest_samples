import json

d = {
  "assistant_captain": [
      "Olimebus#1241",
      "TheCaptain#12345"
  ],
  "captain": "BornToShine#11556",
  "division_concat": "e-east",
  "division_display_name": "E East",
  "hp_mmr_avg": 2704,
  "ngs_id": "600638ca0b86d20028380496",
  "ngs_mmr_avg": "",
  "roster_path": "./app/data/teams/e-east/600638ca0b86d20028380496.json",
  "team_description": "We're a brand new team looking to learn to work together and see how we do in competitive play.",
  "team_members": [
      {
          "battletag": "BornToShine#11556",
          "blizz_id": 6612101,
          "full_battletag": "BornToShine%2311556",
          "heroes_profile": "https://www.heroesprofile.com/Profile/?blizz_id=6612101&battletag=BornToShine&region=1",
          "ngs_id": "5c45fc5ac24d530017344575",
          "region": "1",
          "short_battletag": "BornToShine"
      },
      {
          "battletag": "SubZero#1577",
          "blizz_id": 6639996,
          "full_battletag": "SubZero%231577",
          "heroes_profile": "https://www.heroesprofile.com/Profile/?blizz_id=6639996&battletag=SubZero&region=1",
          "ngs_id": "600643909ba413002219850b",            
          "region": "1",
          "short_battletag": "SubZero"
      },
      {
          "battletag": "TheCaptain#12345",
          "blizz_id": 9771889,
          "full_battletag": "TheCaptain%2312345",
          "heroes_profile": "https://www.heroesprofile.com/Profile/?blizz_id=9771889&battletag=TheCaptain&region=1",
          "ngs_id": "60063c8d0b86d200283804a1",
          "region": "1",
          "short_battletag": "TheCaptain"
      },
      {
          "battletag": "Olimebus#1241",
          "blizz_id": 6749724,
          "full_battletag": "Olimebus%231241",
          "heroes_profile": "https://www.heroesprofile.com/Profile/?blizz_id=6749724&battletag=Olimebus&region=1",
          "ngs_id": "60063c689ba41300221984f0",
          "region": "1",
          "short_battletag": "Olimebus"
      },
      {
          "battletag": "FARFANEWGAN#1582",
          "blizz_id": 8155713,
          "full_battletag": "FARFANEWGAN%231582",
          "heroes_profile": "https://www.heroesprofile.com/Profile/?blizz_id=8155713&battletag=FARFANEWGAN&region=1",
          "ngs_id": "6007b190209f6c00230554cd",
          "region": "1",
          "short_battletag": "FARFANEWGAN"
      },
      {
          "battletag": "Leinad#1643",
          "blizz_id": 741150,
          "full_battletag": "Leinad%231643",
          "heroes_profile": "https://www.heroesprofile.com/Profile/?blizz_id=741150&battletag=Leinad&region=1",
          "ngs_id": "60b77a33fa300e0022e3669b",
          "region": "1",
          "short_battletag": "Leinad"
      },
      {
          "battletag": "Yotaru#1506",
          "blizz_id": 4510293,
          "full_battletag": "Yotaru%231506",
          "heroes_profile": "https://www.heroesprofile.com/Profile/?blizz_id=4510293&battletag=Yotaru&region=1",
          "ngs_id": "60b7e186fa300e0022e3673c",
          "region": "1",
          "short_battletag": "Yotaru"
      },
      {
          "battletag": "Knivers#1675",
          "blizz_id": 9772524,
          "full_battletag": "Knivers%231675",
          "heroes_profile": "https://www.heroesprofile.com/Profile/?blizz_id=9772524&battletag=Knivers&region=1",
          "ngs_id": "60f6cea674fe45001eccdbee",
          "region": "1",
          "short_battletag": "Knivers"
      }
  ],
  "team_mmr_avg": "",
  "team_name": "30 Seconds to Mosh",
  "team_name_lower": "30 seconds to mosh",
  "ticker": "TSTM",
  "ticker_lower": "tstm"
}

def get_dict_keys(dict):

  result = [d for d in dict]

  return result 


def get_dict_keys_and_values(dict):

  result = [ "Key: {0} - Value: {1} ".format(k, v) for (k,v) in dict.items()]

  return result 


def get_dict_key_value(dict, key):

  result = [ "Key: {0} - Value: {1} ".format(k, v) for (k,v) in dict.items() if k == key]

  return result 


def get_dict_of_keys_and_values(dict):

  result = { k:v for (k,v) in dict.items() }

  return result 


def load_dict_and_get_keys(path):

  with open(path, 'r', encoding='utf-8') as file:
    dict = json.load(file)

  result = [d for d in dict]

  return result
