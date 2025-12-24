# Claude-Ableton Bridge - Ableton Live Setup Guide

Complete guide for connecting Ableton Live to the Claude-Ableton Bridge.

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Architecture](#architecture)
4. [Setup Option 1: Max for Live](#option-1-max-for-live)
5. [Setup Option 2: Max/MSP Runtime](#option-2-maxmsp-runtime)
6. [Setup Option 3: Python Scripts](#option-3-python-scripts)
7. [Testing the Connection](#testing-the-connection)
8. [OSC Endpoint Reference](#osc-endpoint-reference)
9. [Troubleshooting](#troubleshooting)

---

## Overview

The Claude-Ableton Bridge is a Go server that communicates with LLMs (Claude, OpenAI, Ollama) and provides musical responses via OSC (Open Sound Control). Since Ableton Live doesn't have native OSC support, you need an intermediary to handle the communication.

**Bridge Configuration (from config.json):**
- **Receive Port:** 7400 (Ableton sends here)
- **Send Port:** 7401 (Bridge sends responses here)
- **Host:** 127.0.0.1 (localhost)

---

## Prerequisites

1. **Go Bridge Running:**
   ```bash
   cd claude-ableton-bridge
   go run main.go
   ```

2. **Valid API Configuration:** Ensure your `config.json` has a valid API key.

---

## Architecture

```
┌─────────────┐         ┌──────────────┐         ┌──────────┐
│ Ableton Live│ ← OSC →│ Intermediary│ ← OSC →│   Go     │
│             │         │ (Max/Python)│         │ Bridge  │
└─────────────┘         └──────────────┘         └────┬─────┘
                                                        │
                                                        ↓
                                                  ┌──────────┐
                                                  │   LLM    │
                                                  │  API     │
                                                  └──────────┘
```

---

## Option 1: Max for Live

**Best for:** Seamless integration within Ableton Live (requires Ableton Suite)

### Installation

1. **Copy the Device:**
   - Locate `max-for-live/ClaudeBridge.maxpat`
   - Copy to your Ableton User Library:
     - Windows: `Documents/Ableton/User Library/Presets/Audio Effects/Max Audio Effect`
     - Mac: `~/Music/Ableton/User Library/Presets/Audio Effects/Max Audio Effect`

2. **In Ableton Live:**
   - Open Ableton Live
   - Go to the Browser panel
   - Navigate to **Audio Effects** → **Max Audio Effect** (or **MIDI Effects** → **Max MIDI Effect**)
   - Drag **ClaudeBridge** onto a track

### Using the Device

1. **Start the Bridge First:**
   ```bash
   cd claude-ableton-bridge
   go run main.go
   ```

2. **In the Device:**
   - The device automatically connects to `127.0.0.1:7400`
   - Green indicator shows connection status
   - Type prompts in the text box
   - Click **Send** to transmit

3. **Recording MIDI Output:**
   - Create a MIDI track
   - Set input to "ClaudeBridge"
   - Arm track for recording
   - Press record in Ableton

---

## Option 2: Max/MSP Runtime

**Best for:** Testing and development without Ableton Suite

### Installation

1. **Download Max/MSP Runtime (Free):**
   - Visit: https://cycling74.com/downloads/
   - Download "Max Runtime" (no license needed)

2. **Open the Patch:**
   - Open `max-for-live/ClaudeBridge.maxpat` in Max Runtime
   - The patch will load with a GUI

### Using the Patch

Same as Max for Live (see above). The patch works independently of Ableton and can send MIDI to any DAW via virtual MIDI ports.

---

## Option 3: Python Scripts

**Best for:** Testing, automation, custom integrations

### Installation

```bash
cd claude-ableton-bridge/python
pip install -r requirements.txt
```

### Running the Test Client

**Interactive Mode:**
```bash
python test_osc.py
```

**Send Single Prompt:**
```bash
python test_osc.py --prompt "Generate a jazz chord progression"
```

**Run Automated Tests:**
```bash
python test_osc.py --test
```

### Listening for Responses

In a separate terminal:
```bash
python osc_receiver.py
```

This displays all OSC messages sent by the bridge.

---

## Testing the Connection

### Step 1: Start the Bridge

```bash
cd claude-ableton-bridge
go run main.go
```

Expected output:
```
Claude-Ableton Bridge
====================
Configuration loaded successfully
API Provider: openai
Model: meta-llama-3.1-8b-instruct
Cache: true

✓ Bridge running
  Listening on port 7400
  Sending to port 7401
  Press Ctrl+C to exit
```

### Step 2: Test with Python

```bash
# Terminal 1: Start the receiver to see responses
python osc_receiver.py

# Terminal 2: Send test messages
python test_osc.py --test
```

### Step 3: Test with Max

1. Open `ClaudeBridge.maxpat`
2. Type "Hello!" in the prompt box
3. Click Send
4. Check the Max console for responses

---

## OSC Endpoint Reference

The bridge accepts these OSC messages:

| Endpoint | Parameters | Description |
|----------|-----------|-------------|
| `/claude/prompt` | `prompt` (string), `context` (string) | General prompt to LLM |
| `/claude/midi` | `prompt` (string) | Generate MIDI data |
| `/claude/chord` | `prompt` (string) | Generate chord progression |
| `/claude/drums` | `prompt` (string) | Generate drum pattern |
| `/claude/melody` | `prompt` (string) | Generate melody |
| `/claude/effects` | `prompt` (string) | Get effects suggestions |
| `/claude/context` | - | Request session context (not implemented) |
| `/claude/ping` | - | Health check |

### Response Addresses

| Address | Description |
|---------|-------------|
| `/claude/response` | General text response |
| `/claude/error` | Error messages |
| `/claude/midi/data` | MIDI data (JSON) |
| `/claude/chord/data` | Chord data (JSON) |
| `/claude/drums/data` | Drum data (JSON) |
| `/claude/melody/data` | Melody data (JSON) |
| `/claude/pong` | Response to ping |

---

## Troubleshooting

### Problem: "Connection refused"

**Cause:** Bridge is not running.

**Solution:**
```bash
cd claude-ableton-bridge
go run main.go
```

### Problem: No responses in Max

**Causes:**
1. Wrong ports in Max patch
2. Firewall blocking UDP
3. Bridge crashed

**Solutions:**
1. Check Max patch uses ports 7400 (send) and 7401 (receive)
2. Disable firewall temporarily to test
3. Check bridge console for errors

### Problem: API errors in bridge logs

**Cause:** Invalid API key or configuration.

**Solution:**
- Check `config.json` has correct API key
- Verify `api_provider` matches your key type
- Test API key directly:

```bash
curl https://chat-ai.academiccloud.de/v1/models \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Problem: MIDI not appearing in Ableton

**Cause:** MIDI routing not configured.

**Solution:**
1. In Ableton, ensure track MIDI input is set to receive from the Max device
2. Arm the track for recording
3. Check Max device has a `midiout` object connected

### Problem: Port already in use

**Cause:** Another process is using the port.

**Solution:**
```bash
# Find process using port (Windows)
netstat -ano | findstr :7400

# Kill the process (replace PID)
taskkill /PID <PID> /F

# Or change ports in config.json
```

---

## Advanced: Sending Raw OSC Messages

### Using Python

```python
from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 7400)

# Send prompt
client.send_message("/claude/prompt", ["Create a funky bassline", "music"])

# Request MIDI
client.send_message("/claude/midi", ["Simple C major arpeggio"])
```

### Using cURL (via OSC-to-HTTP bridge)

Requires an additional tool. Not recommended for production use.

---

## Example Workflow

1. **Start Bridge:**
   ```bash
   go run main.go
   ```

2. **Open Ableton Live**

3. **Load ClaudeBridge Device** onto a MIDI track

4. **Arm Track for Recording**

5. **Send Prompt:**
   ```
   "Create a jazzy ii-V-I chord progression in C major,
   2 bars per chord, middle C octave range"
   ```

6. **Receive MIDI** appears in Ableton's piano roll

---

## Next Steps

- Customize the Max patch for your workflow
- Build custom presets for different music genres
- Integrate with other Max for Live devices
- Create MIDI effect chains for post-processing

---

## File Locations

| File | Purpose |
|------|---------|
| `max-for-live/ClaudeBridge.maxpat` | Max/MSP patch |
| `python/test_osc.py` | Test client |
| `python/osc_receiver.py` | OSC listener |
| `python/requirements.txt` | Python dependencies |
| `config.json` | Bridge configuration |

---

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the bridge logs: `claude-bridge.log`
3. Test with Python scripts first to isolate the issue
