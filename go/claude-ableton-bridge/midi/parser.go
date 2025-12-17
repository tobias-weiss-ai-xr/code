package midi

import (
	"encoding/json"
	"fmt"
	"regexp"
	"strings"
)

type Note struct {
	Note     int `json:"note"`
	Velocity int `json:"velocity"`
	Duration int `json:"duration"` // milliseconds
	Time     int `json:"time"`     // milliseconds from start
}

type Chord struct {
	Name     string `json:"name"`
	Notes    []int  `json:"notes"`
	Duration int    `json:"duration"`
}

type Data struct {
	Notes   []Note  `json:"notes,omitempty"`
	Chord   []int   `json:"chord,omitempty"`
	Chords  []Chord `json:"chords,omitempty"`
	Pattern []Note  `json:"pattern,omitempty"`
	Melody  *Melody `json:"melody,omitempty"`
	Tempo   float64 `json:"tempo,omitempty"`
	Key     string  `json:"key,omitempty"`
}

type Melody struct {
	Key   string `json:"key"`
	Scale string `json:"scale"`
	Notes []Note `json:"notes"`
}

type EffectParams struct {
	Effect     string                 `json:"effect"`
	Parameters map[string]interface{} `json:"parameters"`
}

// ParseClaudeResponse extracts and parses JSON from Claude's response
func ParseClaudeResponse(response string) (*Data, error) {
	jsonStr := extractJSON(response)
	if jsonStr == "" {
		return nil, fmt.Errorf("no JSON found in response")
	}

	var data Data
	if err := json.Unmarshal([]byte(jsonStr), &data); err != nil {
		return nil, fmt.Errorf("failed to parse JSON: %w\nJSON was: %s", err, jsonStr)
	}

	if err := data.Validate(); err != nil {
		return nil, fmt.Errorf("invalid MIDI data: %w", err)
	}

	return &data, nil
}

// ParseEffectParams extracts effect parameters from Claude's response
func ParseEffectParams(response string) (*EffectParams, error) {
	jsonStr := extractJSON(response)
	if jsonStr == "" {
		return nil, fmt.Errorf("no JSON found in response")
	}

	var params EffectParams
	if err := json.Unmarshal([]byte(jsonStr), &params); err != nil {
		return nil, fmt.Errorf("failed to parse effect parameters: %w", err)
	}

	return &params, nil
}

// extractJSON finds and extracts JSON from text that may contain other content
func extractJSON(text string) string {
	// Remove markdown code blocks
	text = strings.ReplaceAll(text, "```json", "")
	text = strings.ReplaceAll(text, "```", "")
	text = strings.TrimSpace(text)

	// Try to find JSON object
	re := regexp.MustCompile(`\{(?:[^\{\}]|\{(?:[^\{\}]|\{[^\{\}]*\})*\})*\}`)
	matches := re.FindAllString(text, -1)

	if len(matches) == 0 {
		return ""
	}

	// Return the longest match (most likely to be complete)
	longest := ""
	for _, match := range matches {
		if len(match) > len(longest) {
			longest = match
		}
	}

	return longest
}

// Validate checks if MIDI data is valid
func (d *Data) Validate() error {
	// Validate notes
	for i, note := range d.Notes {
		if err := validateNote(note, i); err != nil {
			return err
		}
	}

	// Validate chord notes
	for i, note := range d.Chord {
		if note < 0 || note > 127 {
			return fmt.Errorf("chord note %d: invalid note number %d (must be 0-127)", i, note)
		}
	}

	// Validate pattern notes
	for i, note := range d.Pattern {
		if err := validateNote(note, i); err != nil {
			return err
		}
	}

	// Validate melody notes
	if d.Melody != nil {
		for i, note := range d.Melody.Notes {
			if err := validateNote(note, i); err != nil {
				return err
			}
		}
	}

	// Validate chords structure
	for i, chord := range d.Chords {
		for j, note := range chord.Notes {
			if note < 0 || note > 127 {
				return fmt.Errorf("chord %d, note %d: invalid note number %d", i, j, note)
			}
		}
		if chord.Duration < 0 {
			return fmt.Errorf("chord %d: invalid duration %d", i, chord.Duration)
		}
	}

	return nil
}

func validateNote(note Note, index int) error {
	if note.Note < 0 || note.Note > 127 {
		return fmt.Errorf("note %d: invalid note number %d (must be 0-127)", index, note.Note)
	}
	if note.Velocity < 0 || note.Velocity > 127 {
		return fmt.Errorf("note %d: invalid velocity %d (must be 0-127)", index, note.Velocity)
	}
	if note.Duration < 0 {
		return fmt.Errorf("note %d: invalid duration %d (must be >= 0)", index, note.Duration)
	}
	if note.Time < 0 {
		return fmt.Errorf("note %d: invalid time %d (must be >= 0)", index, note.Time)
	}
	return nil
}

// ToJSON converts data to formatted JSON
func (d *Data) ToJSON() ([]byte, error) {
	return json.MarshalIndent(d, "", "  ")
}

// ConvertToMIDIMessages converts Data to individual MIDI messages for Max
func (d *Data) ConvertToMIDIMessages() []MIDIMessage {
	var messages []MIDIMessage

	// Handle individual notes
	for _, note := range d.Notes {
		messages = append(messages, MIDIMessage{
			Type:     "note",
			Note:     note.Note,
			Velocity: note.Velocity,
			Duration: note.Duration,
			Time:     note.Time,
		})
	}

	// Handle simple chord (all notes at once)
	for _, note := range d.Chord {
		messages = append(messages, MIDIMessage{
			Type:     "note",
			Note:     note,
			Velocity: 80,
			Duration: 1000,
			Time:     0,
		})
	}

	// Handle chord progression
	currentTime := 0
	for _, chord := range d.Chords {
		for _, note := range chord.Notes {
			messages = append(messages, MIDIMessage{
				Type:     "note",
				Note:     note,
				Velocity: 80,
				Duration: chord.Duration,
				Time:     currentTime,
			})
		}
		currentTime += chord.Duration
	}

	// Handle pattern
	for _, note := range d.Pattern {
		messages = append(messages, MIDIMessage{
			Type:     "note",
			Note:     note.Note,
			Velocity: note.Velocity,
			Duration: note.Duration,
			Time:     note.Time,
		})
	}

	// Handle melody
	if d.Melody != nil {
		for _, note := range d.Melody.Notes {
			messages = append(messages, MIDIMessage{
				Type:     "note",
				Note:     note.Note,
				Velocity: note.Velocity,
				Duration: note.Duration,
				Time:     note.Time,
			})
		}
	}

	return messages
}

type MIDIMessage struct {
	Type     string `json:"type"`
	Note     int    `json:"note"`
	Velocity int    `json:"velocity"`
	Duration int    `json:"duration"`
	Time     int    `json:"time"`
}
