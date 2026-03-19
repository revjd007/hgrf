# 🔐 Discord Verify Bot
This is a bare bones version of my discord verify bot using discord oauth2 to pull members back into a guild if it were to be termed.

# 💬 Features
- Saves the users refresh token to the database
- Gives role upon successful verification
- Ability to pull all verified members back into a new guild or the current guild

# ⛔️ Features I removed from the free version
- Advanced Logging
- VPN Detection & Blocking
- Custom Home/Verified/Error Pages
- Ability to pull back a single user
- Ability to kick members if they don't verify within a set period
- Removal of their verified role if they deauthorize the bot
- If they leave and join back they will get the verified role again (If they have not deauthorized the bot)

If you are interested in any of the features that are not provided in the free version feel free to contact me [here](https://discord.com/users/1133030912397938820).

You can checkout the non-free version here: https://verify.koma4k.xyz/

# 📥 Installation & Usage

## Local Development
- Make sure to have [Python](https://python.org) installed
- Open command prompt and cd to the directory
- Run `setup.bat` or `py/python -m pip install -r requirements.txt` (Installs all required packages)
- Fill in all the empty fields in `config.py`
- Run `start.bat` or `py/python app.py` (Starts the bot and webserver)
- Once the bot & webserver are running, run `/setup` in your servers verify channel

## Vercel Deployment
1. **Push to GitHub**
   - Create a new repository on GitHub
   - Push this code to your GitHub repository

2. **Deploy to Vercel**
   - Go to [vercel.com](https://vercel.com) and sign up
   - Click "Add New..." → "Project"
   - Import your GitHub repository
   - Vercel will automatically detect it's a Python project

3. **Configure Environment Variables**
   In your Vercel project settings, add these environment variables:
   - `DISCORD_BOT_TOKEN` - Your Discord bot token
   - `RECOVER_KEY` - Password for /restore command
   - `GUILD_ID` - Your Discord server ID
   - `ROLE_ID` - The verified role ID
   - `CLIENT_ID` - Discord application client ID
   - `CLIENT_SECRET` - Discord application client secret
   - `BASE_URL` - Your Vercel deployment URL (e.g., https://your-app.vercel.app)

4. **Update Discord Developer Portal**
   - In your Discord application's OAuth2 settings, add your Vercel URL + `/callback` as a redirect URI
   - Example: `https://your-app.vercel.app/callback`

5. **Deploy**
   - Click "Deploy" and wait for the deployment to complete
   - Your bot will be available at your Vercel URL

**Note**: The Discord bot component runs separately from the web component. You'll need to run the bot locally or host it on a service that supports long-running processes like Replit, Railway, or a VPS.

![FOR ANALYTICAL PURPOSES ONLY](https://tracker.koma4k.xyz/telemetry/clxvkjisb0001xmjnf0eakp35/clxwk4f9i002zryrgzqevn3si.gif)
