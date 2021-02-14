var contextMenu = require("sdk/context-menu");
var tabs = require("sdk/tabs");
var menuItem = contextMenu.Item({
       label: "Translate via dict.cc",
       context: contextMenu.SelectionContext(),
       contentScript: 'self.on("click", function () {' +
		      '  var text = window.getSelection().toString();' +
		      '  self.postMessage(text);' +
		      '});',
	onMessage: function (selectionText){
	    //console.log(selectionText);
	    tabs.open("http://www.dict.cc/?s="+selectionText);
	}
 });
