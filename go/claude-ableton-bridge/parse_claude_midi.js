// parse_claude_midi.js
// Parses JSON MIDI data from Claude-Ableton Bridge

inlets = 1;
outlets = 4; // note, velocity, duration, timing

var scheduled = [];

function anything() {
    var input = arrayfromargs(arguments);
    var jsonString = input.join(" ");
    
    post("Received: " + jsonString.substring(0, 100) + "...\n");
    
    try {
        var data = JSON.parse(jsonString);
        
        // Clear previous scheduled notes
        clearScheduled();
        
        if (data.notes && Array.isArray(data.notes)) {
            post("Processing " + data.notes.length + " notes\n");
            scheduleNotes(data.notes);
        } 
        else if (data.chord && Array.isArray(data.chord)) {
            post("Processing chord with " + data.chord.length + " notes\n");
            playChord(data.chord);
        }
        else if (data.chords && Array.isArray(data.chords)) {
            post("Processing chord progression\n");
            scheduleChordProgression(data.chords);
        }
        else if (data.pattern && Array.isArray(data.pattern)) {
            post("Processing drum pattern\n");
            scheduleNotes(data.pattern);
        }
        else if (data.melody && data.melody.notes) {
            post("Processing melody\n");
            scheduleNotes(data.melody.notes);
        }
        else {
            post("Unknown MIDI format\n");
        }
        
    } catch (e) {
        post("JSON parse error: " + e + "\n");
    }
}

function scheduleNotes(notes) {
    for (var i = 0; i < notes.length; i++) {
        var note = notes[i];
        var time = note.time || 0;
        
        var task = new Task(playNote, this, note);
        task.schedule(time);
        scheduled.push(task);
    }
}

function playNote(note) {
    outlet(0, note.note || 60);
    outlet(1, note.velocity || 80);
    outlet(2, note.duration || 500);
    outlet(3, 0);
}

function playChord(chord) {
    for (var i = 0; i < chord.length; i++) {
        outlet(0, chord[i]);
        outlet(1, 80);
        outlet(2, 1000);
        outlet(3, 0);
    }
}

function scheduleChordProgression(chords) {
    var currentTime = 0;
    for (var i = 0; i < chords.length; i++) {
        var chord = chords[i];
        var time = currentTime;
        
        for (var j = 0; j < chord.notes.length; j++) {
            var task = new Task(playNoteAt, this, 
                chord.notes[j], 80, chord.duration || 1000, time);
            task.schedule(time);
            scheduled.push(task);
        }
        
        currentTime += chord.duration || 1000;
    }
}

function playNoteAt(note, velocity, duration, time) {
    outlet(0, note);
    outlet(1, velocity);
    outlet(2, duration);
    outlet(3, 0);
}

function clearScheduled() {
    for (var i = 0; i < scheduled.length; i++) {
        scheduled[i].cancel();
    }
    scheduled = [];
}

function clear() {
    clearScheduled();
    post("Cleared scheduled notes\n");
}
