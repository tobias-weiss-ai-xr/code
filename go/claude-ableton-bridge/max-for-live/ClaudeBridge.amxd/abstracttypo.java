{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 5,
			"revision" : 1,
			"architecture" : "x64",
			"modernui" : 1
		},
		"classnamespace" : "box",
		"rect" : [ 397.0, 264.0, 640.0, 480.0 ],
		"bglocked" : 0,
		"openinpresentation" : 0,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"assistshowspatchername" : 0,
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-1",
					"maxclass" : "comment",
					"text" : "Claude-Ableton Bridge\n\nThis device connects Ableton Live to the Claude-Ableton Bridge Go server.\n\nSend prompts to Claude and receive MIDI, chords, melodies, drums, and effects suggestions.\n\nOSC Ports:\n- Send to Bridge: 127.0.0.1:7400\n- Receive from Bridge: 127.0.0.1:7401",
					"linecount" : 10,
					"presentation" : 1,
					"numoutlets" : 0,
					"fontsize" : 12.0,
					"patching_rect" : [ 20.0, 10.0, 340.0, 145.0 ],
					"presentation_rect" : [ 20.0, 10.0, 340.0, 145.0 ],
					"fontname" : "Arial",
					"numinlets" : 1,
					"textcolor" : [ 0.2, 0.6, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-2",
					"maxclass" : "comment",
					"text" : "Response from Claude:",
					"presentation" : 1,
					"numoutlets" : 0,
					"fontsize" : 11.0,
					"patching_rect" : [ 20.0, 280.0, 120.0, 20.0 ],
					"presentation_rect" : [ 20.0, 280.0, 120.0, 20.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-3",
					"linecount" : 3,
					"maxclass" : "comment",
					"text" : "Click 'Connect' to start the OSC connection. The bridge must be running first!",
					"presentation" : 1,
					"numoutlets" : 0,
					"fontsize" : 10.0,
					"patching_rect" : [ 380.0, 10.0, 220.0, 47.0 ],
					"presentation_rect" : [ 380.0, 10.0, 220.0, 47.0 ],
					"fontname" : "Arial",
					"numinlets" : 1,
					"textcolor" : [ 0.5, 0.5, 0.5, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-4",
					"maxclass" : "button",
					"presentation" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 380.0, 65.0, 24.0, 24.0 ],
					"presentation_rect" : [ 380.0, 65.0, 24.0, 24.0 ],
					"numinlets" : 1,
					"bgcolor" : [ 0.2, 0.8, 0.4, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-5",
					"maxclass" : "comment",
					"text" : "Connect",
					"presentation" : 1,
					"numoutlets" : 0,
					"fontsize" : 11.0,
					"patching_rect" : [ 410.0, 67.0, 53.0, 20.0 ],
					"presentation_rect" : [ 410.0, 67.0, 53.0, 20.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-6",
					"maxclass" : "newobj",
					"text" : "udpsend 127.0.0.1 7400",
					"numoutlets" : 0,
					"fontsize" : 12.0,
					"patching_rect" : [ 550.0, 200.0, 143.0, 22.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-7",
					"maxclass" : "newobj",
					"text" : "udpreceive 7401",
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"fontsize" : 12.0,
					"patching_rect" : [ 20.0, 200.0, 103.0, 22.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-8",
					"linecount" : 3,
					"maxclass" : "comment",
					"text" : "Route OSC messages to appropriate handlers",
					"numoutlets" : 0,
					"fontsize" : 10.0,
					"patching_rect" : [ 150.0, 230.0, 150.0, 43.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-9",
					"maxclass" : "newobj",
					"text" : "osc.route /claude/response /claude/error /claude/midi/data /claude/chord/data /claude/drums/data /claude/melody/data",
					"numoutlets" : 7,
					"outlettype" : [ "", "", "", "", "", "", "" ],
					"fontsize" : 10.0,
					"patching_rect" : [ 20.0, 230.0, 520.0, 20.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-10",
					"maxclass" : "newobj",
					"text" : "prepend set",
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"fontsize" : 12.0,
					"patching_rect" : [ 20.0, 265.0, 80.0, 22.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-11",
					"maxclass" : "comment",
					"text" : "Error",
					"numoutlets" : 0,
					"patching_rect" : [ 140.0, 265.0, 44.0, 20.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-12",
					"maxclass" : "newobj",
					"text" : "print error",
					"numoutlets" : 0,
					"fontsize" : 12.0,
					"patching_rect" : [ 140.0, 290.0, 70.0, 22.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-13",
					"maxclass" : "comment",
					"text" : "MIDI Data",
					"numoutlets" : 0,
					"patching_rect" : [ 230.0, 265.0, 60.0, 20.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-14",
					"maxclass" : "newobj",
					"text" : "midiout",
					"numoutlets" : 0,
					"fontsize" : 12.0,
					"patching_rect" : [ 230.0, 360.0, 54.0, 22.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-15",
					"maxclass" : "comment",
					"text" : "Chord Data",
					"numoutlets" : 0,
					"patching_rect" : [ 310.0, 265.0, 69.0, 20.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-16",
					"maxclass" : "newobj",
					"text" : "midiout",
					"numoutlets" : 0,
					"fontsize" : 12.0,
					"patching_rect" : [ 310.0, 360.0, 54.0, 22.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-17",
					"maxclass" : "comment",
					"text" : "Drums Data",
					"numoutlets" : 0,
					"patching_rect" : [ 390.0, 265.0, 71.0, 20.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-18",
					"maxclass" : "newobj",
					"text" : "midiout",
					"numoutlets" : 0,
					"fontsize" : 12.0,
					"patching_rect" : [ 390.0, 360.0, 54.0, 22.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-19",
					"maxclass" : "comment",
					"text" : "Melody Data",
					"numoutlets" : 0,
					"patching_rect" : [ 470.0, 265.0, 76.0, 20.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-20",
					"maxclass" : "newobj",
					"text" : "midiout",
					"numoutlets" : 0,
					"fontsize" : 12.0,
					"patching_rect" : [ 470.0, 360.0, 54.0, 22.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-21",
					"maxclass" : "comment",
					"text" : "Send Prompt",
					"presentation" : 1,
					"numoutlets" : 0,
					"fontsize" : 11.0,
					"patching_rect" : [ 20.0, 165.0, 75.0, 20.0 ],
					"presentation_rect" : [ 20.0, 165.0, 75.0, 20.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-22",
					"maxclass" : "message",
					"text" : "Generate a jazzy chord progression",
					"presentation" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"fontsize" : 12.0,
					"patching_rect" : [ 20.0, 190.0, 200.0, 22.0 ],
					"presentation_rect" : [ 20.0, 190.0, 200.0, 22.0 ],
					"fontname" : "Arial",
					"numinlets" : 2
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-23",
					"maxclass" : "button",
					"presentation" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 230.0, 190.0, 20.0, 20.0 ],
					"presentation_rect" : [ 230.0, 190.0, 20.0, 20.0 ],
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-24",
					"maxclass" : "newobj",
					"text" : "osc.parse",
					"numoutlets" : 2,
					"outlettype" : [ "osc-message", "int" ],
					"fontsize" : 12.0,
					"patching_rect" : [ 20.0, 215.0, 70.0, 22.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-25",
					"maxclass" : "newobj",
					"text" : "osc.build /claude/prompt",
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"fontsize" : 12.0,
					"patching_rect" : [ 550.0, 150.0, 144.0, 22.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-26",
					"maxclass" : "newobj",
					"text" : "pack osc s 0",
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"fontsize" : 12.0,
					"patching_rect" : [ 550.0, 120.0, 88.0, 22.0 ],
					"fontname" : "Arial",
					"numinlets" : 3
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-27",
					"maxclass" : "inlet",
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 20.0, 120.0, 30.0, 30.0 ],
					"numinlets" : 0,
					"comment" : "Prompt input"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-28",
					"maxclass" : "outlet",
					"numoutlets" : 0,
					"patching_rect" : [ 20.0, 390.0, 30.0, 30.0 ],
					"numinlets" : 1,
					"comment" : "MIDI out"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-29",
					"maxclass" : "comment",
					"text" : "<-- Send text prompts here",
					"numoutlets" : 0,
					"patching_rect" : [ 55.0, 125.0, 150.0, 20.0 ],
					"fontname" : "Arial",
					"numinlets" : 1
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"source" : [ "obj-27", 0 ],
					"destination" : [ "obj-22", 0 ],
					"midpoints" : [ 29.5, 155.0, 29.5, 180.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-22", 0 ],
					"destination" : [ "obj-25", 0 ],
					"midpoints" : [ 29.5, 230.0, 559.5, 230.0, 559.5, 140.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-23", 0 ],
					"destination" : [ "obj-22", 0 ],
					"midpoints" : [ 239.5, 215.0, 29.5, 215.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-25", 0 ],
					"destination" : [ "obj-26", 0 ],
					"midpoints" : [ 559.5, 180.0, 490.0, 180.0, 490.0, 110.0, 559.5, 110.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-26", 0 ],
					"destination" : [ "obj-4", 0 ],
					"midpoints" : [ 559.5, 150.0, 389.5, 150.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-4", 0 ],
					"destination" : [ "obj-6", 0 ],
					"midpoints" : [ 389.5, 100.0, 660.0, 100.0, 660.0, 180.0, 559.5, 180.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-7", 0 ],
					"destination" : [ "obj-9", 0 ],
					"midpoints" : [ 29.5, 225.0, 29.5, 225.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-9", 0 ],
					"destination" : [ "obj-10", 0 ],
					"midpoints" : [ 29.5, 260.0, 29.5, 260.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-9", 1 ],
					"destination" : [ "obj-12", 0 ],
					"midpoints" : [ 140.0, 260.0, 149.5, 260.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-9", 2 ],
					"destination" : [ "obj-14", 0 ],
					"midpoints" : [ 250.5, 310.0, 239.5, 310.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-9", 3 ],
					"destination" : [ "obj-16", 0 ],
					"midpoints" : [ 328.5, 300.0, 319.5, 300.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-9", 4 ],
					"destination" : [ "obj-18", 0 ],
					"midpoints" : [ 406.5, 290.0, 399.5, 290.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-9", 5 ],
					"destination" : [ "obj-20", 0 ],
					"midpoints" : [ 484.5, 280.0, 479.5, 280.0 ]
				}

			}
 ],
		"dependency_cache" : [ 			{
				"name" : "osc.route.maxpat",
				"bootpath" : "~/Documents/Max 8/Library",
				"patcherrelpath" : ".",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "osc.build.maxpat",
				"bootpath" : "~/Documents/Max 8/Library",
				"patcherrelpath" : ".",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "osc.parse.maxpat",
				"bootpath" : "~/Documents/Max 8/Library",
				"patcherrelpath" : ".",
				"type" : "JSON",
				"implicit" : 1
			}
 ],
		"autosave" : 0
	}
}
