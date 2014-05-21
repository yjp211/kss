/**
 * init tree
 */
$(function(){
    if($("#tree").length != 0){
        var tree = new dhtmlXTreeObject("tree", "100%", "100%", 0);
        tree.setImagePath("/static/lib/dhtmlxtree/img/");
        tree.setDataMode("json");
        tree.setXMLAutoLoading("/org/load_dept/");
        tree.loadXML("/org/load_root/");
    }

});
