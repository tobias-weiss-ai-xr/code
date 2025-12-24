# SAIA AI Integration Guide

This guide explains how to use the Claude-Ableton Bridge with [SAIA AI](https://docs.hpc.gwdg.de/services/saia/index.html) from the HPC center at GWDG.

## What is SAIA?

SAIA (Scalable AI Accelerator) is a service that provides free access to various LLM models through an OpenAI-compatible API. It's hosted by the GWZ German HPC center.

## Getting a SAIA API Key

1. Visit the [KISSKI LLM Service page](https://kisski.lmz.uni-freiburg.de/)
2. Click "Book" to request an API key
3. Fill out the form with your Academic Cloud credentials
4. You'll receive your API key via email

## Configuration

### Quick Setup

1. Copy `config.saia.json` to `config.json`:
```bash
cp config.saia.json config.json
```

2. Edit `config.json` and replace `YOUR_SAIA_API_KEY_HERE` with your actual API key

3. Run the bridge:
```bash
./claude-bridge.exe
```

### Manual Configuration

Alternatively, edit your `config.json` manually:

```json
{
  "api_provider": "openai",
  "openai_api_key": "your-saia-api-key",
  "openai_base_url": "https://chat-ai.academiccloud.de/v1",
  "claude_model": "meta-llama-3.1-8b-instruct",
  "osc_receive_port": 7400,
  "osc_send_port": 7401,
  "osc_host": "127.0.0.1",
  "max_tokens": 2000,
  "enable_cache": true,
  "cache_ttl_seconds": 300
}
```

## Available SAIA Models

### Recommended for Music/MIDI Generation

| Model | Description | Speed | Use Case |
|-------|-------------|-------|----------|
| `meta-llama-3.1-8b-instruct` | Llama 3.1 8B | Fast | Default choice for MIDI generation |
| `llama-3.3-70b-instruct` | Llama 3.3 70B | Medium | More creative melodies |
| `mistral-large-instruct` | Mistral Large | Medium | High-quality compositions |
| `gemma-3-27b-it` | Gemma 3 27B | Fast | Quick responses |

### Reasoning Models (Slower but More Thoughtful)

| Model | Description | Use Case |
|-------|-------------|----------|
| `qwen3-235b-a22b` | Qwen 235B | Complex musical theory |
| `qwq-32b` | QWQ 32B | Mathematical patterns |
| `deepseek-r1` | DeepSeek R1 | Deep reasoning |

### Code/Structured Output Models

| Model | Description | Use Case |
|-------|-------------|----------|
| `qwen2.5-coder-32b-instruct` | Qwen Coder 32B | Better JSON formatting |
| `codestral-22b` | Codestral 22B | Precise MIDI structures |

### Multimodal Models

| Model | Description | Capabilities |
|-------|-------------|--------------|
| `gemma-3-27b-it` | Gemma 3 | Text + Image |
| `internvl2.5-8b` | InternVL 2.5 | Text + Image |
| `qwen2.5-vl-72b-instruct` | Qwen VL 72B | Text + Image |

### RAG/Arcana Models

| Model | Description | Use Case |
|-------|-------------|----------|
| `meta-llama-3.1-8b-rag` | Llama 3.1 RAG | With knowledge retrieval |

## Usage Examples

### Generate MIDI with SAIA

```
OSC Address: /claude/midi
Arguments: "Create a jazz melody in C minor with syncopation"
```

### Generate Chords with SAIA

```
OSC Address: /claude/chord
Arguments: "Create a sophisticated chord progression with extended voicings"
```

### Get Production Advice

```
OSC Address: /claude/prompt
Arguments: "How do I create sidechain compression in Ableton Live?"
```

## Testing SAIA Connection

### Using curl

```bash
curl -X POST "https://chat-ai.academiccloud.de/v1/chat/completions" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama-3.1-8b-instruct",
    "messages": [{"role": "user", "content": "Say hello"}],
    "max_tokens": 10
  }'
```

### Using Python

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-saia-api-key",
    base_url="https://chat-ai.academiccloud.de/v1"
)

response = client.chat.completions.create(
    model="meta-llama-3.1-8b-instruct",
    messages=[{"role": "user", "content": "Generate a C major scale in JSON format"}]
)

print(response.choices[0].message.content)
```

## Advantages of SAIA

- **Free** - No cost for academic users
- **Many Models** - Access to 20+ different LLMs
- **OpenAI Compatible** - Works with existing OpenAI clients
- **Hosted in Europe** - GDPR compliant
- **No Rate Limits** - Generous usage limits

## Switching Between Models

To change models, simply update the `claude_model` field in your `config.json`:

```json
{
  "claude_model": "llama-3.3-70b-instruct"
}
```

Then restart the bridge:
```bash
# Press Ctrl+C to stop
./claude-bridge.exe
```

## Troubleshooting

### API Key Not Working

- Ensure you requested the key from the KISSKI portal
- Check that the email matches your Academic Cloud account
- Verify the key doesn't have extra spaces

### Connection Errors

- Check your internet connection
- Verify the base URL is correct: `https://chat-ai.academiccloud.de/v1`
- Check the bridge logs: `claude-bridge.log`

### Model Not Found

- Verify the model name is spelled correctly
- Check the [SAIA model list](https://docs.hpc.gwdg.de/services/saia/index.html) for available models
- Some models may be temporarily unavailable

### Poor MIDI Generation

- Try a larger model (e.g., `llama-3.3-70b-instruct`)
- Increase `max_tokens` in config
- Use more specific prompts
- Try the `qwen2.5-coder-32b-instruct` model for better JSON formatting

## List All Available Models

To get a current list of all available SAIA models:

```bash
curl -X POST "https://chat-ai.academiccloud.de/v1/models" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

## More Information

- [SAIA Documentation](https://docs.hpc.gwdg.de/services/saia/index.html)
- [HPC Support](mailto:support@gwdg.de)
- [Academic Cloud](https://academiccloud.de/)
