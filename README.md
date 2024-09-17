# VALORANT_DISCORD_BOT
This bot allows users to fetch Valorant ranked stats by providing their in-game name, region, and platform in a Discord chat. It interacts with the HenrikDev API to retrieve the current rank, Elo, and peak rank of the provided account.

## Features
- Fetch current rank and Elo for a Valorant player.
- Retrieve highest rank achieved in a season.
- Supports multiple regions and platforms.

## Installation

1. Clone the repository to your local machine:
   
   ```bash
   git clone https://github.com/superdev86/VALORANT_DISCORD_BOT.git

2. Clone the repository to your local machine:
   
   ```bash
   cd VALORANT_DISCORD_BOT
   ```
3. Clone the repository to your local machine:
   
   **On Windows:**
   ```bash
   cd VALORANT_DISCORD_BOT
   ```
    **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Create a .env file in the root of your project and add the following environment variables:
   ```
   DISCORD_TOKEN=your_discord_bot_token
   VAL_API_KEY=your_valorant_api_key
   ```
   - Replace your_discord_bot_token with your Discord bot token.
   - Replace your_valorant_api_key with your Valorant API key.

## Setup

1. **Create a Discord Bot**:
   
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.
   - Under the "Bot" tab, click "Add Bot" and copy the bot token.
   - Paste this token in the `.env` file under `DISCORD_TOKEN`.

2. **Get a Valorant API Key**:
   
   - You can retrieve your Valorant API key from the [Henrikdev API](https://docs.henrikdev.xyz/) *(you will need to join the discord to generate an api key)*.
   - Once you have the key, paste it into the `.env` file under `VAL_API_KEY`.

3. **Run the Bot**:
   
   - After setting up the `.env` file and installing dependencies, run the bot using:

     ```bash
     python main.py
     ```

4. **Invite the Bot to Your Server**:

   - Go back to the Discord Developer Portal, and under your application, find the OAuth2 tab.
   - Select "bot" under OAuth2 scopes, then select the necessary bot permissions (such as "Send Messages").
   - Copy the generated OAuth2 URL and open it in a new browser tab to invite your bot to your Discord server.

## Usage
**Commands:**
`/rankedstats <region> <platform> <name>#<tag>`

Fetches ranked stats for the given user.

- **region**: Region where the player is located. Valid options are `ap`, `br`, `eu`, `kr`, `latam`, `na`.
- **platform**: Platform the player uses. Valid options are `pc` or `console`.
- **name#tag**: The in-game name and tag in the format `name#tag`.

### Command Example:
```bash
/rankedstats na pc myname#1234

