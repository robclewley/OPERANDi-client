# OPERANDi-client

This demo code supports advanced gameplay for OPERANDi (https://transient-dynamic.itch.io/operandi).

Progress in the game will depend on using the API to control game systems and submit puzzle answers from your web browser or via script automations. The game's local HTTP server can be activated from the pause menu. Once active, you can check it at `http://localhost:50505/status` in your browser (or any computer on your LAN).

The python code here is intended to be run interactively, e.g. in ipython or Jupyter, not as a module script run directly by python (because the async `await` won't work outside of a function call in a regular script). It is meant to provide ideas about how to use the game's local HTTP server.

See https://us-pycon-2019-tutorial.readthedocs.io/aiohttp_client_full.html#full-client
for more ideas.
