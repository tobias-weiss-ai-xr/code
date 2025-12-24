package midi

import (
	"strings"
	"testing"
)

// Test ParseClaudeResponse with valid JSON formats
func TestParseClaudeResponse(t *testing.T) {
	t.Run("Valid notes JSON", func(t *testing.T) {
		jsonResponse := `{"notes": [{"note": 60, "velocity": 100, "duration": 500, "time": 0}]}`
		data, err := ParseClaudeResponse(jsonResponse)
		if err != nil {
			t.Fatalf("ParseClaudeResponse failed: %v", err)
		}
		if len(data.Notes) != 1 {
			t.Errorf("Expected 1 note, got %d", len(data.Notes))
		}
		if data.Notes[0].Note != 60 || data.Notes[0].Velocity != 100 {
			t.Errorf("Note data mismatch: %+v", data.Notes[0])
		}
	})

	t.Run("Valid chord JSON", func(t *testing.T) {
		jsonResponse := `{"chord": [60, 64, 67]}`
		data, err := ParseClaudeResponse(jsonResponse)
		if err != nil {
			t.Fatalf("ParseClaudeResponse failed: %v", err)
		}
		if len(data.Chord) != 3 {
			t.Errorf("Expected 3 chord notes, got %d", len(data.Chord))
		}
	})

	t.Run("Valid melody JSON", func(t *testing.T) {
		jsonResponse := `{
			"melody": {
				"key": "C",
				"scale": "major",
				"notes": [
					{"note": 60, "velocity": 100, "duration": 500, "time": 0},
					{"note": 64, "velocity": 90, "duration": 500, "time": 500}
				]
			}
		}`
		data, err := ParseClaudeResponse(jsonResponse)
		if err != nil {
			t.Fatalf("ParseClaudeResponse failed: %v", err)
		}
		if data.Melody == nil {
			t.Fatal("Expected melody to be non-nil")
		}
		if data.Melody.Key != "C" || data.Melody.Scale != "major" {
			t.Errorf("Melody key/scale mismatch: %+v", data.Melody)
		}
		if len(data.Melody.Notes) != 2 {
			t.Errorf("Expected 2 melody notes, got %d", len(data.Melody.Notes))
		}
	})

	t.Run("Valid chords (progression) JSON", func(t *testing.T) {
		jsonResponse := `{
			"chords": [
				{"name": "C", "notes": [60, 64, 67], "duration": 1000},
				{"name": "G", "notes": [67, 71, 74], "duration": 1000}
			]
		}`
		data, err := ParseClaudeResponse(jsonResponse)
		if err != nil {
			t.Fatalf("ParseClaudeResponse failed: %v", err)
		}
		if len(data.Chords) != 2 {
			t.Errorf("Expected 2 chords, got %d", len(data.Chords))
		}
		if data.Chords[0].Name != "C" {
			t.Errorf("First chord name mismatch: %s", data.Chords[0].Name)
		}
	})

	t.Run("Valid pattern JSON", func(t *testing.T) {
		jsonResponse := `{
			"pattern": [
				{"note": 36, "velocity": 127, "duration": 100, "time": 0},
				{"note": 36, "velocity": 127, "duration": 100, "time": 250}
			]
		}`
		data, err := ParseClaudeResponse(jsonResponse)
		if err != nil {
			t.Fatalf("ParseClaudeResponse failed: %v", err)
		}
		if len(data.Pattern) != 2 {
			t.Errorf("Expected 2 pattern notes, got %d", len(data.Pattern))
		}
	})

	t.Run("Valid tempo and key", func(t *testing.T) {
		jsonResponse := `{"tempo": 120.5, "key": "C minor"}`
		data, err := ParseClaudeResponse(jsonResponse)
		if err != nil {
			t.Fatalf("ParseClaudeResponse failed: %v", err)
		}
		if data.Tempo != 120.5 {
			t.Errorf("Expected tempo 120.5, got %f", data.Tempo)
		}
		if data.Key != "C minor" {
			t.Errorf("Expected key 'C minor', got %s", data.Key)
		}
	})
}

// Test ParseClaudeResponse with invalid JSON
func TestParseClaudeResponse_InvalidJSON(t *testing.T) {
	t.Run("Invalid JSON syntax", func(t *testing.T) {
		invalidJSON := `{"notes": [{"note": 60, "velocity": 100}]]}`
		_, err := ParseClaudeResponse(invalidJSON)
		if err == nil {
			t.Error("Expected error for invalid JSON, got nil")
		}
	})

	t.Run("No JSON found", func(t *testing.T) {
		noJSON := "This is just plain text with no JSON"
		_, err := ParseClaudeResponse(noJSON)
		if err == nil {
			t.Error("Expected error for no JSON, got nil")
		}
		if !strings.Contains(err.Error(), "no JSON found") {
			t.Errorf("Expected 'no JSON found' error, got: %v", err)
		}
	})
}

// Test ParseClaudeResponse with JSON embedded in markdown
func TestParseClaudeResponse_MarkdownEmbedded(t *testing.T) {
	t.Run("JSON in markdown code block", func(t *testing.T) {
		markdownJSON := "```\n{\"notes\": [{\"note\": 60, \"velocity\": 100, \"duration\": 500, \"time\": 0}]}\n```"
		data, err := ParseClaudeResponse(markdownJSON)
		if err != nil {
			t.Fatalf("ParseClaudeResponse with markdown failed: %v", err)
		}
		if len(data.Notes) != 1 {
			t.Errorf("Expected 1 note, got %d", len(data.Notes))
		}
	})

	t.Run("JSON in json-markdown code block", func(t *testing.T) {
		jsonMarkdownJSON := "```json\n{\"chord\": [60, 64, 67]}\n```"
		data, err := ParseClaudeResponse(jsonMarkdownJSON)
		if err != nil {
			t.Fatalf("ParseClaudeResponse with ```json failed: %v", err)
		}
		if len(data.Chord) != 3 {
			t.Errorf("Expected 3 chord notes, got %d", len(data.Chord))
		}
	})

	t.Run("JSON with text before and after", func(t *testing.T) {
		mixedContent := "Here's the response:\n{\"notes\": [{\"note\": 72, \"velocity\": 100, \"duration\": 500, \"time\": 0}]}\nThat's it!"
		data, err := ParseClaudeResponse(mixedContent)
		if err != nil {
			t.Fatalf("ParseClaudeResponse with mixed content failed: %v", err)
		}
		if len(data.Notes) != 1 {
			t.Errorf("Expected 1 note, got %d", len(data.Notes))
		}
		if data.Notes[0].Note != 72 {
			t.Errorf("Expected note 72, got %d", data.Notes[0].Note)
		}
	})
}

// Test ParseEffectParams
func TestParseEffectParams(t *testing.T) {
	t.Run("Valid effect params", func(t *testing.T) {
		effectJSON := `{"effect": "reverb", "parameters": {"room_size": 0.7, "damping": 0.5}}`
		params, err := ParseEffectParams(effectJSON)
		if err != nil {
			t.Fatalf("ParseEffectParams failed: %v", err)
		}
		if params.Effect != "reverb" {
			t.Errorf("Expected effect 'reverb', got %s", params.Effect)
		}
		if params.Parameters == nil {
			t.Fatal("Expected parameters to be non-nil")
		}
		if roomSize, ok := params.Parameters["room_size"]; !ok || roomSize != 0.7 {
			t.Errorf("Expected room_size 0.7, got %v", roomSize)
		}
	})

	t.Run("Effect params in markdown", func(t *testing.T) {
		markdownEffect := "Here are the parameters:\n```json\n{\"effect\": \"delay\", \"parameters\": {\"time\": 0.3, \"feedback\": 0.4}}\n```"
		params, err := ParseEffectParams(markdownEffect)
		if err != nil {
			t.Fatalf("ParseEffectParams with markdown failed: %v", err)
		}
		if params.Effect != "delay" {
			t.Errorf("Expected effect 'delay', got %s", params.Effect)
		}
	})

	t.Run("Invalid effect params JSON", func(t *testing.T) {
		invalidEffect := `{"effect": "reverb", "parameters":`
		_, err := ParseEffectParams(invalidEffect)
		if err == nil {
			t.Error("Expected error for invalid effect params JSON, got nil")
		}
	})

	t.Run("No JSON in effect response", func(t *testing.T) {
		noJSON := "Set the reverb to medium room size"
		_, err := ParseEffectParams(noJSON)
		if err == nil {
			t.Error("Expected error for no JSON, got nil")
		}
	})
}

// Test Data.Validate() for all data types
func TestDataValidate(t *testing.T) {
	t.Run("Valid empty data", func(t *testing.T) {
		data := &Data{}
		if err := data.Validate(); err != nil {
			t.Errorf("Empty data should be valid: %v", err)
		}
	})

	t.Run("Valid notes", func(t *testing.T) {
		data := &Data{
			Notes: []Note{
				{Note: 60, Velocity: 100, Duration: 500, Time: 0},
				{Note: 64, Velocity: 90, Duration: 250, Time: 500},
			},
		}
		if err := data.Validate(); err != nil {
			t.Errorf("Valid notes failed validation: %v", err)
		}
	})

	t.Run("Valid chord", func(t *testing.T) {
		data := &Data{
			Chord: []int{60, 64, 67},
		}
		if err := data.Validate(); err != nil {
			t.Errorf("Valid chord failed validation: %v", err)
		}
	})

	t.Run("Valid chords with duration", func(t *testing.T) {
		data := &Data{
			Chords: []Chord{
				{Name: "C", Notes: []int{60, 64, 67}, Duration: 1000},
				{Name: "G", Notes: []int{67, 71, 74}, Duration: 1000},
			},
		}
		if err := data.Validate(); err != nil {
			t.Errorf("Valid chords failed validation: %v", err)
		}
	})

	t.Run("Valid pattern", func(t *testing.T) {
		data := &Data{
			Pattern: []Note{
				{Note: 36, Velocity: 127, Duration: 100, Time: 0},
			},
		}
		if err := data.Validate(); err != nil {
			t.Errorf("Valid pattern failed validation: %v", err)
		}
	})

	t.Run("Valid melody", func(t *testing.T) {
		data := &Data{
			Melody: &Melody{
				Key:   "C",
				Scale: "major",
				Notes: []Note{
					{Note: 60, Velocity: 100, Duration: 500, Time: 0},
				},
			},
		}
		if err := data.Validate(); err != nil {
			t.Errorf("Valid melody failed validation: %v", err)
		}
	})

	// Invalid cases
	t.Run("Invalid note - note number too high", func(t *testing.T) {
		data := &Data{
			Notes: []Note{
				{Note: 128, Velocity: 100, Duration: 500, Time: 0},
			},
		}
		if err := data.Validate(); err == nil {
			t.Error("Expected validation error for note > 127, got nil")
		}
	})

	t.Run("Invalid note - negative note", func(t *testing.T) {
		data := &Data{
			Notes: []Note{
				{Note: -1, Velocity: 100, Duration: 500, Time: 0},
			},
		}
		if err := data.Validate(); err == nil {
			t.Error("Expected validation error for negative note, got nil")
		}
	})

	t.Run("Invalid note - velocity too high", func(t *testing.T) {
		data := &Data{
			Notes: []Note{
				{Note: 60, Velocity: 128, Duration: 500, Time: 0},
			},
		}
		if err := data.Validate(); err == nil {
			t.Error("Expected validation error for velocity > 127, got nil")
		}
	})

	t.Run("Invalid chord note - out of range", func(t *testing.T) {
		data := &Data{
			Chord: []int{60, 200, 67},
		}
		if err := data.Validate(); err == nil {
			t.Error("Expected validation error for chord note > 127, got nil")
		}
	})
}

// Test ToJSON serialization
func TestToJSON(t *testing.T) {
	t.Run("Serialize notes data", func(t *testing.T) {
		data := &Data{
			Notes: []Note{
				{Note: 60, Velocity: 100, Duration: 500, Time: 0},
			},
		}
		jsonBytes, err := data.ToJSON()
		if err != nil {
			t.Fatalf("ToJSON failed: %v", err)
		}

		if jsonBytes == nil || len(jsonBytes) == 0 {
			t.Error("ToJSON returned empty bytes")
		}
	})

	t.Run("Serialize empty data", func(t *testing.T) {
		data := &Data{}
		jsonBytes, err := data.ToJSON()
		if err != nil {
			t.Fatalf("ToJSON failed for empty data: %v", err)
		}

		if jsonBytes == nil || len(jsonBytes) == 0 {
			t.Error("ToJSON returned empty bytes for empty data")
		}
	})
}

// Test ConvertToMIDIMessages for all formats
func TestConvertToMIDIMessages(t *testing.T) {
	t.Run("Convert notes", func(t *testing.T) {
		data := &Data{
			Notes: []Note{
				{Note: 60, Velocity: 100, Duration: 500, Time: 0},
				{Note: 64, Velocity: 90, Duration: 250, Time: 500},
			},
		}
		messages := data.ConvertToMIDIMessages()

		if len(messages) != 2 {
			t.Fatalf("Expected 2 MIDI messages, got %d", len(messages))
		}
		if messages[0].Type != "note" || messages[0].Note != 60 {
			t.Errorf("First message mismatch: %+v", messages[0])
		}
	})

	t.Run("Convert chord (simple)", func(t *testing.T) {
		data := &Data{
			Chord: []int{60, 64, 67},
		}
		messages := data.ConvertToMIDIMessages()

		if len(messages) != 3 {
			t.Fatalf("Expected 3 MIDI messages, got %d", len(messages))
		}
	})

	t.Run("Convert chord progression", func(t *testing.T) {
		data := &Data{
			Chords: []Chord{
				{Name: "C", Notes: []int{60, 64, 67}, Duration: 1000},
				{Name: "G", Notes: []int{67, 71, 74}, Duration: 1000},
			},
		}
		messages := data.ConvertToMIDIMessages()

		// 3 notes per chord = 6 messages total
		if len(messages) != 6 {
			t.Fatalf("Expected 6 MIDI messages, got %d", len(messages))
		}
	})

	t.Run("Convert pattern", func(t *testing.T) {
		data := &Data{
			Pattern: []Note{
				{Note: 36, Velocity: 127, Duration: 100, Time: 0},
				{Note: 38, Velocity: 100, Duration: 100, Time: 120},
			},
		}
		messages := data.ConvertToMIDIMessages()

		if len(messages) != 2 {
			t.Fatalf("Expected 2 MIDI messages, got %d", len(messages))
		}
	})

	t.Run("Convert melody", func(t *testing.T) {
		data := &Data{
			Melody: &Melody{
				Key:   "C",
				Scale: "major",
				Notes: []Note{
					{Note: 60, Velocity: 100, Duration: 500, Time: 0},
					{Note: 64, Velocity: 90, Duration: 500, Time: 500},
				},
			},
		}
		messages := data.ConvertToMIDIMessages()

		if len(messages) != 2 {
			t.Fatalf("Expected 2 MIDI messages, got %d", len(messages))
		}
	})

	t.Run("Convert empty data", func(t *testing.T) {
		data := &Data{}
		messages := data.ConvertToMIDIMessages()

		if len(messages) != 0 {
			t.Errorf("Expected 0 MIDI messages for empty data, got %d", len(messages))
		}
	})
}
