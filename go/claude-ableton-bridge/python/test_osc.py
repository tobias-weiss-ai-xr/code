"""
Claude-Ableton Bridge Python Test Client

This script sends OSC messages to the Claude-Ableton Bridge server
and can be used to test the connection and functionality.

Requirements:
    pip install python-osc

Usage:
    python test_osc.py
"""

import argparse
import time
from pythonosc import udp_client
from pythonosc import osc_message_builder
from pythonosc import osc_bundle_builder


class ClaudeBridgeClient:
    """Client for communicating with the Claude-Ableton Bridge via OSC."""

    def __init__(self, host="127.0.0.1", send_port=7400, receive_port=7401):
        """
        Initialize the OSC client.

        Args:
            host: Bridge server host (default: 127.0.0.1)
            send_port: Port to send messages TO (bridge's receive port)
            receive_port: Port to receive messages FROM (bridge's send port)
        """
        self.host = host
        self.send_port = send_port
        self.receive_port = receive_port
        self.client = udp_client.SimpleUDPClient(host, send_port)

    def send_prompt(self, prompt, context="music"):
        """Send a general prompt to the bridge."""
        print(f"Sending prompt: {prompt}")
        self.client.send_message("/claude/prompt", [prompt, context])

    def send_midi_request(self, prompt):
        """Request MIDI data generation."""
        print(f"Requesting MIDI: {prompt}")
        self.client.send_message("/claude/midi", [prompt])

    def send_chord_request(self, prompt):
        """Request chord generation."""
        print(f"Requesting chord: {prompt}")
        self.client.send_message("/claude/chord", [prompt])

    def send_drums_request(self, prompt):
        """Request drum pattern generation."""
        print(f"Requesting drums: {prompt}")
        self.client.send_message("/claude/drums", [prompt])

    def send_melody_request(self, prompt):
        """Request melody generation."""
        print(f"Requesting melody: {prompt}")
        self.client.send_message("/claude/melody", [prompt])

    def send_effects_request(self, prompt):
        """Request effects suggestions."""
        print(f"Requesting effects: {prompt}")
        self.client.send_message("/claude/effects", [prompt])

    def send_ping(self):
        """Send a ping to check if bridge is alive."""
        print("Sending ping...")
        self.client.send_message("/claude/ping", [])


def interactive_mode(client):
    """Run the client in interactive mode."""
    print("\n" + "="*50)
    print("Claude-Ableton Bridge - Interactive Test Client")
    print("="*50)
    print("\nAvailable commands:")
    print("  1. prompt      - Send general prompt")
    print("  2. midi        - Request MIDI generation")
    print("  3. chord       - Request chord progression")
    print("  4. drums       - Request drum pattern")
    print("  5. melody      - Request melody generation")
    print("  6. effects     - Request effects suggestions")
    print("  7. ping        - Check if bridge is alive")
    print("  8. quit        - Exit client")
    print("-"*50)

    while True:
        try:
            cmd = input("\n> ").strip().lower()

            if not cmd:
                continue

            if cmd in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            elif cmd == "ping":
                client.send_ping()
                time.sleep(0.5)  # Give time for pong

            elif cmd == "prompt":
                prompt = input("Enter your prompt: ")
                if prompt:
                    context = input("Enter context (default: music): ") or "music"
                    client.send_prompt(prompt, context)

            elif cmd == "midi":
                prompt = input("Describe the MIDI you want: ")
                if prompt:
                    client.send_midi_request(prompt)

            elif cmd == "chord":
                prompt = input("Describe the chord progression: ")
                if prompt:
                    client.send_chord_request(prompt)

            elif cmd == "drums":
                prompt = input("Describe the drum pattern: ")
                if prompt:
                    client.send_drums_request(prompt)

            elif cmd == "melody":
                prompt = input("Describe the melody: ")
                if prompt:
                    client.send_melody_request(prompt)

            elif cmd == "effects":
                prompt = input("Describe the effects you want: ")
                if prompt:
                    client.send_effects_request(prompt)

            else:
                print(f"Unknown command: {cmd}")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


def run_tests(client):
    """Run a series of automated tests."""
    print("\n" + "="*50)
    print("Running Automated Tests")
    print("="*50)

    tests = [
        ("Ping test", lambda: client.send_ping()),
        ("Prompt test", lambda: client.send_prompt("Hello Claude!", "music")),
        ("MIDI test", lambda: client.send_midi_request("Generate a simple C major scale")),
        ("Chord test", lambda: client.send_chord_request("Create a jazz ii-V-I progression")),
        ("Drums test", lambda: client.send_drums_request("Basic rock beat")),
        ("Melody test", lambda: client.send_melody_request("Simple happy melody")),
        ("Effects test", lambda: client.send_effects_request("Reverb for a piano")),
    ]

    for i, (name, test_func) in enumerate(tests, 1):
        print(f"\n{i}. {name}...")
        try:
            test_func()
            time.sleep(1)  # Wait between tests
        except Exception as e:
            print(f"   Failed: {e}")

    print("\n" + "="*50)
    print("Tests complete!")
    print("="*50)


def main():
    parser = argparse.ArgumentParser(
        description="Claude-Ableton Bridge OSC Test Client"
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Bridge server host (default: 127.0.0.1)"
    )
    parser.add_argument(
        "--send-port",
        type=int,
        default=7400,
        help="Port to send messages to (default: 7400)"
    )
    parser.add_argument(
        "--receive-port",
        type=int,
        default=7401,
        help="Port to receive messages from (default: 7401)"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run automated tests"
    )
    parser.add_argument(
        "--prompt",
        type=str,
        help="Send a single prompt"
    )

    args = parser.parse_args()

    # Create client
    client = ClaudeBridgeClient(args.host, args.send_port, args.receive_port)

    print(f"Connected to bridge at {args.host}:{args.send_port}")
    print(f"Listening for responses on port {args.receive_port}")

    # Execute based on arguments
    if args.prompt:
        client.send_prompt(args.prompt)
    elif args.test:
        run_tests(client)
    else:
        interactive_mode(client)


if __name__ == "__main__":
    main()
