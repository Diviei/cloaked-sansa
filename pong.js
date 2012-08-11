
function checkKeys(e)
{
	var key = e.keyCode || 0;
	console.log(key);
	if( key == 38 )//  [UP ARROW]
	{
		moveUp();
	};
	if( key == 40 )//  [DOWN ARROW]
	{
		moveDown();
	};
}
$(document).keyup(checkKeys);

function moveUp(elem)
{
	ws.send("moveUp");
}
function moveDown()
{
	ws.send("moveDown");
}

function updatePosition(y)
{
	var elem = $("#test-element");
	$(elem).animate(
	{
		'top': y
	}, 100);
}