
function showTransform(active_item) {
	var current = $(".menu-item-selected");
    var currentId = current.attr("id");
    var next = $("#" + active_item);
    var nextId = next.attr("id");
    if (currentId == nextId) {
        return;
    }
    current.toggleClass("menu-item-selected");
    next.toggleClass("menu-item-selected");
}