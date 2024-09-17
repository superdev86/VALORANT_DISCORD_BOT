import requests

# Valid regions and platforms from API
VALID_REGIONS = ['ap', 'br', 'eu', 'kr', 'latam', 'na']
VALID_PLATFORMS = ['pc', 'console']


def get_ranked_stats_response(region, platform, name, tag, api_key):
    try:
        response = requests.get(
            f"https://api.henrikdev.xyz/valorant/v2/mmr/{region}/{name}/{tag}",
            headers={
                "Authorization": api_key
            },
        )
        response.raise_for_status()  # raise an exception for bad status codes
    except Exception as e:
        return f"Error: {e}"

    # Check if region and platform are valid
    if region not in VALID_REGIONS:
        return f"Invalid region. Choose from: {', '.join(VALID_REGIONS)}."
    if platform not in VALID_PLATFORMS:
        return f"Invalid platform. Choose from: {', '.join(VALID_PLATFORMS)}."

    # metadata from the api is saved to data
    data = response.json()

    cur_rank = data["data"]["current_data"].get("currenttierpatched", "Unknown")  # gets current rank
    highest_rank = data["data"]["highest_rank"].get("patched_tier", "Unknown")  # gets highest rank
    highest_rank_szn = data["data"]["highest_rank"].get("season", "Unknown")  # gets the season highest rank was hit
    cur_elo = data["data"]["current_data"].get("elo", "Unknown")  # gets current elo

    # Format the output
    output = (f"**{name}**'s Ranked Stats:\n"
              f"Current Elo: {cur_elo}\n"
              f"Current Rank: {cur_rank}\n"
              f"Peak Rank: {highest_rank} in {highest_rank_szn}\n")

    return output
