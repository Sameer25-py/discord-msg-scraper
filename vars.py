vars = {
    "auth_token" : "", #<- auth token goes here 
    "discord_api": "https://discord.com/api/v9",
    "channels":  lambda x : f"/channels/{x}", #x = channel id 
    "guilds" : lambda x : f"/guilds/{x}", #x = guild/server id
    "messages": "/messages", 
    "limit" : lambda x: f"?limit={x}"
}
