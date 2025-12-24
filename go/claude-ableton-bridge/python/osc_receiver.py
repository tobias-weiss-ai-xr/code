"""
OSC Message Receiver for Claude-Ableton Bridge

This script listens for OSC messages from the bridge and displays them.
Useful for debugging and seeing the bridge responses.

Requirements:
    pip install python-osc

Usage:
    python osc_receiver.py
"""

import argparse
from pythonosc import osc_server
from pythonosc.dispatcher import Dispatcher


def create_receiver(port=7401):
    """Create and start an OSC receiver server."""

    dispatcher = Dispatcher()

    # Handler for general responses
    def handle_response(address, *args):
        print(f"\n[RESPONSE] {args[0] if args else ''}")

    # Handler for errors
    def handle_error(address, *args):
        print(f"\n[ERROR] {args[0] if args else 'Unknown error'}")

    # Handler for MIDI data
    def handle_midi_data(address, *args):
        print(f"\n[MIDI DATA] {args[0] if args else ''}")

    # Handler for chord data
    def handle_chord_data(address, *args):
        print(f"\n[CHORD DATA] {args[0] if args else ''}")

    # Handler for drums data
    def handle_drums_data(address, *args):
        print(f"\n[DRUMS DATA] {args[0] if args else ''}")

    # Handler for melody data
    def handle_melody_data(address, *args):
        print(f"\n[MELODY DATA] {args[0] if args else ''}")

    # Handler for pong
    def handle_pong(address, *args):
        print(f"\n[PONG] Bridge is alive! {args[0] if args else ''}")

    # Register handlers
    dispatcher.map("/claude/response", handle_response)
    dispatcher.map("/claude/error", handle_error)
    dispatcher.map("/claude/midi/data", handle_midi_data)
    dispatcher.map("/claude/chord/data", handle_chord_data)
    dispatcher.map("/claude/drums/data", handle_drums_data)
    dispatcher.map("/claude/melody/data", handle_melody_data)
    dispatcher.map("/claude/pong", handle_pong)

    # Default handler for any unmatched message
    def default_handler(address, *args):
        print(f"\n[UNKNOWN] {address}: {args}")

    dispatcher.set_default_handler(default_handler)

    # Create and start server
    server = osc_server.ThreadingOSCUDPServer(
        (args.host if 'args' in dir() and hasattr(args, 'host') else "127.0.0.1", port),
        dispatcher
    )

    return server


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="OSC Receiver for Claude-Ableton Bridge"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=7401,
        help="Port to listen on (default: 7401)"
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host to bind to (default: 127.0.0.1)"
    )

    global args
    args = parser.parse_args()

    print(f"Listening for OSC messages on {args.host}:{args.port}")
    print("Press Ctrl+C to stop\n")

    server = create_receiver(args.port)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
