"""This example demonstrates a basic API usage"""

from pyrogram import Client

# Create a new Client instance
app = Client("my_account",
             api_id=54084,
             api_hash="bfa60fd6ae1a475b3cc3704d4c8f77af")

with app:
    # Send a message, Markdown is enabled by default
    app.send_message(481354245, "Hi there! I'm using **Pyrogram**")

    # Send a location
    app.send_location(481354245, 51.500729, -0.124583)

    # Send a sticker
    app.send_sticker(481354245, "CAADBAADyg4AAvLQYAEYD4F7vcZ43AI")
